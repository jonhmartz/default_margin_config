from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    utilidad = fields.Float(string="Utilidad (%)")
