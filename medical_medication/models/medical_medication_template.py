# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import fields, models, api


class MedicalMedicationTemplate(models.Model):
    _name = 'medical.medication.template'
    _description = 'Medical Medication Template'
    _rec_name = 'pathology_id'

    medicament_id = fields.Many2one(
        string='Medicament',
        comodel_name='medical.medicament',
        required=True,
    )
    pathology_id = fields.Many2one(
        string='Pathology',
        comodel_name='medical.pathology', 
        help=_('Choose a disease for this medicament from the disease list.'
        ' It can be an existing disease of the patient or a prophylactic.'),
    )
    duration = fields.Integer(
        help=_('Period that the patient must take the medication'),
    )
    duration_uom_id = fields.Many2one(
        string='Duration UoM',
        comodel_name='product.uom',
        domain=[('category_id.name', '=', 'Time')],
        help=_('Measurement unit for medication duration'),
    )
    frequency = fields.Integer(
        help=_('Time in between doses the patient must wait (ie, for 1 pill '
        'each 8 hours, put here 8 and select "hours\" in the unit field'),
    )
    frequency_uom_id = fields.Many2one(
        string='Frequency UoM',
        help=_('Measurement unit for medication frequency'),
    )
    frequency_prn = fields.Boolean(
        help=_('Use medication as needed (pro re nata)'),
    )
    medication_dosage_id = fields.Many2one(
        string='Common Dose',
        comodel_name='medical.medication.dosage',
        help=_('Common / standard dosage frequency for this medicament'),
    )
    suggested_administration_hours = fields.Char(
        help=_('Time that medication should typically be administered'),
    )
    quantity = fields.Integer(
        string='Dose Quantity',
        help=_('Quantity of units (eg, 2 capsules) of the medicament'),
    )
    dose_uom_id = fields.Many2one(
        comodel_name='product.uom', string='Dose Unit',
        help=_('Measurement unit for dosage quantity'),
    )

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            if self.medication_dosage_id:
                name = self.medication_dosage_id.name
            elif self.frequency and self.frequency_uom_id:
                name = '%s / %s' % (self.frequency, self.frequency_uom_id)
            elif self.pathology_id:
                name = self.pathology_id.name
            else:
                name = self.medicament_id.name
            res.append((rec.id, name))
        return res
