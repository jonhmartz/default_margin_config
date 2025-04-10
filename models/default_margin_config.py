from odoo import models, fields, api

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Configuración de utilidad por defecto'

    margin_percent = fields.Integer(string='Utilidad por Defecto (%)', default=0)

    @api.model
    def get_margin_percent(self):
        config = self.search([], limit=1)
        return config.margin_percent if config else 0
