# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class MedicalPatientDisease(models.Model):
    _inherit = 'medical.patient.disease'
    prescription_order_line_ids = fields.One2many(
        string='Prescription Lines',
        comodel_name='medical.prescription.order.line',
        inverse_name='disease_id',
        help='Prescriptions related to this disease.',
    )
