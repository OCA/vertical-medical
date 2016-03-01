# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    species_id = fields.Many2one(
        string='Species',
        comodel_name='medical.patient.species',
        default=lambda self: self.env.ref('medical_patient_species.human'),
        help='Select the species of the patient.',
    )
    is_person = fields.Boolean(
        related='species_id.is_person',
        help='Check if the party is a person.',
    )
