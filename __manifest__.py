{
    "name": "Configuración de Utilidad por Defecto",
    "version": "1.0",
    "depends": ["base", "sale"],
    "author": "Tu Empresa",
    "category": "Sales",
    "description": "Permite configurar una utilidad por defecto para las líneas de venta.",
    "data": [
        "data/model_ir_data.xml",
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml",
        "views/menu.xml"
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
