# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models, _
from openerp.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'

    dispense_uom_id = fields.Many2one(
        comodel_name='product.uom',
        string='Dispense UoM',
        help='Dispense Unit of Measure',
        required=True,
        related='medicament_id.uom_id',
    )
    dispensed_ids = fields.Many2many(
        string='Dispensings',
        comodel_name='procurement.order',
        compute='_compute_dispensings',
        readonly=True,
    )
    last_dispense_id = fields.Many2one(
        string='Last Dispense',
        comodel_name='procurement.order',
        store=True,
        compute='_compute_dispensings',
    )
    dispensed_qty = fields.Float(
        store=True,
        compute='_compute_dispensings',
        help='Amount already dispensed (using medicine dosage)',
    )
    pending_dispense_qty = fields.Float(
        store=True,
        compute='_compute_dispensings',
        help='Amount pending dispense (using medicine dosage)',
    )
    exception_dispense_qty = fields.Float(
        store=True,
        compute='_compute_dispensings',
        help='Qty of dispense exceptions (using medicine dosage)',
    )
    cancelled_dispense_qty = fields.Float(
        store=True,
        compute='_compute_dispensings',
        help='Dispense qty cancelled (using medicine dosage)',
    )
    active_dispense_qty = fields.Float(
        store=True,
        compute='_compute_can_dispense_and_qty',
        help='Total amount of dispenses that are active in some way',
    )
    can_dispense = fields.Boolean(
        store=True,
        compute='_compute_can_dispense_and_qty',
        help='Can this prescription be dispensed?',
    )
    can_dispense_qty = fields.Float(
        store=True,
        compute='_compute_can_dispense_and_qty',
        help='Amount that can be dispensed (using medicine dosage)',
    )

    @api.multi
    @api.depends(
        'dispense_uom_id',
        'sale_order_line_ids',
        'sale_order_line_ids.procurement_ids.product_uom',
        'sale_order_line_ids.procurement_ids.product_qty',
        'sale_order_line_ids.procurement_ids.state',
    )
    def _compute_dispensings(self):
        for record in self:

            dispense_ids = []
            dispense_qty = 0.0
            pending_qty = 0.0
            cancel_qty = 0.0
            except_qty = 0.0
            last_procurement_id = None

            order_line_ids = record.sale_order_line_ids.sorted(
                key=lambda r: r.order_id.date_order
            )
            for line_id in order_line_ids:
                procurement_ids = line_id.procurement_ids.sorted(
                    key=lambda r: r.date_planned
                )
                for proc_id in procurement_ids:

                    dispense_ids.append(proc_id.id)
                    last_procurement_id = proc_id

                    if proc_id.product_uom.id != record.dispense_uom_id.id:
                        _qty = self.env['product.uom']._compute_qty_obj(
                            proc_id.product_uom,
                            proc_id.product_qty,
                            record.dispense_uom_id,
                        )
                    else:
                        _qty = proc_id.product_qty

                    if proc_id.state == 'done':
                        dispense_qty += _qty
                    elif proc_id.state in ['confirmed', 'running']:
                        pending_qty += _qty
                    elif proc_id.state == 'cancel':
                        cancel_qty += _qty
                    else:
                        except_qty += _qty

            record.cancelled_dispense_qty = cancel_qty
            record.dispensed_qty = dispense_qty
            record.pending_dispense_qty = pending_qty
            record.exception_dispense_qty = except_qty

            record.dispensed_ids = self.env['procurement.order'].browse(
                set(dispense_ids)
            )
            record.last_dispense_id = last_procurement_id

    @api.multi
    @api.depends(
        'qty',
        'dispensed_qty',
        'exception_dispense_qty',
        'pending_dispense_qty',
    )
    def _compute_can_dispense_and_qty(self):
        for record in self:
            total = sum([record.dispensed_qty,
                         record.exception_dispense_qty,
                         record.pending_dispense_qty])

            record.active_dispense_qty = total
            record.can_dispense = record.qty > total
            record.can_dispense_qty = record.qty - total

    @api.multi
    @api.constrains('patient_id', 'sale_order_line_ids')
    def _check_patient(self):
        for record in self:
            _logger.info('LOGS')
            for sale_line_id in record.sale_order_line_ids:
                _logger.info(sale_line_id)
                _logger.info(sale_line_id.patient_id)
                _logger.info(record.patient_id)
                if sale_line_id.patient_id != record.patient_id:
                    raise ValidationError(_(
                        'Cannot change the patient on a prescription while it '
                        'is linked to active sale order(s).'
                    ))
