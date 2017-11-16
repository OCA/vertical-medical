# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalRequest(models.AbstractModel):
    _inherit = 'medical.request'

    procedure_request_id = fields.Many2one(
        string="Parent Procedure Request",
        comodel_name="medical.procedure.request",
    )   # FHIR Field: BasedOn
    procedure_request_ids = fields.One2many(
        string="Associated Procedure Requests",
        comodel_name="medical.procedure.request",
        compute="_compute_procedure_request_ids",
    )
    procedure_request_count = fields.Integer(
        compute="_compute_procedure_request_ids",
        string='# of Procedure Requests',
        copy=False,
        default=0,
    )

    @api.multi
    def _compute_procedure_request_ids(self):
        inverse_field_name = self._get_parent_field_name()
        for rec in self:
            procedure_requests = self.env['medical.procedure.request'].search(
                [(inverse_field_name, '=', rec.id)])
            rec.procedure_request_ids = [(6, 0, procedure_requests.ids)]
            rec.procedure_request_count = len(rec.procedure_request_ids)

    @api.model
    def _get_request_models(self):
        res = super(MedicalRequest, self)._get_request_models()
        res.append('medical.procedure.request')
        return res

    @api.constrains('procedure_request_id')
    def _check_hierarchy_procedure_request(self):
        for record in self:
            record._check_hierarchy_children({})
