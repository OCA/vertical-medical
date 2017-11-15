# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalAdministrationPractitioner(models.Model):
    # FHIR Entity: Practitioner (https://www.hl7.org/fhir/practitioner.html)
    _name = 'medical.administration.practitioner'
    _description = 'Medical Administration Practitioner'
    _inherit = 'medical.abstract.partner'

    role_ids = fields.Many2many(
        string='Roles',
        comodel_name='medical.role',
    )   # FHIR Field: PractitionerRole
    practitioner_type = fields.Selection(
        string='Entity Type',
        selection=[('internal', 'Internal Entity'),
                   ('external', 'External Entity')],
        readonly=False,
    )

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.administration.practitioner') or '/'
