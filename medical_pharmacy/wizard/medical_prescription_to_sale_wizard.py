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

from openerp import models, api, fields, _
from collections import defaultdict


class MedicalPrescriptionToSaleWizard(models.TransientModel):
    _name = 'medical.prescription.to.sale.wizard'
    _description = 'Convert Medical Prescription(s) to Sale Order(s)'

    def _compute_default_session(self, ):
        return self.env['medical.prescription.order'].browse(
            self._context.get('active_id')
        )
    
    prescription_id = fields.Many2one(
        string='Prescription',
        comodel_name='medical.prescription.order',
        default=_compute_default_session,
        required=True,
        readonly=True,
    )
    split_orders = fields.Selection([
        ('partner', 'By Customer'),
        ('patient', 'By Patient'),
        ('all', 'By Rx Line'),
    ],
        help=_('How to split the new orders'),
    )
    order_date = fields.Datetime(
        help=_('Date for the new orders'),
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        help=_('Pharmacy to dispense orders from'),
        comodel_name='medical.pharmacy',
    )
    sale_wizard_ids = fields.Many2many(
        string='Orders',
        help=_('Orders to create when wizard is completed'),
        comodel_name='medical.sale.wizard',
        inverse_name='prescription_wizard_ids',
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        default='prescription_id.patient_id',
        readonly=True,
    )
    state = fields.Selection([
        ('start', 'Started'),
        ('partial', 'Partial'),
        ('done', 'Completed'),
        ('cancel', 'Cancelled'),
    ],
        readonly=True,
    )
    
    @api.multi
    def _create_sale_wizards(self, ):
        
        self.ensure_one()
        order_map = defaultdict(list)
        order_inserts = []
        
        for rx_line in self.prescription_id.prescription_order_line_ids:
            if self.split_orders == 'partner':
                raise NotImplementedError(_(
                    'Patient and Customers are currently identical concepts'
                ))
            elif self.split_orders == 'patient':
                order_map[rx_line.patient_id].append(rx_line)
            else:
                order_map[None].append(rx_line)

        for order in order_map.values():
            
            order_lines = list((0, 0, {
                'product_id': l.medical_medication_id.id,
                'product_uom_id': l.uom_id.id,
                'product_uom_qty': l.qty,
                'price_unit': l.list_price,
                'patient_id': l.patient_id.id,
                
            }) for l in self.prescription_id.prescription_order_line_ids)
            
            order_inserts.append((0, 0, {
                'prescription_wizard_id': self.id,
                'partner_id': self.patient_id.id,
                'partner_invoice_id': self.patient_id.id,
                'partner_shipping_id': self.patient_id.id,
                'prescription_order_id': self.prescription_id.id,
                'order_line': order_lines,
            }))
        
        self.write({
            'sale_wizard_ids': order_inserts,
            'state': 'start',
        })

    @api.one
    def _do_rx_sale_conversions(self, ):
        sale_obj = self.env['sale.order']
        sale_ids = None
        for sale_wizard_id in self.sale_wizard_ids:
            sale_id = sale_obj.create(sale_wizard_id._to_vals())
            try:
                sale_ids += sale_id
            except TypeError:
                sale_ids = sale_id
        return sale_ids
