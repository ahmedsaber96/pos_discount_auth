# -*- coding: utf-8 -*-
{
    "name": """POS discount authorization""",
    "summary": """Provides authorization code for discounts in POS""",
    "category": "Sales/POS discount authorization",
    "version": "16.0.0.1.0.0",
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
            'pos_discount_auth/static/src/js/Popups/DiscountAuthPopup.js',
            'pos_discount_auth/static/src/js/Screens/ProductScreen/CustomNumpadWidget.js',
            'pos_discount_auth/static/src/xml/Popups/DiscountAuthPopup.xml'
        ]
    },
    'images': [
               'static/description/thumbnail.png',
               'static/description/banner_discount.png',
               'static/description/code_screen.png',
               'static/description/discount.png',
               'static/description/discount_settings.png',
               'static/description/icon.png',],
    "auto_install": False,
    "installable": True,
    "application": True,
}
