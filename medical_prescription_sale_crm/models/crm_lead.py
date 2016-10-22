# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


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
        # readonly=True,
    )
    is_prescription = fields.Boolean(
        readonly=True,
        default=False,
        compute='_compute_prescription_order_and_patient_ids'
    )

    @api.multi
    def _compute_prescription_order_and_patient_ids(self, ):
        for rec_id in self:
            prescription_ids = self.env['medical.prescription.order']
            patient_ids = self.env['medical.patient']
            for line_id in rec_id.prescription_order_line_ids:
                if line_id.prescription_order_id not in prescription_ids:
                    prescription_ids += line_id.prescription_order_id
                if line_id.patient_id not in patient_ids:
                    patient_ids += line_id.patient_id
            rec_id.prescription_order_ids = prescription_ids
            rec_id.is_prescription = len(prescription_ids) > 0
            rec_id.patient_ids = patient_ids
