# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from openerp import api, fields, models


class MedicalPrescriptionOrderLine(models.Model):

    _inherit = 'medical.prescription.order.line'

    refill_qty_remain = fields.Float(
        string='Refill Remain',
        store=True,
        compute='_compute_can_dispense_and_qty',
        help='Amount of refills remaining in the prescription',
    )
    total_qty_remain = fields.Float(
        string='Qty Remaining',
        store=True,
        compute='_compute_can_dispense_and_qty',
        help='Total units remaining in the prescription',
    )
    total_allowed_qty = fields.Float(
        string='Qty Allowed',
        store=True,
        compute='_compute_can_dispense_and_qty',
        help='Total units allowed in the prescription, including refills',
    )
    dispense_remain_qty = fields.Float(
        string='Dispense Remaining Qty',
        compute='_compute_dispense_remain',
        help='Estimated number of units remaining from all finished dispenses',
    )
    dispense_remain_day = fields.Float(
        string='Dispense Remaining Days',
        compute='_compute_dispense_remain',
        help='Estimated days remaining based on all finished dispenses',
    )

    @api.multi
    def _compute_dispense_remain(self):
        day_uom_id = self.env.ref('medical_medication.product_uom_day')
        for record in self:

            if not record.duration_uom_id or record.duration <= 0:
                continue

            procurements = \
                record.dispensed_ids.filtered(
                    lambda r: r.state == 'done'
                ).sorted(
                    key=lambda r: r.date_planned
                )

            if not procurements:
                record.dispense_remain_qty, record.dispense_remain_day = 0, 0
                continue
            first_proc = procurements[0]

            date_first_dispense = fields.Datetime.from_string(
                first_proc.date_planned,
            )
            date_delta = datetime.now() - date_first_dispense
            days_passed = date_delta.days

            if day_uom_id != record.duration_uom_id:
                day_qty = self.env['product.uom']._compute_qty_obj(
                    record.duration_uom_id,
                    record.duration,
                    day_uom_id,
                )
            else:
                day_qty = record.duration

            # @TODO
            # What should happen if day_qty is 0?
            if not day_qty:
                continue

            # @TODO
            # record.qty can be set to 0, causing total_qty to be 0
            # and causing 0 division error for line 86
            total_qty = record.qty * (record.refill_qty_original + 1.0)
            daily_qty = total_qty / float(day_qty)
            estimated_use = days_passed * daily_qty

            total_dispensed = 0
            for proc in procurements:
                if record.dispense_uom_id != proc.product_uom:
                    dispense_qty = self.env['product.uom']._compute_qty_obj(
                        proc.product_uom,
                        proc.product_qty,
                        record.dispense_uom_id,
                    )
                else:
                    dispense_qty = proc.product_qty
                total_dispensed += dispense_qty

            remaining_units = total_dispensed - estimated_use
            remaining_units = 0 if remaining_units < 0 else remaining_units

            record.dispense_remain_qty = remaining_units
            record.dispense_remain_day = remaining_units / daily_qty

    @api.multi
    @api.depends(
        'qty',
        'dispensed_qty',
        'exception_dispense_qty',
        'pending_dispense_qty',
        'refill_qty_original',
        'dispense_remain_qty',
        'prescription_order_id.partner_id.company_id' +
        '.medical_prescription_refill_threshold',
    )
    def _compute_can_dispense_and_qty(self):
        """ Overload to provide refill logic """
        super(MedicalPrescriptionOrderLine, self).\
            _compute_can_dispense_and_qty()

        for record in self:

            total_qty = record.qty * (record.refill_qty_original + 1.0)
            record.total_allowed_qty = total_qty
            record.total_qty_remain = total_qty - record.active_dispense_qty

            if record.qty > 0 and record.active_dispense_qty > record.qty:
                refills_out = (record.active_dispense_qty / record.qty) - 1.0
                remain = record.refill_qty_original - refills_out
            else:
                remain = record.refill_qty_original
            record.refill_qty_remain = remain

            if not record.refill_qty_remain:
                continue
            if record.can_dispense_qty == record.qty:
                continue

            pending_and_unused = sum([
                record.exception_dispense_qty,
                record.pending_dispense_qty,
                record.dispense_remain_qty,
            ])
            if pending_and_unused >= record.qty:
                continue

            allowed = record.qty - pending_and_unused

            if allowed > record.total_qty_remain:
                allowed = record.total_qty_remain
            record.can_dispense = allowed > 0
            record.can_dispense_qty = allowed

            refill_threshold = record.prescription_order_id.partner_id \
                .company_id.medical_prescription_refill_threshold
            if refill_threshold:
                if pending_and_unused > refill_threshold * record.qty:
                    record.can_dispense = False
                    record.can_dispense_qty = 0
