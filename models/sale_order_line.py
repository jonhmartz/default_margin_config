from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    margin_percent = fields.Float(string='Utilidad (%)')
