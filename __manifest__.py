{
    "name": "Default Margin Config",
    "version": "1.0",
    "depends": ["sale"],
    "author": "AutoGen",
    "category": "Sales",
    "description": "Configuración global de utilidad para ventas.",
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml"
    ],
    "installable": True,
    "application": True,
}