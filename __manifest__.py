{
    'name': 'Default Margin Config',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/margin_config_views.xml',
        'views/sale_order_line_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
