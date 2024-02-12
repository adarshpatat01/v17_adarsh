# -*- coding: utf-8 -*-

from odoo import api, fields, models , tools
import base64

class ResPartner(models.Model):
    _inherit = 'res.partner'

    feedback_email = fields.Boolean(string="Feedback Email")

    def send_customer_feedback_mail(self,customer,current_order):
        partner = self.env['res.partner'].browse(customer.get('id'))
        pos_order = self.env['pos.order'].sudo().search([('pos_reference', '=', current_order)])
        template = self.env.ref('bi_pos_customer_feedback.customer_feedback_mail_template',raise_if_not_found=False)
        email_values = {'email_to': customer.get('email')}
        message = ''
        message += '<p>Dear %s ,</p>' % partner.name
        message += '<br></br>'
        message += '<p>Thank you for visiting our store. Please click on the button below to provide us with your ' \
                   'valuable comments.</p>'
        message += '<br></br>'
        message += "<a class='mail_btn' href='/customer-feedback-form/%s/%s'>For Feedback, Please Click Here.</a>" % (partner.id, current_order)
        message += '<br></br>'
        message += '<br></br>'
        message += '<p>If you have any questions, don\'t be afraid to ask.</p>'
        message += '<br></br>'
        message += "<div class='text-center p-4'><a class='mail_btn' href='/unsubscribe/%s'>UNSUBSCRIBE</a></div>" % (partner.id)
        report = self.env['ir.actions.report']._render_qweb_pdf("bi_pos_customer_feedback.pos_order_report_card_pdf", pos_order.id)
        filename = pos_order.name
        attachment_data = {
            'name': '%s.pdf' % filename,
            'datas': base64.b64encode(report[0]),
            'res_model': 'pos.order',
            'res_id': pos_order.id,
            'mimetype': 'application/x-pdf',
            'type': 'binary',
        }
        pos_attachment = self.env['ir.attachment'].sudo().create(attachment_data)
        template.attachment_ids = [(6, 0, [pos_attachment.id])]
        if customer.get('email'):
            partner.message_post(attachments=[('%s.pdf' % filename, report[0])], body=message)
            template.with_context(customer=customer.get('id'), customer_name=customer.get('name'), receipt_number=current_order).send_mail(self.id, email_values=email_values, force_send=True)




