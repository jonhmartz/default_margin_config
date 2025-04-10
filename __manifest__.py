
{
    "name": "Default Margin Config",
    "summary": "Utilidad por defecto para líneas de venta",
    "version": "1.0",
    "category": "Sales",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml",
        "views/menu.xml"
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}
