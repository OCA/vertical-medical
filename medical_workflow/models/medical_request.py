# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class MedicalRequest(models.AbstractModel):
    """
        Medical reference request
        FHIR Model: Request (https://www.hl7.org/fhir/request.html)
    """
    _name = 'medical.request'
    _description = 'Medical request'

    _STATES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('completed', 'Completed'),
        ('entered-in-error', 'Entered in Error'),
        ('cancelled', 'Cancelled'),
    ]

    internal_identifier = fields.Char(
        string='Internal identifier ID',
        default='/',
        readonly=True,
    )  # FHIR field: identifier
    name = fields.Char(
        string='Name',
        help='Name',
    )
    state = fields.Selection(
        _STATES,
        readonly=False,
        states={
            'cancelled': [('readonly', True)],
            'completed': [('readonly', True)]
        },
        required=True,
        default='draft',
    )  # FHIR field: status
    intent = fields.Selection(
        [('proposal', 'Proposal'),
         ('plan', 'Plan'),
         ('order', 'Order'),
         ('option', 'Option')],
        required=True,
        default='proposal',
    )   # FHIR Field: intent
    priority = fields.Selection(
        [('low', 'Low'),
         ('normal', 'Normal'),
         ('high', 'High')],
        required=True,
        default='normal',
    )   # FHIR Field: priority
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        required=True,
        index=True,
        help='Patient Name',
    )   # FHIR field: subject
    performer_id = fields.Many2one(
        string='Performer',
        comodel_name='medical.practitioner',
        help='Who is to perform the procedure',
    )  # FHIR Field : performer
    service_id = fields.Many2one(
        string='Service',
        comodel_name='product.product',
        domain="[('type', '=', 'service')]",
    )   # FHIR Field: code
    order_by_id = fields.Many2one(
        string="Ordered by",
        comodel_name='res.partner',
        help="Person who has initiated the order.",
    )   # FHIR Field: requester/agent
    order_date = fields.Datetime(
        string="Order date",
        help="Start of the order.",
    )   # FHIR Field: authoredOn
    observations = fields.Text(
        string='Observations',
    )   # FHIR Field: note
    plan_definition_id = fields.Many2one(
        comodel_name='workflow.plan.definition'
    )   # FHIR Field: definition

    activity_definition_id = fields.Many2one(
        comodel_name='workflow.activity.definition',
    )   # FHIR Field: definition

    plan_definition_action_id = fields.Many2one(
        comodel_name='workflow.plan.definition.action',
    )   # FHIR Field: definition
    is_editable = fields.Boolean(
        compute='_compute_is_editable'
    )

    @api.multi
    @api.depends('state')
    def _compute_is_editable(self):
        for rec in self:
            if rec.state in ('active', 'suspended', 'completed',
                             'entered-in-error', 'cancelled', 'unknown'):
                rec.is_editable = False
            else:
                rec.is_editable = True

    def draft2active(self):
        self.write({'state': 'active'})

    def active2suspended(self):
        self.write({'state': 'suspended'})

    def active2completed(self):
        self.write({'state': 'completed'})

    def active2error(self):
        self.write({'state': 'entered-in-error'})

    def reactive(self):
        self.write({'state': 'active'})

    def cancel(self):
        self.write({'state': 'cancelled'})

    def _get_internal_identifier(self, vals):
        """TO-DO: Implement method to define the correct sequence for the
        internal identifier."""
        raise UserError(_('Function is not defined'))

    @api.model
    def create(self, vals):
        if vals.get('internal_identifier', '/') == '/':
            vals['internal_identifier'] = self._get_internal_identifier(vals)
        return super(MedicalRequest, self).create(vals)

    @api.multi
    def generate_event(self):
        """ Implement method in order to generate an event"""
        raise UserError(_('Function is not defined'))
