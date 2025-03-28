from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    weight_required = fields.Boolean(
        string="Weight Required in POS",
        related="company_id.weight_required",
        readonly=False,
        default=True,
        help="Check if you want to require the"
        " customer's weight according to the age warning",
    )
