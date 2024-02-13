# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Advance POS Products Tags',
    'version': '17.0.0.0',
    'category': 'Point of Sale',
    'summary': 'Product tag on pos product tag apply product tag on pos product filter by tag pos tag filter pos product tag filter apply tag filter on pos tag point of sale tag point of sale product tag pos order filter by tag pos order tag product tag on pos filter tag',
    'description': """
       Odoo POS Filter Products by Tags module allows you to filter products on the basis of tags assigned to the product.
        With the help of this module, Seller can create different tags and assign these tags to the products such that seller can
         filter product in POS Session on the basis of these tags. A seller can assign multiple tags to the product.
         Also, a seller can create or assign tags to the product at any time in running POS session.
    """,
    'author': 'BrowseInfo',
    'website': 'https://www.browseinfo.com',
    "price": 39,
    "currency": 'EUR',
    'depends': ['point_of_sale','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/point_of_sale.xml',
        'views/product_view.xml',
        'views/product_tag_view.xml',
    ],
    'qweb': [
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'bi_pos_advance_tag/static/src/css/pos.css',
            'bi_pos_advance_tag/static/src/app/models.js',
            # 'bi_pos_advance_tag/static/src/app/posdb.js',
            # 'bi_pos_advance_tag/static/src/app/pos_store.js',
            
            # 'bi_pos_advance_tag/static/src/app/addproducttagpopup.js',
            # 'bi_pos_advance_tag/static/src/app/addproducttagpopup.xml',
            # 'bi_pos_advance_tag/static/src/app/productscreen.js',
            # 'bi_pos_advance_tag/static/src/app/productwidget.js',
            # 'bi_pos_advance_tag/static/src/app/productwidget.xml',
            # 'bi_pos_advance_tag/static/src/app/successfullremovetagpopup.js',
            # 'bi_pos_advance_tag/static/src/app/successfullremovetagpopup.xml',
            # 'bi_pos_advance_tag/static/src/app/successtagpopup.js',
            # 'bi_pos_advance_tag/static/src/app/successtagpopup.xml',
            
            

        ],
    },
    'installable': True,
    'auto_install': False,
    'live_test_url': 'https://youtu.be/rzM0cdg-xAM',
    "images":['static/description/Banner.gif'],
    'license': 'OPL-1'
}
