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

from openerp import fields, models, api


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'
    _order = 'priority desc, date_start_treatment, id'

    @api.one
    def _compute_dispensings_and_orders(self, ):
        ''' Get related dispensings and orders. Also sets dispense qty's '''

        dispense_ids, order_ids = [], []
        dispense_qty, pending_qty, cancel_qty, except_qty = 0.0, 0.0, 0.0, 0.0
        for line_id in self.sale_order_line_ids:

            order_ids.append(line_id.order_id)
            for proc_id in line_id.procurement_ids:

                dispense_ids.append(proc_id.id)

                if proc_id.product_uom.id != self.dispense_uom_id.id:
                    _qty = proc_id.product_uom._compute_qty_obj(
                        proc_id.product_qty, self.dispense_uom_id
                    )
                else:
                    _qty = self.dispense_uom_id

                if proc_id.state == 'done':
                    dispense_qty += _qty
                elif proc_id.state in ['confirmed', 'running']:
                    pending_qty += _qty
                elif proc_id.state == 'cancel':
                    cancel_qty += _qty
                else:
                    except_qty += _qty

        self.cancelled_dispense_qty = cancel_qty
        self.dispensed_qty = dispense_qty
        self.pending_dispense_qty = pending_qty
        self.exception_dispense_qty = except_qty

        self.order_ids = self.env['sale.order'].browse(set(order_ids))
        self.dispensed_ids = self.env['procurement.order'].browse(dispense_ids)

    @api.one
    def _compute_can_dispense_and_qty(self, ):
        '''
        Determine whether Rx can be dispensed based on current dispensings,
        and what qty
        '''

        total = sum(self.dispensed_qty, self.exception_dispense_qty,
                    self.pending_dispense_qty)

        if self.qty > total:
            self.can_dispense = True
            self.can_dispense_qty = self.qty - total
        else:
            self.can_dispense = False
            self.can_dispense_qty = self.qty - total

    sale_order_line_ids = fields.One2many(
        comodel_name='sale.order.line',
        inverse_name='prescription_order_line_id',
        readonly=True,
    )
    sale_order_ids = fields.Many2many(
        comodel_name='sale.order',
        compute='_compute_dispensings_and_orders',
        readonly=True,
    )
    dispensed_ids = fields.One2many(
        'procurement.order',
        compute='_compute_dispensings_and_orders',
        readonly=True,
    )
    dispensed_qty = fields.Float(
        default=0.0,
        readonly=True,
        compute='_compute_dispensings_and_orders',
        help='Amount already dispensed (using medicine dosage)',
    )
    pending_dispense_qty = fields.Float(
        default=0.0,
        readounly=True,
        compute='_compute_dispensings_and_orders',
        help='Amount pending dispense (using medicine dosage)',
    )
    exception_dispense_qty = fields.Float(
        default=0.0,
        readounly=True,
        compute='_compute_dispensings_and_orders',
        help='Qty of dispense exceptions (using medicine dosage)',
    )
    cancelled_dispense_qty = fields.Float(
        default=0.0,
        readounly=True,
        compute='_compute_dispensings_and_orders',
        help='Dispense qty cancelled (using medicine dosage)',
    )
    can_dispense = fields.Boolean(
        compute='_compute_can_dispense_and_qty',
        default=False,
        readonly=True,
        help='Can this prescription be dispensed?',
    )
    can_dispense_qty = fields.Float(
        compute='_compute_can_dispense_and_qty',
        default=0.0,
        help='Amount that can be dispensed (using medicine dosage)',
    )

    receive_method = fields.Selection([
        ('online', 'E-Prescription'),
        ('phone', 'Phoned In'),
        ('fax', 'Fax'),
        ('mail', 'Physical Mail'),
        ('transfer', 'Transferred In'),
    ],
        default='fax',
        string='Receipt Method',
        help='How the Rx was received',
    )
    verify_method = fields.Selection([
        ('none', 'Not Verified'),
        ('doctor_phone', 'Called Doctor'),
    ],
        default='none',
        help='Method of Rx verification',
    )
    receive_date = fields.Datetime(
        default=fields.Datetime.now,
        string='Receipt Date',
        help='When the Rx was received',
    )
