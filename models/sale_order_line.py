from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    utilidad_linea = fields.Float(string="Utilidad (%)")
    importe_utilidad = fields.Monetary(
        string="Importe con Utilidad",
        currency_field='currency_id',
        compute="_compute_importe_utilidad",
        store=True
    )

    @api.depends('product_uom_qty', 'price_unit')
    def _compute_importe_utilidad(self):
        for line in self:
            line.importe_utilidad = line.product_uom_qty * line.price_unit

    @api.onchange('product_id', 'product_uom_qty', 'order_id', 'utilidad_linea')
    def _onchange_precio_por_utilidad(self):
        for line in self:
            if not line.product_id or not line.order_id:
                return

            costo = line.product_id.standard_price
            utilidad = line.utilidad_linea or line.order_id.utilidad_predeterminada or 0

            if utilidad < 100:
                try:
                    line.price_unit = round(costo / (1 - utilidad / 100), 2)
                except ZeroDivisionError:
                    line.price_unit = 0
