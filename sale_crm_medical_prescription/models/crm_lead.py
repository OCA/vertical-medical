# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    patient_ids = fields.Many2many(
        string='Patients',
        comodel_name='medical.patient',
        compute='_compute_prescription_order_and_patient_ids',
        readonly=True,
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        comodel_name='medical.pharmacy',
    )
    prescription_order_ids = fields.Many2many(
        string='Prescriptions',
        comodel_name='medical.prescription.order',
        compute='_compute_prescription_order_and_patient_ids',
        readonly=True,
    )
    prescription_order_line_ids = fields.Many2many(
        string='Prescription Lines',
        comodel_name='medical.prescription.order.line',
    )
    is_prescription = fields.Boolean(
        string='Prescription',
        readonly=True,
        default=False,
        compute='_compute_prescription_order_and_patient_ids',
    )

    @api.multi
    def _compute_prescription_order_and_patient_ids(self):
        prescription_ids = self.env['medical.prescription.order']
        patient_ids = self.env['medical.patient']

        for record in self:
            for line_id in record.prescription_order_line_ids:

                if line_id.prescription_order_id not in prescription_ids:
                    prescription_ids += line_id.prescription_order_id

                if line_id.patient_id not in patient_ids:
                    patient_ids += line_id.patient_id

            record.prescription_order_ids = prescription_ids
            record.is_prescription = len(prescription_ids) > 0
            record.patient_ids = patient_ids
