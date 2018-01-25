# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, fields, models
import openerp.addons.decimal_precision as dp
import logging


_logger = logging.getLogger(__name__)


class MedicalSaleTemp(models.TransientModel):
    _name = 'medical.sale.temp'
    _description = 'Temporary order info for Sale2Rx workflow'

    note = fields.Text()
    origin = fields.Char()
    order_line = fields.One2many(
        string='Order Lines',
        comodel_name='medical.sale.line.temp',
        inverse_name='order_id',
        required=True,
    )
    prescription_wizard_id = fields.Many2one(
        comodel_name='medical.sale.wizard',
        inverse_name='sale_wizard_ids',
        default=lambda s: s._compute_default_session(),
        readonly=True,
    )
    patient_id = fields.Many2one(
        string='Patient',
        help='Patient (used for defaults when creating sale lines)',
        comodel_name='medical.patient',
        required=True,
    )
    prescription_order_ids = fields.Many2many(
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
    currency_id = fields.Many2one(
        string='Currency',
        comodel_name='res.currency',
    )
    date_order = fields.Date(
        string='Order Date',
    )
    company_id = fields.Many2one(
        string='Company',
        comodel_name='res.company',
        required=True,
    )
    user_id = fields.Many2one(
        string='Salesperson',
        comodel_name='res.users',
        required=True,
        readonly=True,
    )
    team_id = fields.Many2one(
        string='Sales Team',
        comodel_name='crm.team',
    )
    amount_untaxed = fields.Float(
        string='Total Before Tax',
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
    state = fields.Selection(
        selection=[
            ('new', 'Not Started'),
            ('start', 'Started'),
            ('done', 'Completed'),
        ],
        readonly=True,
        default='new',
    )

    @api.model
    def _compute_default_session(self):
        return self.env['medical.sale.wizard'].browse(
            self._context.get('active_id')
        )

    @api.multi
    def _compute_line_cnt(self):
        for record in self:
            record.line_cnt = len(record.order_line)

    @api.multi
    def _compute_all_amounts(self):
        for record in self:
            untaxed = 0.0
            for line in record.order_line:
                untaxed += line.price_subtotal
            record.amount_untaxed = untaxed

    @api.multi
    def action_next_wizard(self):
        self.ensure_one()
        self.state = 'done'
        wizard_action = self.prescription_wizard_id.action_next_wizard()
        _logger.debug('next_wizard: %s', wizard_action)
        return wizard_action

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
            yield self._to_vals()

    @api.multi
    def _to_vals(self):
        """ Return a values dictionary to create in real model """
        self.ensure_one()
        pids = [(4, p.id, 0) for p in self.prescription_order_ids]
        return {
            'user_id': self.user_id.id,
            'company_id': self.company_id.id,
            'partner_id': self.partner_id.id,
            'partner_invoice_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'prescription_order_ids': pids,
            'pricelist_id': self.pricelist_id.id,
            'pharmacy_id': self.pharmacy_id.id,
            'date_order': self.date_order,
            'client_order_ref': self.client_order_ref,
            'state': 'sale',
            'order_line': self.order_line._to_insert(),
            'currency_id': self.currency_id.id,
            'origin': self.origin,
            'note': self.note,
            'team_id': self.team_id.id,
            'project_id': self.project_id.id,
        }
