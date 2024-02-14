# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _
from odoo.exceptions import UserError


class res_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    warning_child_task = fields.Many2one('project.task.type', 'Prevent stage to change untill all task on same stage')

    @api.model
    def get_values(self):
        res = super(res_config_settings, self).get_values()
        warning_child_task = self.env['ir.config_parameter'].sudo().get_param('bi_subtask.warning_child_task')
        if warning_child_task:
            res.update(
                warning_child_task=int(warning_child_task),

            )
        return res

    def set_values(self):
        res = super(res_config_settings, self).set_values()
        warning_child_task = self.env['ir.config_parameter'].sudo().set_param('bi_subtask.warning_child_task',
                                                                              self.warning_child_task.id)
        return res


class subtask_wizard(models.Model):
    _name = 'subtask.wizard'
    _description = "Subtask Wizard"

    subtask_lines = fields.One2many('project.task', 'wiz_id', string="Task Line")

    def create_subtask(self):
        list_of_stage = []
        project_task_id = self.env['project.task'].browse(self._context.get('active_id'))
        for stage in project_task_id.project_id.type_ids:
            stage_ids = self.env['project.task.type'].search([('id', '=', stage.id)])
            list_of_stage.append(stage_ids.id)
        for task in self.subtask_lines:
            task.task_parent_id = self._context.get('active_id')
            task.description = task.des
            task.is_subtask = True
            task.project_id = project_task_id.project_id.id
            if list_of_stage:
                task.stage_id = list_of_stage[0]

        return True


class ProjectTask(models.Model):
    _inherit = "project.task"

    wiz_id = fields.Many2one('subtask.wizard', string="Wiz Parent Id")
    task_parent_id = fields.Many2one('project.task', string="Parent Id" )
    subtask_ids = fields.One2many('project.task', 'task_parent_id', string="Subtask")
    test = fields.Char("Test")
    des = fields.Char('Task Description')
    is_subtask = fields.Boolean('Is a subtask')
    planned_hours=fields.Float('Planned hours')
#
#
#
#
#
#     def _ensure_fields_are_accessible(self, fields, operation='read', check_group_user=True):
#         assert operation in ('read', 'write'), 'Invalid operation'
#         check_group_user = True
#         if fields and (not check_group_user or self.env.user.has_group('base.group_portal')) and not self.env.su:
#             unauthorized_fields = set(fields) - (self.SELF_READABLE_FIELDS if operation == 'read' else self.SELF_WRITABLE_FIELDS)
#             if unauthorized_fields:
#                 self.custom_fields_access(unauthorized_fields,operation)
#
#     def custom_fields_access(self,unauthorized_fields,operation):
#         if operation == 'read':
#             error_message = _('You cannot read %s fields in task.', ', '.join(unauthorized_fields))
#         else:
#             error_message = _('You cannot write on %s fields in task.', ', '.join(unauthorized_fields))
#
#
    @api.onchange('parent_id')
    def button_disable(self):
        if self.parent_id:
            self.is_subtask = True
            self.task_parent_id = self.parent_id.id
            self.project_id = self.parent_id.project_id
        else:
            self.is_subtask = False
            self.project_id = False

    def cancel_test(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    # def _compute_subtask_count(self):
    #     result = super(ProjectTask, self)._compute_subtask_count()
    #     for task in self:
    #         task_ids = self.env['project.task'].search([('task_parent_id', '=', task.id)])
    #         if task_ids:
    #             task.subtask_count = len(task_ids)
    #             task.parent_id = task.task_parent_id
    #     return result

    @api.onchange('stage_id')
    def button_is_visible(self):
        if self.stage_id.name == 'Done' or self.stage_id.name == 'done' and self.parent_id and not self.task_parent_id:
            self.is_subtask = True
        else:
            self.is_subtask = False



    def write(self, vals):
        if vals.get('stage_id'):
            task_type_search = self.env['ir.config_parameter'].sudo().get_param('bi_subtask.warning_child_task')

            if task_type_search:

                if vals.get('stage_id') == int(task_type_search):
                    for task in self.subtask_ids:
                        if task.stage_id.id != int(task_type_search):
                            raise UserError("You can not close parent task until all child tasks are closed.")
        return super(ProjectTask, self).write(vals)
