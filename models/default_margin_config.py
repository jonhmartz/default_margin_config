from odoo import models, fields

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Configuración de Utilidad por Defecto'

    margin_percent = fields.Float(string='Utilidad por defecto (%)', default=0.0)