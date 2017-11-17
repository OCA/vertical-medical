# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalRequest(models.AbstractModel):
    _inherit = 'medical.request'

    careplan_id = fields.Many2one(
        string="Parent Careplan",
        comodel_name="medical.careplan",
    )   # FHIR Field: BasedOn
    careplan_ids = fields.One2many(
        string="Associated Care Plans",
        comodel_name="medical.careplan",
        compute='_compute_careplan_ids',
    )
    careplan_count = fields.Integer(
        compute="_compute_careplan_ids",
        string='# of Care Plans',
        copy=False,
        default=0,
    )

    @api.multi
    def _compute_careplan_ids(self):
        inverse_field_name = self._get_parent_field_name()
        for rec in self:
            careplans = self.env['medical.careplan'].search(
                [(inverse_field_name, '=', rec.id)])
            rec.careplan_ids = [(6, 0, careplans.ids)]
            rec.careplan_count = len(rec.careplan_ids)

    @api.model
    def _get_request_models(self):
        res = super(MedicalRequest, self)._get_request_models()
        res.append('medical.careplan')
        return res

    @api.constrains('careplan_id')
    def _check_hierarchy_careplan(self):
        for record in self:
            record._check_hierarchy_children({})
