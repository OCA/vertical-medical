# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _
from openerp import api, fields, models
from openerp.exceptions import Warning


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
    @api.returns('s', lambda value: value.id)
    def create(self, vals):
        try:
            human = self.env.ref('medical_patient_species.human')
        except:
            vals['is_person'] = (vals['name'].lower() == "human")
        else:
            vals['is_person'] = (self.id == human.id)
        return super(MedicalPatientSpecies, self).create(vals)

    @api.multi
    def unlink(self):
        for record in self:
            if record.id == self.env.ref('medical_patient_species.human').id:
                raise Warning(
                    _('Human is a permanent record and cannot be destroyed')
                )
            else:
                return super(MedicalPatientSpecies, record).unlink()

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
