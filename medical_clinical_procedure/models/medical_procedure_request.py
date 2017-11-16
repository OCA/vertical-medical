# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class MedicalProcedureRequest(models.Model):
    """
        Medical Procedure request
        FHIR Model: Procedure request (
            https://www.hl7.org/fhir/procedurerequest.html)
    """
    _name = 'medical.procedure.request'
    _description = 'Procedure Request'
    _inherit = 'medical.request'
    _order = 'sequence, id'

    sequence = fields.Integer(
        required=True,
        default=1,
    )
    occurrence = fields.Datetime(
        string='Occurrence date',
        help='When the procedure should occur',
        required=True,
        default=fields.Datetime.now,
    )
    procedure_ids = fields.One2many(
        string='Related Procedure',
        comodel_name='medical.procedure',
        inverse_name='procedure_request_id',
        readonly=True,
    )
    procedure_count = fields.Integer(
        compute="_compute_procedure_count",
        string='# of Procedures',
        copy=False,
    )

    @api.depends('procedure_ids')
    def _compute_procedure_count(self):
        for record in self:
            record.procedure_count = len(record.procedure_ids)

    @api.multi
    def unlink(self):
        if self.mapped('procedure_ids'):
            raise exceptions.Warning(
                _('You cannot delete a record that refers to a Procedure!'))
        return super(MedicalProcedureRequest, self).unlink()

    @api.multi
    def action_view_procedure(self):
        self.ensure_one()
        action = self.env.ref(
            'medical_clinical_procedure.medical_procedure_action')
        result = action.read()[0]

        result['context'] = {
            'default_patient_id': self.patient_id.id,
            'default_performer_id': self.performer_id.id,
            'default_procedure_request_id': self.id,
            'default_name': self.name,
        }
        result['domain'] = "[('procedure_request_id', '=', " + \
                           str(self.id) + ")]"
        if len(self.procedure_ids) == 1:
            res = self.env.ref('medical.procedure.view.form', False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = self.procedure_ids.id
        return result

    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.procedure.request') or '/'

    def _get_procedure_values(self):
        self.ensure_one()
        return {
            'procedure_request_id': self.id,
            'name': self.name,
            'plan_definition_id': (
                self.plan_definition_id and self.plan_definition_id.id
            ),
            'activity_definition_id': (
                self.activity_definition_id and self.activity_definition_id.id
            ),
            'plan_definition_action_id': (
                self.plan_definition_action_id and
                self.plan_definition_action_id.id
            ),
            'service_id': self.service_id and self.service_id.id,
            'patient_id': self.patient_id.id,
            'performer_id': self.performer_id and self.performer_id.id
        }

    @api.multi
    def generate_event(self):
        proc_obj = self.env['medical.procedure']
        procedure_ids = []
        for request in self:
            vals = request._get_procedure_values()
            procedure = proc_obj.create(vals)
            procedure_ids.append(procedure.id)
        return proc_obj.browse(procedure_ids)
