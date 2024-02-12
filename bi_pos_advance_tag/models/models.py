# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class PosConfig(models.Model):
    _inherit = "pos.config"

    enable_product_tag = fields.Boolean(string="Enable Product tag")

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_product_tag = fields.Boolean(related='pos_config_id.enable_product_tag',readonly=False)

class POSProductTag(models.Model):
    _name = 'pos.product.tag'
    _description = 'Product Tag'

    name = fields.Char(string='Tag Name')

    @api.model
    def add_tag_operation(self, tag, product):
        tag_new = self.env['pos.product.tag'].sudo().search([('name', '=', tag)], limit=1)
        if not tag_new:
            tag_new = self.create({'name': tag})

        prod1 = self.env['product.product'].sudo().browse(product)
        prod1.sudo().write({'tag_ids': [(4, tag_new.id)]})
        return [tag_new.id, tag_new.name]

    @api.model
    def remove_tag_operation(self, tag, product):
        tag_new = self.env['pos.product.tag'].sudo().search([('name', '=', tag)], limit=1)
        prod1 = self.env['product.product'].sudo().browse(product)
        l = []
        for i in prod1.tag_ids:
            if i.id == tag_new.id:
                continue
            else:
                l.append(i.id)
        prod1.sudo().update({'tag_ids': [(6, 0, l)]})
        return [tag_new.id, tag_new.name]


class ProductProduct(models.Model):
    _inherit = 'product.product'
    _description = 'Product Product Inherit'

    tag_ids = fields.Many2many("pos.product.tag",
                               string='Product By Tags')


class POSOrderLoad(models.Model):
    _inherit = 'pos.session'


    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].extend(['tag_ids'])
        return result

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        new_model = 'pos.product.tag'
        if new_model not in result:
            result.append(new_model)
        return result

    def _loader_params_pos_product_tag(self):
        return {
            'search_params': {
                'domain': [],
                'fields': [
                    'id','name',
                ],
            }
        }

    def _get_pos_ui_pos_product_tag(self, params):
        return self.env['pos.product.tag'].search_read(**params['search_params'])