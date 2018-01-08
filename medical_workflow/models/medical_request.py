# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class MedicalRequest(models.AbstractModel):
    # FHIR Entity: Request (https://www.hl7.org/fhir/request.html)
    _name = 'medical.request'
    _description = 'Medical request'
    _inherit = ['medical.abstract', 'mail.thread', 'mail.activity.mixin']

    _STATES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('completed', 'Completed'),
        ('entered-in-error', 'Entered in Error'),
        ('cancelled', 'Cancelled'),
    ]
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
    )   # FHIR field: status
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
        comodel_name='res.partner',
        domain=[('is_practitioner', '=', True)],
        help='Who is to perform the procedure',
    )   # FHIR Field : performer
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
        comodel_name='workflow.plan.definition',
    )   # FHIR Field: definition
    activity_definition_id = fields.Many2one(
        comodel_name='workflow.activity.definition',
    )   # FHIR Field: definition
    plan_definition_action_id = fields.Many2one(
        comodel_name='workflow.plan.definition.action',
    )   # FHIR Field: definition
    is_editable = fields.Boolean(
        compute='_compute_is_editable',
    )
    is_medical_request = fields.Boolean(
        'Medical request',
        compute='_compute_is_medical_request',
    )

    def _compute_is_medical_request(self):
        for rec in self:
            rec.is_medical_request = True

    def _get_medical_request_context(self, context):
        for name, field in self._fields.items():
            if field.comodel_name and 'is_medical_request' in \
                self.env[field.comodel_name]._fields and field.type == \
                    'many2one':
                context.update({'default_%s' % field.name: self[name].id})
                if 'is_medical_request' in self._fields:
                    if field.comodel_name == self._name:
                        context.update({'default_%s' % field.name: self.id})
                    else:
                        field_id = getattr(self, field.name).id
                        context.update({'default_%s' % field.name: field_id})
        return context

    @api.multi
    @api.depends('name', 'internal_identifier')
    def name_get(self):
        result = []
        for record in self:
            name = '[%s]' % record.internal_identifier
            if record.name:
                name = '%s %s' % (name, record.name)
            result.append((record.id, name))
        return result

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

    @api.multi
    def generate_event(self):
        """ Implement method in order to generate an event"""
        raise UserError(_('Function is not defined'))

    @api.model
    def _get_request_models(self):
        return []

    def _check_hierarchy_children(self, vals, counter=1):
        if self._name not in vals:
            vals[self._name] = []
        if self.id in vals[self._name]:
            raise ValidationError(_('Recursion loop found'))
        vals[self._name].append(self.id)
        if counter > 50:
            raise ValidationError(_('Too many recursion'))
        self.ensure_one()
        for model in self._get_request_models():
            for child in self.env[model].search([
                (self._get_parent_field_name(), '=', self.id)
            ]):
                child._check_hierarchy_children(vals, counter + 1)

    def _get_parent_field_name(self):
        """ Implement method in order to return the parent field name"""
        raise UserError(_('Field name is not defined'))

    @api.multi
    def action_view_request(self):
        self.ensure_one()
        model = self.env.context.get('model_name', False)
        if model:
            params = self.env[model].action_view_request_parameters()
        else:
            raise UserError(_('No model provided.'))
        inverse_name = self._get_parent_field_name()
        requests = self.env[model].search([(inverse_name, '=', self.id)])
        action = self.env.ref(params['view'])
        result = action.read()[0]
        context = {'default_patient_id': self.patient_id.id}
        context = self._get_medical_request_context(context)
        result['context'] = context
        result['domain'] = [(inverse_name, '=', self.id)]
        if len(requests) == 1:
            res = self.env.ref(params['view_form'], False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = requests.id
        return result
