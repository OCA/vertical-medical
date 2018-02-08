# -*- coding: utf-8 -*-
# #############################################################################
#
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
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

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            if self.medication_dosage_id:
                name = self.medication_dosage_id.name
            elif self.frequency and self.frequency_unit:
                name = '%s / %s' % (self.frequency, self.frequency_unit)
            elif self.pathology_id:
                name = self.pathology_id.name
            else:
                name = self.medicament_id.name
            res.append((rec.id, name))
        return res

    medicament_id = fields.Many2one(
        comodel_name='medical.medicament', string='Medicament', required=True)
    pathology_id = fields.Many2one(
        comodel_name='medical.pathology', string='Pathology',
        help='Choose a disease for this medicament from the disease list. '
        'It can be an existing disease of the patient or a prophylactic.')
    duration = fields.Integer(
        help='Period that the patient must take the medication. in minutes,'
        ' hours, days, months, years or indefinately')
    duration_period = fields.Selection(selection=[
        ('minutes', 'Minutes'),
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('months', 'Months'),
        ('years', 'Years'),
        ('indefinite', 'Indefinite'),
    ], help='Period that the patient must take the medication in minutes, '
        'hours, days, months, years or indefinately')
    frequency = fields.Integer(
        help='Time in between doses the patient must wait (ie, for 1 pill '
        'each 8 hours, put here 8 and select "hours\" in the unit field')
    frequency_unit = fields.Selection(selection=[
        ('seconds', 'seconds'),
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('weeks', 'weeks'),
        ('wr', 'when required'),
    ])
    frequency_prn = fields.Boolean(help='Use it as needed, pro re nata')
    medication_dosage_id = fields.Many2one(
        comodel_name='medical.medication.dosage', string='Common Dose',
        help='Common / standard dosage frequency for this medicament')
    suggested_administration_hours = fields.Char()
    quantity = fields.Integer(
        string='Dose Quantity',
        help='Quantity of units (eg, 2 capsules) of the medicament')
    dose_unit_id = fields.Many2one(
        comodel_name='product.uom', string='Dose Unit')
