from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    utilidad = fields.Float(string='Utilidad (%)', default=0.0)

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        config = self.env['default.margin.config'].search([], limit=1)
        res['utilidad'] = config.utilidad if config else 0.0
        return res