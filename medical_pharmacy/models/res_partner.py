# -*- coding: utf-8 -*-
# Copyright 2016-2018 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(
        selection_add=[
            ('medical.pharmacy', 'Medical Pharmacy'),
            ('medical.pharmacist', 'Medical Pharmacist'),
        ],
    )
