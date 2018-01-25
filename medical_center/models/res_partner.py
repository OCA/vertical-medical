# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    type = fields.Selection(selection_add=[
        ('medical.center', 'Medical Center'),
    ])
