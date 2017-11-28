# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo import models, fields


class MedicalSpecialty(models.Model):
    _name = 'medical.specialty'
    _description = 'Medical Specialty'
    _sql_constraints = [
        ('code_uniq', 'UNIQUE(code)', 'Code must be unique!'),
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]

    code = fields.Char(
        string='Code',
        help='Speciality code',
        size=256,
        required=True,
    )
    name = fields.Char(
        string='Name',
        help='Name of the specialty',
        size=256,
        required=True,
    )
