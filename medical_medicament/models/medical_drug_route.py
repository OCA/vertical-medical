# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalDrugRoute(models.Model):
    _name = 'medical.drug.route'
    _description = 'Medical Drug Route'

    name = fields.Char(
        required=True,
        translate=True,
    )
    code = fields.Char(
        required=True,
    )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Drug route name must be unique!'),
        ('code_uniq', 'UNIQUE(code)', 'Drug route code must be unique!')
    ]
