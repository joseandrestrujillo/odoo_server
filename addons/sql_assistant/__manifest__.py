{
    'name': 'SQL Assistant',
    'version': '1.0',
    'category': 'Tools',
    'description': 'Adds a SQL assistant tab to the user interface.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/sql_assistant_view.xml',
    ],
    'installable': True,
}
