from odoo import models, fields

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Configuración de Utilidad por Defecto'

    utilidad = fields.Float(string='Utilidad por Defecto (%)', default=0.0)