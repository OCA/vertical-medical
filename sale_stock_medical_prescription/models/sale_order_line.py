# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dispense_qty = fields.Float(
        default=0.0,
        readonly=True,
        store=True,
        compute='_compute_dispense_qty',
    )

    @api.multi
    @api.depends('product_uom',
                 'prescription_order_line_id.dispense_uom_id',
                 )
    def _compute_dispense_qty(self):
        for rec_id in self:
            rx_line = rec_id.prescription_order_line_id
            if not rx_line:
                return
            if rec_id.product_uom == rx_line.dispense_uom_id:
                rec_id.dispense_qty = rec_id.product_uom_qty
            else:
                rec_id.dispense_qty = rec_id.product_uom._compute_quantity(
                    rec_id.product_uom_qty,
                    rx_line.dispense_uom_id,
                )

    @api.multi
    @api.constrains('product_id', 'prescription_order_line_id')
    def _check_product(self):
        if self.env.context.get('__rx_force__'):
            return True
        for rec_id in self:
            if not rec_id.prescription_order_line_id:
                continue
            rx_line = rec_id.prescription_order_line_id
            if rx_line.medicament_id.product_id != rec_id.product_id:
                if not rx_line.is_substitutable:
                    raise ValidationError(_(
                        'Products must be same on Order and Rx lines. '
                        'Got %s on order line %s, expected %s from %r'
                    ) % (
                        rec_id.product_id.name, rec_id.name,
                        rx_line.medicament_id.product_id.name, rx_line,
                    ))
                else:
                    # @TODO: implement determination for what drugs can be
                    #        substituted
                    pass

    @api.multi
    @api.constrains('patient_id', 'prescription_order_line_id')
    def _check_patient(self):
        if self.env.context.get('__rx_force__'):
            return True
        for rec_id in self:
            if not rec_id.prescription_order_line_id:
                continue
            rx_line = rec_id.prescription_order_line_id
            if rec_id.patient_id != rx_line.patient_id:
                raise ValidationError(_(
                    'Patients must be same on Order and Rx lines. '
                    'Got %s on order line %d, expected %s from rx line %d'
                ) % (
                    rec_id.patient_id.name, rec_id.id,
                    rx_line.patient_id.name, rx_line.id,
                ))

    @api.multi
    @api.constrains('dispense_qty', 'prescription_order_line_id', 'state')
    def _check_can_dispense(self):
        if self.env.context.get('__rx_force__'):
            return True
        for rec_id in self:
            conditions = [
                rec_id.product_id.is_medicament,
                rec_id.prescription_order_line_id,
            ]
            if not all(conditions):
                continue
            rx_line = rec_id.prescription_order_line_id
            if not rx_line.can_dispense:
                raise ValidationError(_(
                    'Cannot dispense %s because there are related, '
                    'pending order(s). \n'
                    'Currently %.2f processed %.2f pending %.2f exception'
                ) % (
                    rec_id.dispense_qty,
                    rx_line.dispensed_qty,
                    rx_line.pending_dispense_qty,
                    rx_line.exception_dispense_qty,
                ))
            if rec_id.dispense_qty > rx_line.can_dispense_qty:
                raise ValidationError(_(
                    'Cannot dispense - %s goes over Rx qty by %d'
                ) % (
                    rec_id.name,
                    rec_id.dispense_qty - rx_line.can_dispense_qty
                ))

    @api.multi
    def _prepare_order_line_procurement(self, group_id=False):
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_order_line_procurement(
            group_id=group_id
        )
        if self.product_id.is_medicament:
            medicament_id = self.env['medical.medicament'].get_by_product(
                self.product_id,
            )
            warehouse_id = self.order_id.warehouse_id
            if medicament_id.is_prescription:
                res['route_ids'] = [
                    (6, 0, [warehouse_id.prescription_route_id.id])
                ]
            else:
                res['route_ids'] = [
                    (6, 0, [warehouse_id.otc_route_id.id])
                ]
        return res
