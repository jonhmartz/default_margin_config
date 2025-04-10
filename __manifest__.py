{
    "name": "Configuración de Utilidad por Defecto",
    "version": "1.0",
    "depends": ["base", "sale"],
    "author": "ChatGPT",
    "category": "Sales",
    "description": "Permite configurar una utilidad por defecto y aplicarla a las líneas de venta.",
    "data": [
        "security/ir.model.access.csv",
        "views/margin_config_view.xml",
        "views/sale_order_line_view.xml",
        "views/actions.xml",
        "views/menu.xml"
    ],
    "installable": True,
    "application": False
}