# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[
        ('medical.practitioner', 'Medical Practitioner'),
    ])
