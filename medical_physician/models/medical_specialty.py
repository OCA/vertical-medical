# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MedicalSpecialty(models.Model):
    _name = 'medical.specialty'
    _description = 'Medical Specialties'

    code = fields.Char(
        string='ID',
        help='Speciality Code',
        size=256,
    )
    name = fields.Char(
        string='Specialty',
        help='Name of the specialty',
        size=256,
        required=True,
        translate=True,
    )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
