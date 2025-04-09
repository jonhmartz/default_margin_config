from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    utilidad_predeterminada = fields.Integer(
        string="Utilidad Aplicada (%)",
        default=lambda self: self.env['default.margin.config'].search([], limit=1).utilidad or 0
    )
