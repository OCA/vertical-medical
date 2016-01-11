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

from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp
import logging


_logger = logging.getLogger(__name__)


class MedicalSaleWizard(models.TransientModel):
    _name = 'medical.sale.wizard'
    _description = 'Temporary order info for Sale2Rx workflow'

    def _compute_default_session(self, ):
        return self.env['medical.sale.wizard'].browse(
            self._context.get('active_id')
        )
    
    @api.one
    def _compute_line_cnt(self, ):
        self.line_cnt = len(self.order_line)

    @api.one
    def _compute_all_amounts(self, ):
        #curr = self.pricelist_id.currency_id
        untaxed = 0.0
        taxes = 0.0
        for line in self.order_line:
            untaxed += line.price_subtotal
            #taxes += line.amount_tax
        self.write({
            'amount_untaxed': untaxed,
        })

    order_line = fields.One2many(
        string='Order Lines',
        comodel_name='medical.sale.line.wizard',
        inverse_name='order_id',
        required=True,
    )
    prescription_wizard_id = fields.Many2one(
        comodel_name='medical.rx.sale.wizard',
        inverse_name='sale_wizard_ids',
        default=_compute_default_session,
        readonly=True,
    )
    patient_id = fields.Many2one(
        string='Patient',
        help='Patient (used for defaults when creating sale lines)',
        comodel_name='medical.patient',
        required=True,
    )
    prescription_order_id = fields.Many2one(
        string='Prescription',
        comodel_name='medical.prescription.order',
        required=True,
        readonly=True,
    )
    line_cnt = fields.Integer(
        string='Order Line Count',
        compute='_compute_line_cnt',
    )
    partner_id = fields.Many2one(
        string='Customer',
        comodel_name='res.partner',
        required=True,
    )
    pricelist_id = fields.Many2one(
        string='Pricelist',
        comodel_name='product.pricelist',
        required=True,
    )
    partner_invoice_id = fields.Many2one(
        string='Invoice Partner',
        comodel_name='res.partner',
    )
    partner_shipping_id = fields.Many2one(
        string='Ship To',
        comodel_name='res.partner',
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        comodel_name='medical.pharmacy',
        required=True,
    )
    client_order_ref = fields.Char(
        string='Order Reference',
    )
    origin = fields.Char()
    currency_id = fields.Many2one(
        string='Currency',
        comodel_name='res.currency',
    )
    date_order = fields.Date(
        string='Order Date',
    )
    warehouse_id = fields.Many2one(
        string='Warehouse',
        comodel_name='stock.warehouse',
        required=True,
    )
    company_id = fields.Many2one(
        string='Company',
        comodel_name='res.company',
        required=True,
    )
    note = fields.Text()
    user_id = fields.Many2one(
        string='Salesperson',
        comodel_name='res.users',
        required=True,
        readonly=True,
    )
    section_id = fields.Many2one(
        string='Sales Team',
        comodel_name='crm.case.section',
    )
    amount_untaxed = fields.Float(
        compute='_compute_all_amounts',
        digits_compute=dp.get_precision('Account'),
    )
    payment_term = fields.Many2one(
        string='Payment Term',
        comodel_name='account.payment.term',
    )
    fiscal_position = fields.Many2one(
        string='Fiscal Position',
        comodel_name='account.fiscal.position',
    )
    project_id = fields.Many2one(
        string='Project',
        comodel_name='account.analytic.account',
    )
    state = fields.Selection([
        ('new', _('Not Started')),
        ('start', _('Started')),
        ('done', _('Completed')),
    ],
        readonly=True,
        default='new',
    )

    @api.multi
    def next_wizard(self, ):
        self.ensure_one()
        self.state = 'done'
        #   @TODO: allow this workflow without a parent wizard
        wizard_action = self.prescription_wizard_id.next_wizard()
        _logger.debug('next_wizard: %s', wizard_action)
        return wizard_action

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
            'user_id': self.user_id.id,
            'company_id': self.company_id.id,
            'partner_id': self.partner_id.id,
            'partner_invoice_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'prescription_order_id': self.prescription_order_id.id,
            'pricelist_id': self.pricelist_id.id,
            'pharmacy_id': self.pharmacy_id.id,
            'date_order': self.date_order,
            'client_order_ref': self.client_order_ref,
            'warehouse_id': self.warehouse_id.id,
            'state': 'rx_verify',
            'order_line': self.order_line._to_insert(),
            'currency_id': self.currency_id.id,
            'origin': self.origin,
            'note': self.note,
            'section_id': self.section_id.id,
            'payment_term': self.payment_term.id,
            'fiscal_position': self.fiscal_position.id,
            'project_id': self.project_id.id,
        }
