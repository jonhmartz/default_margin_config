{
    "name": "Default Margin Config",
    "version": "1.0",
    "category": "Sales",
    "depends": ["sale", "base"],
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml",
        "views/menu.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}
