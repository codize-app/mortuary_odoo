# -*- coding: utf-8 -*-
{
    'name': "Odoo for Mortuary business",

    'summary': """
        Odoo for Mortuary business""",

    'description': """
        Odoo for Mortuary business
    """,

    'author': "Codize",
    'website': "https://www.codize.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
