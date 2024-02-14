# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "User Direct POS Login to POS Screen Odoo App",
    "version" : "17.0.0.0",
    "category" : "Point of Sale",
    "depends" : ['base','sale_management','point_of_sale','website'],
    'external_dependencies': {
            'python': ['easygui']
        },
    "author": "BrowseInfo",
    'summary': 'Apps allows to Redirect on POS screen without going to backend POS Direct Login Odoo POS screen login POS user POS session login User Direct Login pos screen login point of sales direct pos login pos sign in pos signin direct pos direct sign in pos access',
    "description": """
    
    Purpose :- 
This apps allows you to Redirect on 
odoo POS screen without going backend once login. 
odoo login pos login pos cashier login pos direct 
odoo RFID POS Login odoo User Login to POS Screen
odoo pos screen login pos screen log in 
odoo Direct Login to POS odoo direct sign to pos
odoo user login to pos screen odoo pos screen login 
odoo pos sign in odoo direct pos sign in POS Direct Login
odoo Direct Login to POS odoo POS User Login
odoo login pos user POS screen login POS user to directly on POS screen

odoo point of sales Direct Login Without Odoo Backend pos user login POS Direct Login
odoo POS Direct Login Without Odoo Backend pos login screen directly 
odoo Direct login into POS Odoo POS Portal Login POS Portal Login
odoo POS User Login Management default POS session Direct Login to POS
odoo point of sales login point of sale login point of sale cashier login point of sales cashier login
odoo point of sale direct login point of sale user login point of sales login
odoo pos screen directly point of sales cashier login point of sales direct login point of sales user login
    
    """,
    "website" : "https://www.browseinfo.com",
    "price": 13.48,
    "currency": "EUR",
    "data": ['views/custom_pos_view.xml'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_login_odoo/static/src/js/gui.js',
        ],
    },
    "auto_install": False,
    "installable": True,
    "live_test_url":'https://youtu.be/UkGZ-fb6GBM',
    "images":['static/description/Banner.gif'],
    'license': 'OPL-1',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
