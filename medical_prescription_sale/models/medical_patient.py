# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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
    # @TODO: Get rid of these in favor of relations. Quick fix for website
    allergies = fields.Char()
    existing_meds = fields.Char()
