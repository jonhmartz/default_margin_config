{
    "name": "Default Margin Config",
    "summary": "Configura una utilidad por defecto para líneas de venta",
    "version": "1.0",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3"
}