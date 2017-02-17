# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models


class MedicalMedicamentNdc(models.Model):
    _name = 'medical.medicament.ndc'
    _description = 'Medical Medicament NDC'

    name = fields.Char(
        string='NDC',
        help='National Drug Code',
    )
    manufacturer_id = fields.Many2one(
        string='Manufacturer',
        comodel_name='medical.manufacturer',
    )
    medicament_id = fields.Many2one(
        string='Medicament',
        comodel_name='medical.medicament',
        required=True,
    )
