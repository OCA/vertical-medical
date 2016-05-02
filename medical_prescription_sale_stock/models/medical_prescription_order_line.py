# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api, _
from openerp.exceptions import ValidationError


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'

    dispense_uom_id = fields.Many2one(
        comodel_name='product.uom',
        string='Dispense UoM',
        help='Dispense Unit of Measure',
    )
    dispensed_ids = fields.Many2many(
        string='Dispensings',
        comodel_name='procurement.order',
        compute='_compute_dispensings',
        store=True,
    )
    last_dispense_id = fields.Many2one(
        string='Last Dispense',
        comodel_name='procurement.order',
        compute='_compute_dispensings',
        store=True,
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
    can_dispense = fields.Boolean(
        compute='_compute_can_dispense_and_qty',
        store=True,
        help='Can this prescription be dispensed?',
    )
    can_dispense_qty = fields.Float(
        compute='_compute_can_dispense_and_qty',
        store=True,
        help='Amount that can be dispensed (using medicine dosage)',
    )
    dispense_uom_id = fields.Many2one(
        string='Dispense Units',
        comodel_name='product.uom',
        store=True,
        help='Dispense unit of measurement',
    )

    @api.multi
    @api.depends('dispense_uom_id',
                 'sale_order_line_ids',
                 'sale_order_line_ids.procurement_ids.product_uom',
                 'sale_order_line_ids.procurement_ids.product_qty',
                 'sale_order_line_ids.procurement_ids.state', )
    def _compute_dispensings(self, ):
        ''' Get related dispensings - Also sets dispense qtys '''

        for rec_id in self:

            dispense_ids = []
            dispense_qty = 0.0
            pending_qty = 0.0
            cancel_qty = 0.0
            except_qty = 0.0
            last_procurement_id = None

            order_line_ids = rec_id.sale_order_line_ids.sorted(
                key=lambda r: r.order_id.date_order
            )
            for line_id in order_line_ids:
                procurement_ids = line_id.procurement_ids.sorted(
                    key=lambda r: r.date_planned
                )
                for proc_id in procurement_ids:

                    dispense_ids.append(proc_id.id)
                    last_procurement_id = proc_id

                    if proc_id.product_uom.id != rec_id.dispense_uom_id.id:
                        _qty = proc_id.product_uom._compute_qty_obj(
                            proc_id.product_qty, rec_id.dispense_uom_id
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

            rec_id.cancelled_dispense_qty = cancel_qty
            rec_id.dispensed_qty = dispense_qty
            rec_id.pending_dispense_qty = pending_qty
            rec_id.exception_dispense_qty = except_qty
            rec_id.dispensed_ids = self.env['procurement.order'].browse(
                set(dispense_ids)
            )
            rec_id.last_dispense_id = last_procurement_id

    @api.multi
    @api.depends('qty',
                 'dispensed_qty',
                 'exception_dispense_qty',
                 'pending_dispense_qty')
    def _compute_can_dispense_and_qty(self, ):
        '''
        Determine whether Rx can be dispensed based on current dispensings,
        and what qty
        '''

        for rec_id in self:
            written_qty = rec_id.qty
            total = sum([rec_id.dispensed_qty,
                         rec_id.exception_dispense_qty,
                         rec_id.pending_dispense_qty])

            rec_id.can_dispense = rec_id.qty > total
            rec_id.can_dispense_qty = rec_id.qty - total

    @api.multi
    @api.constrains('patient_id', 'sale_order_line_ids')
    def _check_patient(self, ):
        for rec_id in self:
            for sale_line_id in rec_id.sale_order_line_ids:
                if sale_line_id.patient_id != rec_id.patient_id:
                    raise ValidationError(_(
                        'Cannot change the patient on a prescription while it '
                        'is linked to active sale order(s)'
                    ))
