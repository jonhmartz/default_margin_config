from odoo import models, fields

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Configuración de utilidad por defecto'

    default_margin = fields.Integer(string="Utilidad por defecto (%)", default=0)