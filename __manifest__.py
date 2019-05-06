# -*- coding: utf-8 -*-
{
    'name': "KCRA_ProductManage",

    'summary': """
        Gestió de Cripto Monedes.
        """,

    'description': """
        Descripció del modul de KryptoCoins, gestiona, crea, visualitza la gestió de les Cripto Monedes.
    """,

    'author': "Mario & Victor",
    'website': "http://www.kriptocoins.ra",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Coins',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}