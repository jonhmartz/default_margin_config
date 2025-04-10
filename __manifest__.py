{
    "name": "Default Margin Config",
    "version": "1.0",
    "depends": ["base", "sale"],
    "author": "AutoGen",
    "category": "Sales",
    "summary": "Configura una utilidad por defecto para líneas de venta",
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml",
        "views/menu.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}
