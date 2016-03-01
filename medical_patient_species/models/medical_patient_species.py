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
        compute='_compute_is_person',
        store=True,
    )

    @api.multi
    def _compute_is_person(self):
        for rec_id in self:
            rec_id.is_person = (
                rec_id.id == self.env.ref('medical_patient_species.human').id
            )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
