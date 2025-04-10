{
    'name': 'Default Margin Config',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Configure default margin for sales',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/margin_config_view.xml',
        'views/sale_order_line_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
