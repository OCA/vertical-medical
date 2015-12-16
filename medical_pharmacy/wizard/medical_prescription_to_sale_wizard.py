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


class MedicalPrescriptionToSaleWizard(models.TransientModel):
    _name = 'medical.prescription.to.sale.wizard'
    _description = 'Convert Medical Prescription(s) to Sale Order(s)'

    def _compute_default_session(self, ):
        return self.env['medical.prescription.order'].browse(
            self._context.get('active_id')
        )
    
    prescription_id = fields.Many2one(
        comodel_name='medical.prescription.order',
        string='Prescription',
        default=_compute_default_session,
        required=True,
        readonly=True,
    )
    split_orders = fields.Selection([
        ('partner', 'By Customer'),
        ('patient', 'By Patient'),
        ('all', 'By Rx Line'),
    ],
        help='How to split the new orders',
    )
    order_date = fields.Datetime(
        help='Date for the new orders',
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        comodel_name='medical.pharmacy',
        help='Pharmacy to dispense orders from',
    )
    sale_wizard_ids = fields.Many2many(
        string='Orders',
        help='Orders to create when wizard is completed',
        comodel_name='medical.sale.wizard',
    )
    state_id = fields.Many2one(
        string='State',
        comodel_name='medical.prescription.order.state',
        related='prescription_id.state_id',
        select=True,
        readonly=True,
        copy=False,
    )
    # state = fields.Selection([
    #     ('start', 'Started'),
    #     ('partial', 'Partial'),
    #     ('done', 'Completed'),
    #     ('cancel', 'Cancelled'),
    # ],
    #     readonly=True,
    # )

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
