from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    weight = fields.Float(tracking=True)
