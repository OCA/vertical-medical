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

    def _compute_default_session(self, ):
        return self.env['medical.prescription.order'].browse(
            self._context.get('active_id')
        )

    order_line = fields.One2many(
        string='Order Lines',
        comodel_name='medical.sale.line.wizard',
        inverse_name='order_id',
        required=True,
    )
    prescription_wizard_ids = fields.Many2many(
        comodel_name='medical.rx.sale.wizard',
        readonly=True,
    )
    patient_id = fields.Many2one(
        string='Patient',
        help='Patient (used for defaults when creating sale lines)',
        comodel_name='medical.patient',
    )
    prescription_order_id = fields.Many2one(
        string='Prescription',
        comodel_name='medical.prescription.order',
        default=_compute_default_session,
        required=True,
        readonly=True,
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
