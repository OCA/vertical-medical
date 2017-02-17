# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    safety_cap_yn = fields.Boolean(
        string='Use Safety Cap',
        help='Check this if the patient prefers a safety cap on their '
             'prescription dispensings.',
    )
    counseling_yn = fields.Boolean(
        string='Provide Counseling',
        help='Check this if the patient requires counseling on their '
             'prescription dispensings.'
    )
    allergies = fields.Char()
    existing_meds = fields.Char()
