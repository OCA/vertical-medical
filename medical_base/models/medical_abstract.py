# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class MedicalAbstract(models.AbstractModel):
    # FHIR Entity: default entity, as all models have internal_identifiers
    _name = 'medical.abstract'

    internal_identifier = fields.Char(
        name='Identifier',
        help='Internal identifier used to identify this record',
        readonly=True,
        default='/'
    )  # FHIR Field: identifier

    @api.model
    def create(self, vals):
        if vals.get('internal_identifier', '/') == '/':
            vals['internal_identifier'] = self._get_internal_identifier(vals)
        return super(MedicalAbstract, self).create(vals)

    def _get_internal_identifier(self, vals):
        # It should be rewritten for each element
        raise UserError(_('Function is not defined'))
