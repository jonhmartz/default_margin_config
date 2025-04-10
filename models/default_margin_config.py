from odoo import models, fields, api

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Configuración de Utilidad por Defecto'

    utilidad = fields.Integer(string='Utilidad por Defecto (%)', default=0)

    @api.model
    def get_singleton(self):
        config = self.search([], limit=1)
        if not config:
            config = self.create({})
        return config
