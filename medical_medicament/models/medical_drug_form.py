# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


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
        ('name_uniq', 'UNIQUE(name)', 'Drug form name must be unique!'),
        ('code_uniq', 'UNIQUE(code)', 'Code should be unique!'),
    ]
