# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    type = fields.Selection(selection_add=[
        ('medical.practitioner', 'Insurance'),
    ])

