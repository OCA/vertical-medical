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


class MedicalSaleWizard(models.TransientModel):
    _name = 'medical.sale.wizard'
    _inherit = 'sale.order'
    _description = 'Temporary order info for Sale2Rx workflow'

    order_line = fields.One2many(
        'medical.sale.line.wizard',
        required=True,
    )

    @api.multi
    def _to_insert(self, ):
        ''' List of insert tuples for ORM methods '''
        return list(
            (6, 0, v) for v in self._to_vals_iter()
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
            'address_allotment_id': self.address_allotment_id.id,
            'salesman_id': self.salesman_id.id,
            'sequence': self.sequence,
            'company_id': self.company_id.id,
            'delay': self.delay,
            'discount': self.discount,
            'partner_id': self.partner_id.id,
            'partner_invoice_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'pharmacy_id': self.pharmacy_id.id,
            'order_line': sale_id.order_line._to_insert(),
        }

class MedicalSaleLineWizard(models.TransientModel):
    _name = 'medical.sale.line.wizard'
    _inherit = 'sale.order.line'
    _description = 'Temporary order line info for Sale2Rx workflow'
    
    order_id = fields.Many2one(
        'medical.sale.wizard',
        readonly=True,
        required=True,
    )
    product_id = fields.Many2one(
        string='Medication',
        comodel_name='medical.patient.medication',
        required=True,
    )

    @api.multi
    def _to_insert(self, ):
        ''' List of insert tuples for ORM methods '''
        return list(
            (6, 0, v) for v in self._to_vals_iter()
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
            'delay': self.delay,
            'product_id': self.product_id.product_id.id,
            'product_uom': self.product_uom.id,
            'product_uom_qty': self.product_uom_qty,
            'price_unit': self.price_unit,
            'price_reduce': self.price_reduce,
            'tax_id': self.tax_id,
            'discount': self.discount,
        }
