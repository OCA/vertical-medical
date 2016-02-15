# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MedicalPatientDisease(models.Model):
    _inherit = 'medical.patient.disease'
    prescription_order_line_ids = fields.One2many(
        string='Prescription Lines',
        comodel_name='medical.prescription.order.line',
        inverse_name='disease_id',
        help='Prescriptions related to this disease.',
    )
