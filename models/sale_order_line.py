from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    utilidad = fields.Float(string='Utilidad (%)', default=0.0)

    @api.model
    def create(self, vals):
        if 'utilidad' not in vals:
            config = self.env['default.margin.config'].search([], limit=1)
            vals['utilidad'] = config.utilidad if config else 0.0
        return super().create(vals)
