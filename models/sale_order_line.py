from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    utilidad = fields.Integer(
        string="Utilidad (%)", 
        default=lambda self: self.env['default.margin.config'].get_singleton().utilidad
    )

