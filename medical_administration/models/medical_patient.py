# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalPatient(models.Model):
    # FHIR Entity: Patient (http://hl7.org/fhir/patient.html)
    _name = 'medical.patient'
    _inherit = 'medical.abstract.partner'

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')],
    )   # FHIR Field: gender
    # https://www.hl7.org/fhir/valueset-administrative-gender.html)
    marital_status = fields.Selection(
        [
            ('s', 'Single'),
            ('m', 'Married'),
            ('w', 'Widowed'),
            ('d', 'Divorced'),
            ('l', 'Separated'),
        ]
    )   # FHIR Field: maritalStatus
    # https://www.hl7.org/fhir/valueset-marital-status.html
    birth_date = fields.Date(
        string='Birth date'
    )   # FHIR Field: birthDate
    deceased_date = fields.Date(
        string='Deceased date'
    )   # FHIR Field: deceasedDate
    is_deceased = fields.Boolean(
        compute='_compute_is_deceased'
    )   # FHIR Field: deceasedBoolean

    @api.depends('deceased_date')
    def _compute_is_deceased(self):
        for record in self:
            record.is_deceased = bool(record.deceased_date)

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code('medical.patient') or '/'
