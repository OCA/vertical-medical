# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api
from datetime import datetime


import logging
_logger = logging.getLogger(__name__)


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'

    refill_qty_remain = fields.Float(
        string='Refill Remain',
        readonly=True,
        help='Amount of refills remaining in the prescription',
    )
    total_qty_remain = fields.Float(
        string='Qty Remaining',
        readonly=True,
        help='Total units remaining in the prescription',
    )
    total_allowed_qty = fields.Float(
        string='Qty Allowed',
        readonly=True,
        help='Total units allowed in the prescription, including refills',
    )
    last_dispense_remain_qty = fields.Float(
        string='Dispense Remaining Qty',
        compute=lambda s: s._compute_dispense_remain(),
        help='Estimated number of units remaining from last dispense',
    )
    last_dispense_remain_percent = fields.Float(
        string='Dispense Remaining Percent',
        compute=lambda s: s._compute_dispense_remain(),
        help='Estimated percentage remaining from last dispense',
    )
    last_dispense_remain_day = fields.Float(
        string='Dispense Remaining Days',
        compute=lambda s: s._compute_dispense_remain(),
        help='Estimated days remaining from last dispense',
    )

    @api.multi
    @api.depends('qty',
                 'refill_qty_original',
                 'active_dispense_qty',
                 )
    def _compute_qty_remain(self):
        for rec_id in self:
            _logger.debug('In dispense qty %s', rec_id)
            total_qty = rec_id.qty * (rec_id.refill_qty_original + 1.0)
            rec_id.total_allowed_qty = total_qty
            rec_id.total_qty_remain = total_qty - rec_id.active_dispense_qty
            if rec_id.qty and rec_id.total_qty_remain:
                remain = (rec_id.total_qty_remain / rec_id.qty) - 1.0
                rec_id.refill_qty_remain = remain

    @api.multi
    def _compute_dispense_remain(self):

        day_uom_id = self.env.ref('product.product_uom_day')
        for rec_id in self:

            procurement_ids = \
                rec_id.dispensed_ids.filtered(
                    lambda r: r.state == 'done'
                ).sorted(
                    key=lambda r: r.date_planned
                )

            if not len(procurement_ids):
                continue

            proc_id = procurement_ids[-1]

            if rec_id.dispense_uom_id != proc_id.product_uom:
                dispense_qty = proc_id.product_uom._compute_qty_obj(
                    proc_id.product_qty, rec_id.dispense_uom_id
                )
            else:
                dispense_qty = proc_id.product_qty

            if day_uom_id != rec_id.duration_uom_id:
                day_qty = rec_id.duration_uom_id._compute_qty_obj(
                    rec_id.duration, day_uom_id,
                )
            else:
                day_qty = rec_id.duration

            date_dispense = fields.Datetime.from_string(proc_id.date_planned)
            daily_qty = rec_id.total_allowed_qty / float(day_qty)
            days_dispensed = dispense_qty / daily_qty
            date_delta = datetime.now() - date_dispense
            days_remain = days_dispensed - date_delta.days

            rec_id.last_dispense_remain_day = days_remain
            rec_id.last_dispense_remain_qty = days_remain * daily_qty
            rec_id.last_dispense_remain_percent = 100.0 * (
                days_remain / days_dispensed
            )

    @api.multi
    @api.depends('qty',
                 'dispensed_qty',
                 'exception_dispense_qty',
                 'pending_dispense_qty',
                 )
    def _compute_can_dispense_and_qty(self):
        """ Overload to provide refill logic """
        super(MedicalPrescriptionOrderLine, self).\
            _compute_can_dispense_and_qty()
        for rec_id in self:
            _logger.debug('In dispense compute %s', rec_id)
            if not rec_id.refill_qty_remain:
                continue
            if rec_id.can_dispense_qty == rec_id.qty:
                continue
            pending = sum([rec_id.exception_dispense_qty,
                           rec_id.pending_dispense_qty])
            if pending >= rec_id.qty:
                continue
            allowed = rec_id.qty - pending
            if allowed > rec_id.total_qty_remain:
                allowed = rec_id.total_qty_remain
            rec_id.can_dispense = bool(allowed)
            rec_id.can_dispense_qty = allowed
