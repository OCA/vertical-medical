# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalDrugForm(models.Model):
    _name = 'medical.drug.form'
    _description = 'Medical Drug Form'

    name = fields.Char(
        required=True,
        translate=True,
    )
    code = fields.Char(
        required=True,
    )

    _sql_constraints = [
        ('code_uniq', 'UNIQUE(code)', 'Code should be unique!'),
    ]
