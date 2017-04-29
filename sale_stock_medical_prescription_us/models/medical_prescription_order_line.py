# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models, api
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)


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
        for rec_id in self:
            if not rec_id.duration_uom_id or rec_id.duration <= 0:
                continue

            procurement_ids = \
                rec_id.dispensed_ids.filtered(
                    lambda r: r.state == 'done'
                ).sorted(
                    key=lambda r: r.date_planned
                )

            if not procurement_ids:
                rec_id.dispense_remain_qty, rec_id.dispense_remain_day = 0, 0
                continue

            first_proc = procurement_ids[0]
            date_first_dispense = fields.Datetime.from_string(
                first_proc.date_planned,
            )
            date_delta = datetime.now() - date_first_dispense
            days_passed = date_delta.days

            if day_uom_id != rec_id.duration_uom_id:
                day_qty = self.env['product.uom']._compute_qty_obj(
                    rec_id.duration_uom_id, rec_id.duration, day_uom_id,
                )
            else:
                day_qty = rec_id.duration
            total_qty = rec_id.qty * (rec_id.refill_qty_original + 1.0)
            daily_qty = total_qty / float(day_qty)
            estimated_use = days_passed * daily_qty

            total_dispensed = 0
            for proc_id in procurement_ids:
                if rec_id.dispense_uom_id != proc_id.product_uom:
                    dispense_qty = self.env['product.uom']._compute_qty_obj(
                        proc_id.product_uom,
                        proc_id.product_qty,
                        rec_id.dispense_uom_id,
                    )
                else:
                    dispense_qty = proc_id.product_qty
                total_dispensed += dispense_qty

            remaining_units = total_dispensed - estimated_use
            remaining_units = 0 if remaining_units < 0 else remaining_units
            rec_id.dispense_remain_qty = remaining_units
            rec_id.dispense_remain_day = remaining_units / daily_qty

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
        for rec_id in self:

            total_qty = rec_id.qty * (rec_id.refill_qty_original + 1.0)
            rec_id.total_allowed_qty = total_qty
            rec_id.total_qty_remain = total_qty - rec_id.active_dispense_qty
            if rec_id.qty > 0 and rec_id.active_dispense_qty > rec_id.qty:
                refills_out = (rec_id.active_dispense_qty / rec_id.qty) - 1.0
                remain = rec_id.refill_qty_original - refills_out
            else:
                remain = rec_id.refill_qty_original
            rec_id.refill_qty_remain = remain

            if not rec_id.refill_qty_remain:
                continue
            if rec_id.can_dispense_qty == rec_id.qty:
                continue

            pending_and_unused = sum([
                rec_id.exception_dispense_qty,
                rec_id.pending_dispense_qty,
                rec_id.dispense_remain_qty,
            ])
            if pending_and_unused >= rec_id.qty:
                continue

            allowed = rec_id.qty - pending_and_unused
            if allowed > rec_id.total_qty_remain:
                allowed = rec_id.total_qty_remain
            rec_id.can_dispense = allowed > 0
            rec_id.can_dispense_qty = allowed

            refill_threshold = rec_id.prescription_order_id.partner_id \
                .company_id.medical_prescription_refill_threshold
            if refill_threshold:
                if pending_and_unused > refill_threshold * rec_id.qty:
                    rec_id.can_dispense = False
                    rec_id.can_dispense_qty = 0
