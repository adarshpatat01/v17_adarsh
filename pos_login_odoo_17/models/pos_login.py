# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    pos_config = fields.Many2one('pos.config', string="Point of Sale")

    def get_config_id(self, session_uid):
        user_id = self.browse(session_uid)
        res = False
        if user_id.pos_config:
            res = True
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
