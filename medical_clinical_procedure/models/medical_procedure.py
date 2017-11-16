# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class MedicalProcedure(models.Model):
    """
        Medical procedure
        FHIR Model: Procedure (https://www.hl7.org/fhir/procedure.html)
    """
    _name = 'medical.procedure'
    _description = 'Medical Procedure'
    _inherit = 'medical.event'

    procedure_request_id = fields.Many2one(
        comodel_name='medical.procedure.request',
        string='Procedure request',
        readonly=True
    )   # FHIR Field: BasedOn
    performed_initial_date = fields.Datetime(
        string='Initial date'
    )   # FHIR Field: performed/performedPeriod
    performed_end_date = fields.Datetime(
        string='End date'
    )   # FHIR Field: performed/performedPeriod

    @api.constrains('procedure_request_id')
    def _check_procedure(self):
        if len(self.procedure_request_id.procedure_ids) > 1:
            raise exceptions.ValidationError(
                _("You cannot create more than one Procedure "
                    "for each Procedure Request."))

    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.procedure') or '/'

    @api.multi
    def preparation2in_progress(self):
        res = super(MedicalProcedure, self).preparation2in_progress()
        for record in self:
            if not record.performed_initial_date:
                record.performed_initial_date = fields.Datetime.now()
        return res

    @api.multi
    def in_progress2completed(self):
        res = super(MedicalProcedure, self).in_progress2completed()
        for record in self:
            if not record.performed_end_date:
                record.performed_end_date = fields.Datetime.now()
        return res
