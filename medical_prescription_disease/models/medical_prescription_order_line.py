# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'
    disease_id = fields.Many2one(
        string='Disease',
        comodel_name='medical.patient.disease',
        help='Disease diagnosis related to prescription.',
    )

    @api.multi
    @api.onchange('patient_id')
    def _onchange_patient_id(self, ):
        self.ensure_one()
        return {
            'domain': {
                'disease_id': [('patient_id', '=', self.patient_id.id)],
                'prescription_order_id': [
                    ('patient_id', '=', self.patient_id.id)
                ],
            }
        }

    @api.multi
    @api.onchange('disease_id')
    def _onchange_disease_id(self, ):
        for rec_id in self:
            rec_id.patient_id = rec_id.disease_id.patient_id.id
