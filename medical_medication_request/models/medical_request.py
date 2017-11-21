# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalRequest(models.AbstractModel):
    _inherit = 'medical.request'

    medication_request_id = fields.Many2one(
        string="Parent medication request",
        comodel_name="medical.medication.request",
    )   # FHIR Field: BasedOn
    medication_request_ids = fields.One2many(
        string="Medication requests",
        comodel_name="medical.medication.request",
        compute="_compute_medication_request_ids",
    )
    medication_request_count = fields.Integer(
        compute="_compute_medication_request_ids",
        string='# of Medication Requests',
        copy=False,
        default=0,
    )

    @api.multi
    def _compute_medication_request_ids(self):
        inverse_field_name = self._get_parent_field_name()
        for rec in self:
            medication_requests = self.env[
                'medical.medication.request'].search(
                [(inverse_field_name, '=', rec.id)])
            rec.medication_request_ids = [(6, 0, medication_requests.ids)]
            rec.medication_request_count = len(rec.medication_request_ids)

    @api.model
    def _get_request_models(self):
        res = super(MedicalRequest, self)._get_request_models()
        res.append('medical.medication.request')
        return res

    @api.constrains('medication_request_id')
    def _check_hierarchy_medication_request(self):
        for record in self:
            record._check_hierarchy_children({})
