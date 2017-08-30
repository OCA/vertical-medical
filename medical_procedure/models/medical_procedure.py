# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class MedicalProcedure(models.Model):
    _name = 'medical.procedure'
    _description = 'Medical Procedure'
    _inherit = 'mail.thread'

    _STATES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('completed', 'Completed'),
        ('completed-and-invoiced', 'Completed and Invoiced'),
        ('entered-in-error', 'Entered in Error'),
        ('cancelled', 'Cancelled'),
        ('unknown', 'Unknown'),
    ]

    @api.constrains('procedure_request_id')
    def _check_procedure(self):
        if len(self.procedure_request_id.procedure_ids) > 1:
            raise exceptions.ValidationError(
                "You cannot create more than one Procedure "
                "for each Procedure Request.")

    @api.multi
    @api.depends('internal_identifier', 'title')
    def _compute_name(self):
        for rec in self:
            rec.name = '[%s]' % rec.internal_identifier
            if rec.title:
                rec.name = '%s %s' % (rec.name, rec.title)

    internal_identifier = fields.Char(
        string='Procedure ID',
        default='/',
        readonly=True,
    )
    subject_id = fields.Many2one(
    #TODO: to be extended with subject groups.
        string='Patient',
        comodel_name='medical.patient',
        required=True,
        index=True,
        help='Patient Name',
    )
    performer_id = fields.Many2one(
        # to be extended with groups.
        string='Performer',
        comodel_name='medical.practitioner',
        help='Who performed the procedure',
    )
    priority = fields.Selection(
        [('low', 'Low'),
         ('normal', 'Normal'),
         ('high', 'High')],
        required=True,
        default='normal',
    )
    procedure_request_id = fields.Many2one(
        string='Procedure Request',
        comodel_name='medical.procedure.request',
        index=True,
        readonly=True,
        help='The request for this procedure',
    )
    date_start = fields.Datetime(
        'Start Date',
        required=True,
        copy=False,
        default=fields.Datetime.now,
        help='date when the procedure was initiated',
    )
    date_end = fields.Datetime(
        'End Date',
        copy=False,
        help='date when the procedure was finished',
    )
    title = fields.Char(
        string='Title',
        help="Human-friendly name for the Procedure",
    )
    state = fields.Selection(
        selection=_STATES,
        string='Status',
        index=True,
        track_visibility='onchange',
        required=True,
        default='draft',
    )
    details = fields.Text(
        string='Procedure Details',
    )
    is_editable = fields.Boolean(
        string="Is editable",
        compute="_compute_is_editable",
        readonly=True,
    )
    service_id = fields.Many2one(
        string='Service',
        comodel_name='product.product',
        domain="[('type', '=', 'service')]",
    )
    center_id = fields.Many2one(
        string='Center',
        comodel_name='medical.center',
        required=True,
        index=True,
        help='Responsible Medical Center',
    )

    def _change_date_end(self):
        self.date_end = fields.Datetime.now()
        return self.date_end

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['internal_identifier'] = self.env['ir.sequence'].next_by_code(
                'medical.procedure') or '/'
        return super(MedicalProcedure, self).create(vals)

    @api.multi
    def name_get(self):
        # TDE: this could be cleaned a bit I think

        def _name_get(d):
            name = d.get('name', '')
            code = self._context.get('display_default_code', True) and d.get(
                'default_code', False) or False
            if code:
                name = '[%s] %s' % (code, name)
            return (d['id'], name)

        result = []
        for procedure in self.sudo():
            name = '[%s]' % procedure.internal_identifier
            if procedure.title:
                name = '%s %s' % (name, procedure.title)
            result.append((procedure.id, name))
        return result

    @api.multi
    @api.depends('state')
    def _compute_is_editable(self):
        for rec in self:
            if rec.state in ('active', 'suspended', 'completed',
                             'completed-and-invoiced', 'entered-in-error',
                             'cancelled', 'unknown'):
                rec.is_editable = False
            else:
                rec.is_editable = True

    @api.multi
    def button_draft(self):
        for rec in self:
            rec.state = 'draft'
        return True

    @api.multi
    def button_active(self):
        for rec in self:
            rec.state = 'active'
        return True

    @api.multi
    def button_suspended(self):
        for rec in self:
            rec.state = 'suspended'
        return True

    @api.multi
    def button_completed(self):
        for rec in self:
            self._change_date_end()
            rec.state = 'completed'
        return True

    @api.multi
    def button_completed_and_invoiced(self):
        for rec in self:
            rec.state = 'completed-and-invoiced'
        return True

    @api.multi
    def button_entered_in_error(self):
        for rec in self:
            rec.state = 'entered-in-error'
        return True

    @api.multi
    def button_cancelled(self):
        for rec in self:
            self._change_date_end()
            rec.state = 'cancelled'
        return True

    @api.multi
    def button_unknown(self):
        for rec in self:
            rec.state = 'unknown'
        return True
