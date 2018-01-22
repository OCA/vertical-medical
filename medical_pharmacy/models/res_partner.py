# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    type = fields.Selection(selection_add=[
        ('medical.pharmacy', 'Medical Pharmacy'),
        ('medical.pharmacist', 'Medical Pharmacist'),
    ])
