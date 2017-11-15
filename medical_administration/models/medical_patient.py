# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, models, modules


class MedicalPatient(models.Model):
    # FHIR Entity: Patient (http://hl7.org/fhir/patient.html)
    _name = 'medical.patient'
    _inherit = 'medical.abstract.partner'

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code('medical.patient') or '/'
