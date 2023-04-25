# -*- coding: utf-8 -*-
{
    'name': "Asistente SQL",
    'application': True,
    'summary': """
        Cualquier consulta a los datos de tu empresa, sin complicaciones.
        """,

    'description': """
        Este modulo te permite realizar consultas sobre los datos de tu e-comerce en lenguaje natural.
    """,

    'author': "Ai2SQL",
    'website': "http://www.google.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'icon': '/sql_assistant/static/src/logo.png',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
