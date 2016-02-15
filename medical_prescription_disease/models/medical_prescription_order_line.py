# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MedicalPrescriptionOrderLine(models.Model):
    _inherit= 'medical.prescription.order.line'
    disease_id = fields.Many2one(
        string='Disease',
        comodel_name='medical.patient.disease',
        required=True,
        domain=lambda s: [('pathology_id', '=', s.pathology_id.id),
                          ('patient_id', '=', s.patient_id.id), ],
        help='Disease diagnosis related to prescription.',
    )
