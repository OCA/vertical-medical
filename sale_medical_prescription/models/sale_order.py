# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    patient_ids = fields.Many2many(
        string='Patients',
        comodel_name='medical.patient',
        compute='_compute_patient_ids',
        readonly=True,
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        comodel_name='medical.pharmacy',
    )
    prescription_order_ids = fields.Many2many(
        string='Prescriptions',
        comodel_name='medical.prescription.order',
        compute='_compute_prescription_order_ids',
        readonly=True,
    )
    prescription_order_line_ids = fields.Many2many(
        string='Prescription Lines',
        comodel_name='medical.prescription.order.line',
        compute='_compute_prescription_order_ids',
        readonly=True,
    )

    @api.multi
    def _compute_patient_ids(self):
        for rec_id in self:
            patient_ids = []
            for line_id in rec_id.order_line:
                patient_ids.append(line_id.patient_id.id)
            rec_id.patient_ids = self.env['medical.patient'].browse(
                set(patient_ids)
            )

    @api.multi
    def _compute_prescription_order_ids(self):
        rx_mod = 'medical.prescription.order'
        for rec_id in self:
            prescription_ids = []
            prescription_line_ids = []
            for order_line_id in rec_id.order_line:
                if not order_line_id.prescription_order_line_id:
                    continue
                line_id = order_line_id.prescription_order_line_id
                prescription_line_ids.append(line_id.id)
                prescription_ids.append(line_id.prescription_order_id.id)
            rec_id.prescription_order_ids = self.env[rx_mod].browse(
                set(prescription_ids)
            )
            line_obj = self.env['%s.line' % rx_mod]
            rec_id.prescription_order_line_ids = line_obj.browse(
                set(prescription_line_ids)
            )
