# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import _, api, fields, models
from openerp.exceptions import ValidationError


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    dispense_qty = fields.Float(
        default=0.0,
        readonly=True,
        store=True,
        compute='_compute_dispense_qty',
    )

    @api.multi
    @api.depends('product_uom', 'prescription_order_line_id.dispense_uom_id')
    def _compute_dispense_qty(self):
        for record in self:
            rx_line = record.prescription_order_line_id
            if not rx_line:
                return
            if record.product_uom == rx_line.dispense_uom_id:
                record.dispense_qty = record.product_uom_qty
            else:
                record.dispense_qty = self.env['product.uom']._compute_qty_obj(
                    record.product_uom,
                    record.product_uom_qty,
                    rx_line.dispense_uom_id,
                )

    @api.multi
    @api.constrains('product_id', 'prescription_order_line_id')
    def _check_product(self):
        if self.env.context.get('__rx_force__'):
            return True
        for record in self:
            if not record.prescription_order_line_id:
                continue
            rx_line = record.prescription_order_line_id
            if rx_line.medicament_id.product_id != record.product_id:
                if not rx_line.is_substitutable:
                    raise ValidationError(_(
                        'Products must be same on Order and Rx lines. '
                        'Got %s on order line %s, expected %s from %r'
                    ) % (
                        record.product_id.name, record.name,
                        rx_line.medicament_id.product_id.name, rx_line,
                    ))
                else:
                    pass

    @api.multi
    @api.constrains('dispense_qty', 'prescription_order_line_id', 'state')
    def _check_can_dispense(self):
        if self.env.context.get('__rx_force__'):
            return True
        for record in self:
            conditions = [
                record.product_id.is_medicament,
                record.prescription_order_line_id,
            ]
            if not all(conditions):
                continue
            rx_line = record.prescription_order_line_id
            if not rx_line.can_dispense:
                raise ValidationError(_(
                    'Cannot dispense %s because there are related, '
                    'pending order(s). \n'
                    'Currently %.2f processed %.2f pending %.2f exception'
                ) % (
                    record.dispense_qty,
                    rx_line.dispensed_qty,
                    rx_line.pending_dispense_qty,
                    rx_line.exception_dispense_qty,
                ))
            if record.dispense_qty > rx_line.can_dispense_qty:
                raise ValidationError(_(
                    'Cannot dispense - %s goes over Rx qty by %d'
                ) % (
                    record.name,
                    record.dispense_qty - rx_line.can_dispense_qty
                ))

    @api.multi
    def _prepare_order_line_procurement(self, group_id=False):
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_order_line_procurement(
            group_id=group_id
        )
        if self.product_id.is_medicament:
            medicament = self.env['medical.medicament'].get_by_product(
                self.product_id,
            )
            warehouse = self.order_id.warehouse_id
            if medicament.is_prescription:
                res['route_ids'] = [
                    (6, 0, [warehouse.prescription_route_id.id])
                ]
            else:
                res['route_ids'] = [
                    (6, 0, [warehouse.otc_route_id.id])
                ]
        return res
