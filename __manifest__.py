{
    "name": "Configuración de Utilidad por Defecto",
    "version": "1.0",
    "depends": ["base", "sale"],
    "author": "damred",
    "category": "Sales",
    "description": "Permite configurar y guardar una utilidad por defecto que se extrae en las líneas de venta.",
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
