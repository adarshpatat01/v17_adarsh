# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools


class PosOrder(models.Model):
    _inherit = 'pos.order'

    service = fields.Char(string="Overall Service")
    product = fields.Char(string="Product")
    price = fields.Char(string="Price")
    order_billing = fields.Char(string="Ordering & Billing")
    shopping_exp = fields.Char(string="Shopping Experience")
    customer_review = fields.Text(string="Feedback Comment")

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].append('feedback_email')
        return result
