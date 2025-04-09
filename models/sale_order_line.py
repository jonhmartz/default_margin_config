
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    utilidad = fields.Integer(string="Utilidad (%)", default=0)
    
    @api.onchange('product_id')
    def _onchange_product_id_set_margin(self):
        config = self.env['default.margin.config'].search([], limit=1)
        utilidad = config.utilidad if config else 0
        self.utilidad = utilidad
        if self.product_id:
            self.price_unit = self.product_id.standard_price * (1 + (utilidad / 100))

    @api.onchange('utilidad')
    def _onchange_utilidad_update_price(self):
        if self.product_id:
            self.price_unit = self.product_id.standard_price * (1 + (self.utilidad / 100))

    @api.onchange('price_unit', 'product_uom_qty')
    def _compute_amount(self):
        for line in self:
            line.price_subtotal = line.price_unit * line.product_uom_qty
