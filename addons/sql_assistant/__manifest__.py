{
    'name': 'SQL Assistant',
    'version': '1.0',
    'summary': 'Module for SQL Assistance',
    'description': 'Module for SQL Assistance',
    'author': 'Your Name',
    'depends': ['base', 'model_sql_assistant'],
    'data': [
        'security/ir.model.access.csv',
        'views/sql_assistant_view.xml',
    ],
    'application': True,
    'auto_install': False,
    'installable': True,
}
