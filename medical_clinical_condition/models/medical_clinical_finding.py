# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalClinicalFinding(models.Model):
    # FHIR Entity: Condition Code
    # (http://hl7.org/fhir/valueset-condition-code.html)
    _name = 'medical.clinical.finding'
    _inherit = 'medical.abstract'
    _description = 'Condition/Problem/Diagnosis codes'

    name = fields.Char(
        required=True,
    )
    description = fields.Char()
    sct_code_id = fields.Many2one(
        comodel_name='medical.sct.concept',
        domain=[('is_clinical_finding', '=', True)],
    )

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.clinical.finding') or '/'
