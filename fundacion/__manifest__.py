# -*- coding: utf-8 -*-
{
    'name': "fundacion",

    'summary': """
        Es una fundación de perritos""",

    'description': """
        Ayudamos a los perritos de la calle a buscar un nuevo hogar
    """,

    'author': "Peluditos SAS",
    'website': "http://www.peluditos.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Fundacion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
