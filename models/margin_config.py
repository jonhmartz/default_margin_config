from odoo import models, fields

class MarginConfig(models.Model):
    _name = "default.margin.config"
    _description = "Configuración de utilidad por defecto"
    _rec_name = "utilidad"

    utilidad = fields.Integer(
        string="Utilidad por defecto (%)",
        required=True,
        default=30,
    )
