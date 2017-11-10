# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[
        ('medical.insurance.company', 'Insurance'),
    ])
