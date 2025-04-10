
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    utilidad = fields.Integer(string="Utilidad (%)", default=0)
