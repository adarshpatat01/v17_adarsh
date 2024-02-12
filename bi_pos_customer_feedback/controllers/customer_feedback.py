from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.web import Home

class WebsiteCustomer(http.Controller):
    @http.route(['/customer-feedback-form/<int:contact_name>/<string:receipt_name>'], type='http', auth="public", website=True)
    def customer_feedback(self, contact_name=False, receipt_name=False, **kw):
        partner = request.env['res.partner'].sudo().browse(contact_name)
        values ={'name': partner.name, 'receipt_number': receipt_name}
        return request.render("bi_pos_customer_feedback.customer_feedback_form",values)

    @http.route(['/unsubscribe/<int:contact_name>'], type='http', auth="public",website=True)
    def unsubscribe(self, contact_name=False, **kw):
        partner = request.env['res.partner'].sudo().browse(contact_name)
        partner.feedback_email = False
        return request.render("bi_pos_customer_feedback.unsubscribe_page")

    @http.route('/feedback/form/submit', type='http', auth="public",website=True, sitemap=False)
    def feedback_form_submit(self, **post):
        pos_order = request.env['pos.order'].sudo().search([('pos_reference','=',post.get('receipt_number'))])
        pos_order.service = post.get('service_val')
        pos_order.product = post.get('product_val')
        pos_order.price = post.get('price_val')
        pos_order.order_billing = post.get('order_bill_val')
        pos_order.shopping_exp = post.get('shop_exp_val')
        pos_order.customer_review = post.get('customer_review')
        value = {'name': pos_order.partner_id.name}
        return request.render("bi_pos_customer_feedback.feedback_thank_you_page", value)


