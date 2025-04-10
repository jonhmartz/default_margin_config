from odoo import models, fields

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Default Margin Config'
    _rec_name = 'default_margin'

    default_margin = fields.Float(string='Utilidad por defecto (%)', default=0.0)
