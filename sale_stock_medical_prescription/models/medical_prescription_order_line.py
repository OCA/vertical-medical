# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, fields, models


class MedicalPrescriptionOrderLine(models.Model):

    _inherit = 'medical.prescription.order.line'

    dispense_uom_id = fields.Many2one(
        comodel_name='product.uom',
        string='Dispense UoM',
        help='Dispense Unit of Measure',
        required=True,
        default=lambda s: s._default_dispense_uom_id(),
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

    @api.model
    def _default_dispense_uom_id(self):
        return self.env['product.uom'].browse(
            self.env['product.template']._get_uom_id()
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
            last_procurement = None

            order_lines = record.sale_order_line_ids.sorted(
                key=lambda r: r.order_id.date_order
            )
            for order_line in order_lines:
                procurements = order_line.procurement_ids.sorted(
                    key=lambda r: r.date_planned
                )
                for procurement in procurements:

                    dispense_ids.append(procurement.id)
                    last_procurement = procurement

                    if procurement.product_uom.id != record.dispense_uom_id.id:
                        _qty = self.env['product.uom']._compute_qty_obj(
                            procurement.product_uom,
                            procurement.product_qty,
                            record.dispense_uom_id,
                        )
                    else:
                        _qty = procurement.product_qty

                    if procurement.state == 'done':
                        dispense_qty += _qty
                    elif procurement.state in ['confirmed', 'running']:
                        pending_qty += _qty
                    elif procurement.state == 'cancel':
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
            record.last_dispense_id = last_procurement

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
