# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalLocation(models.Model):
    # FHIR Entity: Location (https://www.hl7.org/fhir/location.html)
    _name = 'medical.location'
    _description = 'Medical Location'
    _inherit = 'medical.abstract.partner'

    _STATES = [
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('inactive', 'Inactive'),
    ]

    state = fields.Selection(
        _STATES,
        readonly=False,
        default='active',
    )  # FHIR field: status
    description = fields.Text(
        string='Description',
    )  # FHIR field: description

    @api.model
    def create(self, vals):
        vals.update({
            'is_company': True,
            'customer': False,
        })
        return super(MedicalLocation, self).create(vals)

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.location') or '/'
