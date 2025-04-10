
from odoo import models, fields

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Configuración de utilidad por defecto'

    utilidad = fields.Integer(string="Utilidad por Defecto (%)", default=0)
