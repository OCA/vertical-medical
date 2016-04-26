# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MedicalMedicamentNdc(models.Model):
    _name = 'medical.medicament.ndc'
    _description = 'Medical Medicament NDC'

    name = fields.Char(
        string='NDC',
        help='National Drug Code',
    )
    medicament_id = fields.Many2one(
        string='Medicament',
        comodel_name='medical.medicament',
        required=True,
    )
