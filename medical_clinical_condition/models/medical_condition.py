# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalCondition(models.Model):
    # FHIR Entity: Condition (https://www.hl7.org/fhir/condition.html)
    _name = 'medical.condition'
    _inherit = 'medical.abstract'
    _description = 'Conditions'

    patient_id = fields.Many2one(
        comodel_name='medical.patient',
        string='Subject',
        required=True,
    )   # FHIR Field: Subject
    category_code = fields.Selection([
        ('problem-list-item', 'Problem'),
        ('encounter-diagnosis', 'Diagnosis')
    ],  default='problem-list-item',
        required=True,
    )   # FHIR Field: category
    clinical_finding_id = fields.Many2one(
        comodel_name='medical.clinical.finding',
        required=True,
    )
    active = fields.Boolean(
        default=True,
    )

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code('medical.condition') or '/'
