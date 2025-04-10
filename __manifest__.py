{
    "name": "Default Margin Config",
    "version": "1.0",
    "category": "Sales",
    "summary": "Configura un porcentaje de utilidad por defecto para ventas",
    "description": "Permite establecer un porcentaje de utilidad por defecto que se aplica en las líneas de venta.",
    "author": "Tu Nombre o Empresa",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "data/config_data.xml",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml",
        "views/menu.xml"
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True
}