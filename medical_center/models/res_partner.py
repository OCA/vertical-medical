# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    type = fields.Selection(selection_add=[
        ('medical.center', 'Medical Center'),
    ])
