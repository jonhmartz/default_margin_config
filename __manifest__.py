{
    "name": "Utilidad por Defecto",
    "version": "1.0",
    "summary": "Define una utilidad por defecto que se usa en ventas y cotizaciones",
    "category": "Sales",
    "author": "TuNombre",
    "license": "LGPL-3",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_view.xml",
        "views/sale_order_line_view.xml"
    ],
    "installable": True,
    "application": True
}
