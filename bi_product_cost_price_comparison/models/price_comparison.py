from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def view_purchase_order_pivot(self):
        context= (self._context.get('active_ids'))       
        pivot_view_id = self.env.ref('bi_product_cost_price_comparison.view_purchase_order_pivot_1').id
        return {
            'type': 'ir.actions.act_window',
            'name': _('Price Comparison'),
            'res_model': 'purchase.order.line',
            'view_type': 'form',
            'view_mode': 'pivot',
            'views': [(pivot_view_id, 'pivot')],
            'domain': [('order_id', 'in', context)],
        }

