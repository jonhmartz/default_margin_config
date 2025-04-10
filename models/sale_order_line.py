from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    utilidad = fields.Float(string="Utilidad (%)", default=lambda self: self._default_utilidad)

    @api.model
    def _default_utilidad(self):
        config = self.env['default.margin.config'].search([], limit=1)
        return config.default_margin if config else 0

    @api.onchange('utilidad', 'purchase_price')
    def _onchange_utilidad(self):
        for line in self:
            if line.purchase_price:
                margin_amount = (line.purchase_price * line.utilidad) / 100
                line.price_unit = line.purchase_price + margin_amount