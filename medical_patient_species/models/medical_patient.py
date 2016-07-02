# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models
from openerp.exceptions import ValidationError


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    species_id = fields.Many2one(
        string='Species',
        required=True,
        comodel_name='medical.patient.species',
        help='Select the species of the patient.',
    )
    is_person = fields.Boolean(
        related='species_id.is_person',
        help='Check if the party is a person.',
    )

    @api.multi
    @api.constrains('parent_id')
    def _check_parent_id_exists(self):
        if not self.is_person and not self.parent_id.name:
            raise ValidationError(
                'Must have a legal representative if not human.'
            )
