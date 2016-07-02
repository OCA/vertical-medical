# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MedicalPatientSpecies(models.Model):
    _name = 'medical.patient.species'
    _description = 'Medical Patient Species'

    name = fields.Char(
        string='Species',
        help='Name of the species',
        size=256,
        required=True,
        translate=True,
    )
    is_person = fields.Boolean(
        readonly=True,
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        human = self.env.ref('medical_patient_species.human')
        self.is_person = (self.id == human.id)
        return super(MedicalPatientSpecies, self).create(vals)

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
