# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Split Invoices/Bills/Credit Notes/Debit Notes',
    'version': '17.0.0.0',
    'category': 'Accounting',
    'summary': 'Split Bills split credit notes Extract Invoices split customer invoices extract bills split debit notes splitting invoice splitting bills splitting vendor bill split vendor bills Extract invoice lines split invoice lines split vendor bill lines splitting',
    'description': """

        Split or Extract Invoice in odoo,
        Split or Extract Bill in odoo,
        Split or Extract Credit Note in odoo,
        Split or Extract Debit Note in odoo,
        Check or Uncheck Invoice Lines in odoo,
        Splited Invoice Number in odoo,
        Extracted Invoice Number in odoo,

    """,
    'author': 'BrowseInfo',
    "price": 12,
    "currency": 'EUR',
    'website': 'https://www.browseinfo.com',
    'depends': ['base', 'account'],
    'data': [
        'security/allow_split_invoice.xml',
        'security/ir.model.access.csv',
        'wizard/split_invoice_wizard_view.xml',
        'views/invoice_action.xml',
        'views/invoice_view.xml',
    ],
    'demo': [],
    'test': [],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/irhdODNtGO8',
    "images":['static/description/Banner.gif'],
}
