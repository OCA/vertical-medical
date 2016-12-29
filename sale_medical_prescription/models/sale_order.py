# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


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
        for record in self:
            patient_ids = []
            for line_id in record.order_line:
                patient_ids.append(line_id.patient_id.id)
            record.patient_ids = self.env['medical.patient'].browse(
                set(patient_ids)
            )

    @api.multi
    def _compute_prescription_order_ids(self):
        rx_model = self.env['medical.prescription.order']
        rx_line_model = self.env['medical.prescription.order.line']

        for record in self:
            rx_lines = rx_line_model.browse()
            rx_orders = rx_model.browse()

            for order_line in record.order_line:
                if not order_line.prescription_order_line_id:
                    continue

                related_rx_line = order_line.prescription_order_line_id
                related_rx_order = related_rx_line.prescription_order_id

                if related_rx_line not in rx_lines:
                    rx_lines += related_rx_line

                if related_rx_order not in rx_orders:
                    rx_orders += related_rx_order

            record.prescription_order_ids = rx_orders
            record.prescription_order_line_ids = rx_lines
