from odoo import models, fields

class DefaultMarginConfig(models.Model):
    _name = "default.margin.config"
    _description = "Configuración de Utilidad por Defecto"

    utilidad = fields.Integer("Utilidad por Defecto", required=True)