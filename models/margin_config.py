from odoo import models, fields

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Default Margin Configuration'

    margin_percent = fields.Float(string='Utilidad por Defecto', default=0.0)
