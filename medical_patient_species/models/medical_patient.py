# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    species_id = fields.Many2one(
        string='Species',
        comodel_name='medical.patient.species',
        help='Select the species of the patient.',
    )
    is_person = fields.Boolean(
        related='species_id.is_person',
        help='Check if the party is a person.',
    )

    @api.multi
    @api.constrains('parent_id', 'species_id')
    def _check_parent_id(self):
        for rec_id in self:
            if not rec_id.is_person and not rec_id.parent_id:
                raise ValidationError(
                    _('Must have a legal representative if not Human.')
                )

    @api.constrains('species_id')
    def _check_species_id(self):
        if not self.species_id:
            raise ValidationError(
                _('Must have a species defined')
            )

    @api.model
    def create(self, vals):
        if not vals.get('species_id'):
            human = self.env.ref('medical_patient_species.human')
            vals.update({'species_id': human.id})
        return super(MedicalPatient, self).create(vals)
