# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'POS Customer Feedback and Rating',
    'version': '17.0.0.0',
    'category': 'Point of Sale',
    'summary': 'POS customer survey point of sale customer review on POS client rating for POS order customer feedback for point of sales customer review for POS order client feedback customer POS feedback POS rating POS review POS order survey',
    'description': """POS Customer Feedback Odoo App redefines the customer experience at the point of sale by getting customer feedback. User can configure to send feedback email and customer will receive and email once POS order paid, Customer can provide ratings and review and also can unsubscribe from receiving feedback email.""",
    'author': 'BrowseInfo',
    'website': 'https://www.browseinfo.com',
    "price": 49,
    "currency": 'EUR',
    'depends': ['base', 'website','sale', 'point_of_sale','website_sale'],
    'data': [
        'data/customer_feedback_mail_template.xml',
        'views/res_partner_view.xml',
        'views/pos_order_view.xml',
        'views/customer_feedback_form_template.xml',
        'views/thank_you_page.xml',
        'views/unsubscribe_page.xml',
        'views/pos_order_report.xml',
    ],
    'demo': [],
    'test': [],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend':[
            'bi_pos_customer_feedback/static/src/css/mail_button.css',
        ],
        'web.assets_frontend':[
            'bi_pos_customer_feedback/static/src/css/website_form.css',
        ],
        'point_of_sale._assets_pos': [
            'bi_pos_customer_feedback/static/src/app/pos_store.js',
        ]
    },
    'installable': True,
    'auto_install': False,
    'live_test_url': 'https://youtu.be/3R7YjT2mRzc',
    "images": ['static/description/POS-Customer-Feedback.gif'],
}
