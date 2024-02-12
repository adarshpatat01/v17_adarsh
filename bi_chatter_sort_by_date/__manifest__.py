# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Chatter Sorting',
    'version': '17.0.0.0',
    'category': 'Extra Tools',
    'summary': "Chatter sorting by date portal chatter box sort by dates website chatter sort chat messages arrange by date wise chatter entries on portal chatter arranging by date wise chatter box sorting by date in chatter sort by date chatter messages",
    'description': """

        Chatter Sorting Odoo App helps users to sorting out chatter based on the date. User have option to sort by date button in the chatter to sorting the chat date wise and in the portal also there will be an option of sorting the chatter.

    """,
    'author': 'BrowseInfo',
    "price": 39,
    "currency": 'EUR',
    'website': 'https://www.browseinfo.com',
    'depends': ['mail'],
    'assets': {
        'web.assets_backend': [
            'bi_chatter_sort_by_date/static/src/xml/chatter_topbar.xml',
            'bi_chatter_sort_by_date/static/src/js/new.js',
        ],
        'web.assets_frontend': [
            'bi_chatter_sort_by_date/static/src/js/portal_chatter.js',
            'bi_chatter_sort_by_date/static/src/xml/portal_chatter.xml',
        ],
    },
    'license':'OPL-1',
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/Y9b4qHmpe3Q',
    "images":['static/description/Chatter-Sorting-Banner.gif'],
}