# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        related='prescription_order_line_id.patient_id',
    )
    prescription_order_line_id = fields.Many2one(
        string='Prescription Line',
        comodel_name='medical.prescription.order.line',
    )
    medication_id = fields.Many2one(
        string='Medication',
        comodel_name='medical.patient.medication',
        related='prescription_order_line_id.medical_medication_id',
    )
    dispense_qty = fields.Float(
        default=0.0,
        readonly=True,
        compute='_compute_dispense_qty',
    )
