# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    medication_ids = fields.One2many(
        string='Medications',
        comodel_name='medical.patient.medication',
        inverse_name='patient_id',
        help='Medications that the patient is currently on',
    )
