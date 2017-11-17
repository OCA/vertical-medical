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
    is_editable = fields.Boolean(
        compute='_compute_is_editable'
    )

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

    @api.multi
    @api.depends('state')
    def _compute_is_editable(self):
        for rec in self:
            if rec.state in ('suspended', 'inactive'):
                rec.is_editable = False
            else:
                rec.is_editable = True

    def active2suspended(self):
        self.write({'state': 'suspended'})

    def suspended2active(self):
        self.write({'state': 'active'})

    def active2inactive(self):
        self.write({'state': 'inactive'})

    def inactive2active(self):
        self.write({'state': 'active'})

    def suspended2inactive(self):
        self.write({'state': 'inactive'})
