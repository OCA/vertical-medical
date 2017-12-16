# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalMedicamentComponent(models.Model):
    _name = 'medical.medicament.component'
    _description = 'Medical Medicament Component'

    medicament_ids = fields.Many2many(
        string='Related Medicaments',
        comodel_name='medical.medicament',
    )
    name = fields.Char(
        help='Component name',
        required=True,
    )
    is_active_ingredient = fields.Boolean(
        string='Active Ingredient?',
        help='Check this if the component is an active ingredient.',
    )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Component names must be unique.')
    ]
