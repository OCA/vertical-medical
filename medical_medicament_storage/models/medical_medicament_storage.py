# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalMedicamentStorage(models.Model):
    _name = 'medical.medicament.storage'
    _description = 'Medical Medicament - Storage Instructions'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Each name/code must be unique.'),
    ]

    name = fields.Char(
        string='Code',
        help='Short code for this set of storage instructions',
        required=True,
    )
    instructions = fields.Text(
        required=True,
    )
