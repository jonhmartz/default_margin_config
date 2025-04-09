from odoo import models, fields

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Configuración de Margen por Defecto'

    utilidad = fields.Float(string='Utilidad por defecto (%)', required=True, default=30)
