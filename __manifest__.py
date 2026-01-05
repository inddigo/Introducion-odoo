{
    'name': 'Módulo Introducción',
    'version': '1.0',
    'summary': 'Módulo de introducción a Odoo',
    'description': 'Modulo para gestion de productos y partes',
    'author': 'Joshua',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/producto_views.xml',
        'views/parte_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}