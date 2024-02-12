# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import api, fields, models

class POSOrderReport(models.AbstractModel):
    _name = 'report.bi_pos_customer_feedback.report_card'
    _description = 'POS Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['pos.order'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'pos.order',
            'docs': docs,
            'proforma': True
        }
