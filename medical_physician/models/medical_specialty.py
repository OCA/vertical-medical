# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class MedicalSpecialty(models.Model):
    _name = 'medical.specialty'
    _description = 'Medical Specialties'

    code = fields.Char(
        string='ID',
        help='Speciality Code',
    )
    name = fields.Char(
        string='Specialty',
        help='Name of the specialty',
        required=True,
        translate=True,
    )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
