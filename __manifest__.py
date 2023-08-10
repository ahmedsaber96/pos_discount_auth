# -*- coding: utf-8 -*-
{
    "name": """POS discount authorization code""",
    "summary": """Provides authorization code for discounts in POS""",
    "category": "Point of Sale",
    "version": "16.0.0",
    "author": "Ahmed Saber",
    "support": "developersaber@gmail.com",
    "website": "http://developersaber.com",
    "license": "LGPL-3",
    "depends": [
        "pos_discount",
    ],
    'price': 0.00,
    "data": [
        'views/pos_config_view.xml',
    ],
'assets': {
        'point_of_sale.assets':[
            'pos_discount_auth/static/src/js/config.js',
            'pos_discount_auth/static/src/js/discount.js'
        ]
    },
    "qweb": ['static/src/xml/pos_code_view.xml'],
    'images': ['static/description/thumbnail.png',
                'static/description/banner_discount.png',
               'static/description/code_screen.png',
               'static/description/discount.png',
               'static/description/discount_settings.png',
               'static/description/icon.png',],
    "auto_install": False,
    "installable": True,
    "application": False,
}
