{
    "name": "Configuración de Utilidad por Defecto",
    "version": "1.0",
    "category": "Sales",
    "summary": "Permite configurar una utilidad por defecto para ventas",
    "author": "Tu Empresa",
    "depends": ["base", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml"
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}