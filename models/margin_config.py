from odoo import models, fields

class MarginConfig(models.Model):
    _name = "default.margin.config"
    _description = "Configuración de utilidad por defecto"
    _rec_name = "id"

    porcentaje_utilidad = fields.Float(string="Utilidad por defecto (%)", default=0.0)