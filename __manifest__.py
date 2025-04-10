{
    'name': 'Default Margin Config',
    'version': '1.0',
    'summary': 'Configuración de utilidad por defecto para ventas',
    'category': 'Sales',
    'author': 'TuNombre',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/default_margin_config_view.xml',
    ],
    'installable': True,
    'application': True,
}
