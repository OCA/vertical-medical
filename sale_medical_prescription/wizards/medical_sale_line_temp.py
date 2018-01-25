# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class MedicalSaleLineTemp(models.TransientModel):
    _name = 'medical.sale.line.temp'
    _description = 'Temporary order line info for Sale2Rx workflow'

    order_id = fields.Many2one(
        string='Order',
        comodel_name='medical.sale.temp',
        readonly=True,
        required=True,
    )
    sequence = fields.Integer()
    product_id = fields.Many2one(
        string='Product',
        comodel_name='product.product',
    )
    product_uom = fields.Many2one(
        string='Unit of Measure',
        comodel_name='product.uom',
    )
    product_uom_qty = fields.Float(
        string='Quantity',
        digits_compute=dp.get_precision('Product UoM'),
        required=True,
        store=True,
    )
    price_unit = fields.Float(
        string='Unit Price',
        digits_compute=dp.get_precision('Product Price'),
        required=True,
        store=True,
    )
    price_subtotal = fields.Float(
        string='Subtotal',
        digits_compute=dp.get_precision('Account'),
        required=True,
        compute='_compute_all_amounts',
    )
    prescription_order_line_id = fields.Many2one(
        string='Prescription Line',
        comodel_name='medical.prescription.order.line',
    )

    @api.multi
    @api.depends('price_unit', 'product_uom_qty')
    def _compute_all_amounts(self):
        for record in self:
            record.price_subtotal = record.price_unit * record.product_uom_qty

    @api.multi
    def _to_insert(self):
        """ List of insert tuples for ORM methods """
        return list(
            (0, 0, v) for v in self._to_vals_iter()
        )

    @api.multi
    def _to_vals_iter(self):
        """ Generator of values dicts for ORM methods """
        for record in self:
            yield record._to_vals()

    @api.multi
    def _to_vals(self):
        """ Return a values dictionary to create in real model """
        self.ensure_one()
        name = '%s - %s' % (
            self.prescription_order_line_id.prescription_order_id.name,
            self.product_id.display_name,
        )
        return {
            'name': name,
            'sequence': self.sequence,
            'product_id': self.product_id.id,
            'product_uom': self.product_uom.id,
            'product_uom_qty': self.product_uom_qty,
            'prescription_order_line_id': self.prescription_order_line_id.id,
            'state': 'sale',
            'price_unit': self.price_unit,
        }
