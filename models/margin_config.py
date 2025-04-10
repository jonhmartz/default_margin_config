from odoo import models, fields, api

class DefaultMarginConfig(models.Model):
    _name = 'default.margin.config'
    _description = 'Configuración de Margen'

    utilidad = fields.Float(string="Utilidad por Defecto (%)", default=0)

    @api.model
    def get_singleton(self):
        config = self.search([], limit=1)
        if not config:
            config = self.create({'utilidad': 0})
        return config