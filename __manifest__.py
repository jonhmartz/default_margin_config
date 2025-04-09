{
    "name": "Default Margin Config",
    "version": "1.0",
    "depends": ["sale"],
    "author": "TuNombre",
    "category": "Sales",
    "description": "Configura una utilidad por defecto para líneas de ventas.",
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml",
        "views/menu.xml"
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}