from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    weight_required = fields.Boolean()
