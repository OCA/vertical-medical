# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    disease_ids = fields.One2many(
        comodel_name='medical.patient.disease',
        inverse_name='patient_id',
        string='Diseases',
    )
    count_disease_ids = fields.Integer(
        compute='_compute_count_disease_ids',
        string='Diseases',
    )

    @api.multi
    def _compute_count_disease_ids(self):
        for rec_id in self:
            rec_id.count_disease_ids = len(rec_id.disease_ids)

    @api.multi
    def action_invalidate(self):
        for rec_id in self:
            super(MedicalPatient, rec_id).action_invalidate()
            rec_id.disease_ids.action_invalidate()

    @api.multi
    def action_revalidate(self):
        for rec_id in self:
            rec_id.active = True
            rec_id.partner_id.active = True
            disease_ids = self.env['medical.patient.disease'].search([
                ('patient_id', '=', self.id),
                ('active', '=', False),
            ])
            disease_ids.action_revalidate()
