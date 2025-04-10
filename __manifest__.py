{
    "name": "Default Margin Config",
    "version": "1.0",
    "summary": "Configura una utilidad por defecto para líneas de venta",
    "category": "Sales",
    "author": "ChatGPT",
    "license": "LGPL-3",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/menu.xml",
        "views/sale_order_line_view.xml",
        "data/model_data.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}
