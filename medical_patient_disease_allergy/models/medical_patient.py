# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    disease_ids = fields.One2many(
        string='Diseases',
        comodel_name='medical.patient.disease',
        inverse_name='patient_id',
        domain=[('is_allergy', '=', False)],
    )
    allergy_ids = fields.One2many(
        string='Allergies',
        comodel_name='medical.patient.disease',
        inverse_name='patient_id',
        domain=[('is_allergy', '=', True)],
    )
    count_allergy_ids = fields.Integer(
        string='Allergies',
        compute='_compute_count_allergy_ids',
    )

    @api.multi
    def action_invalidate(self, ):
        for rec_id in self:
            super(MedicalPatient, rec_id).action_invalidate()
            for disease_id in rec_id.allergy_ids:
                disease_id.action_invalidate()

    @api.multi
    def _compute_count_allergy_ids(self, ):
        for rec_id in self:
            rec_id.count_allergy_ids = len(rec_id.allergy_ids)
