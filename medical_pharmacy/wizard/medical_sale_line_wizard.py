# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class MedicalSaleLineWizard(models.TransientModel):
    _name = 'medical.sale.line.wizard'
    _description = 'Temporary order line info for Sale2Rx workflow'

    def _compute_default_session(self, ):
        rx_obj = self.env['medical.prescription.order.line']
        if self.prescription_wizard_id:
            return self.prescription_wizard_id.prescription_id
        return rx_obj.browse(self._context.get('active_id'))
    
    def _compute_price_subtotal(self, ):
        self.price_subtotal = self.price_unit * self.product_uom_qty

    order_id = fields.Many2one(
        string='Order',
        comodel_name='medical.sale.wizard',
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
        'Quantity',
        digits_compute= dp.get_precision('Product UoM'),
        required=True,
    )
    price_unit = fields.Float(
        'Unit Price',
        digits_compute= dp.get_precision('Product Price'),
        required=True,
    )
    price_subtotal = fields.Float(
        digits_compute= dp.get_precision('Product Subtotal'),
        required=True,
        compute='_compute_price_subtotal',
    )

    @api.multi
    def _to_insert(self, ):
        ''' List of insert tuples for ORM methods '''
        return list(
            (0, 0, v) for v in self._to_vals_iter()
        )

    @api.multi
    def _to_vals_iter(self, ):
        ''' Generator of values dicts for ORM methods '''
        for sale_id in self:
            yield self._to_vals()

    @api.multi
    def _to_vals(self, ):
        ''' Return a values dictionary to create in real model '''
        self.ensure_one()
        return {
            'name': self.product_id.display_name,
            'sequence': self.sequence,
            'product_id': self.product_id.id,
            'product_uom': self.product_uom.id,
            'product_uom_qty': self.product_uom_qty,
            'price_unit': self.price_unit,
        }
