# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class MedicalProcedureRequest(models.Model):
    _name = 'medical.procedure.request'
    _description = 'Medical Procedure Request'
    _inherit = 'mail.thread'
    _order = 'sequence, id'

    _STATES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('completed', 'Completed'),
        ('entered-in-error', 'Entered in Error'),
        ('cancelled', 'Cancelled'),
    ]

    internal_identifier = fields.Char(
        string='Procedure Request ID',
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
        #TODO: to be extended with groups.
        string='Performer',
        comodel_name='medical.practitioner',
        help='Who is to perform the procedure',
    )
    procedure_ids = fields.One2many(
        string='Related Procedure',
        comodel_name='medical.procedure',
        inverse_name='procedure_request_id',
        readonly=True,
    )
    occurrence = fields.Datetime(
        string='Occurrence date',
        help='When the procedure should occur',
        required=True,
        default=fields.Datetime.now,
    )
    service_id = fields.Many2one(
        string='Service',
        comodel_name='product.product',
        domain="[('type', '=', 'service')]",
    )
    intent = fields.Selection(
        [('proposal', 'Proposal'),
         ('plan', 'Plan'),
         ('order', 'Order'),
         ('option', 'Option')],
        required=True,
        default='proposal',
    )
    priority = fields.Selection(
        [('low', 'Low'),
         ('normal', 'Normal'),
         ('high', 'High')],
        required=True,
        default='normal',
    )
    requester = fields.Many2one(
        string='Requested by',
        comodel_name='res.users',
        default=lambda self: self.env.user,
    )
    authored_on = fields.Datetime(
        'Request date',
        required=True,
        copy=False,
        default=fields.Datetime.now,
        help='When was the request made',
    )
    title = fields.Char(
        string='Title',
        help="Human-friendly name for the Procedure Request",
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('active', 'Active'),
         ('suspended', 'Suspended'),
         ('completed', 'Completed'),
         ('entered-in-error', 'Entered in Error'),
         ('cancelled', 'Cancelled')],
        readonly=False,
        states={'cancelled': [('readonly', True)]},
        required=True,
        default='draft',
    )
    observations = fields.Text(
        string='Observations',
    )
    request_group_id = fields.Many2one(
        string='Originating Request Group',
        comodel_name='medical.request.group',
    )
    center_id = fields.Many2one(
        string='Center',
        comodel_name='medical.center',
        required=True,
        index=True,
        help='Responsible Medical Center',
    )
    procedure_count = fields.Integer(
        compute="_compute_procedure_count",
        string='# of Procedures',
        copy=False,
        default=0,
    )
    request_group_active = fields.Boolean(
        string='Request Group Active',
        default=False,
        compute='_compute_request_group_active',
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )
    is_billable = fields.Boolean(
        string='Is billable?',
        default=False,
    )

    @api.multi
    @api.depends('internal_identifier', 'title')
    def _compute_name(self):
        for rec in self:
            rec.name = '[%s]' % rec.internal_identifier
            if rec.title:
                rec.name = '%s %s' % (rec.name, rec.title)

    @api.depends('procedure_ids')
    def _compute_procedure_count(self):
        self.procedure_count = len(self.procedure_ids)

    @api.multi
    def _compute_request_group_active(self):
        for rec in self:
            if rec.env.user._has_group('medical_request_group.'
                                       'group_request_group'):
                rec.request_group_active = True
            else:
                rec.request_group_active = False

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
        for ProcedureRequest in self.sudo():
            name = '[%s]' % ProcedureRequest.internal_identifier
            if ProcedureRequest.title:
                name = '%s %s' % (name, ProcedureRequest.title)
            result.append((ProcedureRequest.id, name))
        return result

    @api.multi
    def unlink(self):
        if self.mapped('procedure_ids'):
            raise exceptions.Warning(
                _('You cannot delete a record that refers to a Procedure!'))
        return super(MedicalProcedureRequest, self).unlink()

    @api.multi
    @api.depends('state')
    def _compute_is_editable(self):
        for rec in self:
            if rec.state in ('active', 'suspended', 'completed',
                             'entered-in-error', 'cancelled', 'unknown'):
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
            rec.state = 'completed'
        return True

    @api.multi
    def button_entered_in_error(self):
        for rec in self:
            rec.state = 'entered-in-error'
        return True

    @api.multi
    def button_cancelled(self):
        for rec in self:
            rec.state = 'cancelled'
        return True

    @api.multi
    def button_unknown(self):
        for rec in self:
            rec.state = 'unknown'
        return True

    @api.multi
    def action_view_procedure(self):
        action = self.env.ref('medical_procedure.medical_procedure_action')
        result = action.read()[0]

        result['context'] = {'default_subject_id': self.subject_id.id,
                             'default_performer_id': self.performer_id.id,
                             'default_priority': self.priority,
                             'default_procedure_request_id': self.id,
                             'default_title': self.title,
                             'default_center_id': self.center_id.id,
                             }

        if not self.procedure_ids:
            journal_domain = [
                ('subject_id', '=', self.subject_id.id),
                ('performer_id', '=', self.performer_id.id),
                ('priority', '=', self.priority),
                ('procedure_request_id', '=', self.id),
                ('title', '=', self.title),
                ('center_id', '=', self.center_id.id),
            ]
            default_journal_id = self.env['medical.procedure'].search(
                journal_domain, limit=1)
            if default_journal_id:
                result['context']['default_journal_id'] = default_journal_id.id
        else:
            result['context']['default_journal_id'] = self.procedure_ids[
                0].subject_id.id

        if len(self.procedure_ids) != 1:
            result['domain'] = "[('id', 'in', " + str(self.procedure_ids.ids) + \
                               ")]"
        elif len(self.procedure_ids) == 1:
            res = self.env.ref('medical.procedure.view.form', False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = self.procedure_ids.id
        return result

    def _get_ir_sequence(self, vals):
        """TO-DO: Implement method to define the correct sequence for the
        internal identifier."""
        return 'medical.procedure.request'

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            ir_sequence = self._get_ir_sequence(vals)
            vals['internal_identifier'] = self.env['ir.sequence'].next_by_code(
                ir_sequence) or '/'
        return super(MedicalProcedureRequest, self).create(vals)

