# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class ResPartner(models.Model):
    # FHIR Entity: Location (https://www.hl7.org/fhir/location.html)
    _inherit = 'res.partner'

    @api.model
    def _default_edit_location(self):
        return self.env['res.users'].browse(
            self.env.uid
        ).has_group(
            'medical_administration_location.'
            'group_medical_location_manager'
        )

    is_location = fields.Boolean(
        default=False,
    )
    edit_location = fields.Boolean(
        default='_default_edit_location',
        compute='_compute_edit_location',
    )
    location_identifier = fields.Char(
        readonly=True,
    )  # FHIR Field: identifier
    description = fields.Text(
        string='Description',
    )  # FHIR field: description

    def _compute_edit_location(self):
        for record in self:
            record.edit_location = self._default_edit_location()

    @api.model
    def _get_medical_identifiers(self):
        res = super(ResPartner, self)._get_medical_identifiers()
        res.append((
            'is_medical',
            'is_location',
            'location_identifier',
            self._get_location_identifier
        ))
        return res

    @api.model
    def _get_location_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.location') or '/'
