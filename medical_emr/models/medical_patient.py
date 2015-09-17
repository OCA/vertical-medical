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
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import api, fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    @api.one
    def action_invalidate(self):
        super(MedicalPatient, self).action_invalidate()
        self.disease_ids.action_invalidate()

    family_id = fields.Many2one(
        comodel_name='medical.family', string='Family')
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'), ], string='Blood Type')
    rh = fields.Selection([
        ('+', '+'),
        ('-', '-')], string='Rh')
    primary_care_physician_id = fields.Many2one(
        comodel_name='medical.physician', string='Primary Care Doctor')
    childbearing_age = fields.Boolean(string='Childbearing Age')
    medication_ids = fields.One2many(
        comodel_name='medical.patient.medication', inverse_name='patient_id',
        string='Medications')
    evaluation_ids = fields.One2many(
        comodel_name='medical.patient.evaluation', inverse_name='patient_id',
        string='Evaluations')
    critical_info = fields.Text(
        string='Important disease, allergy or procedures information')
    disease_ids = fields.One2many(
        comodel_name='medical.patient.disease', inverse_name='patient_id',
        string='Diseases')
    ethnicity_id = fields.Many2one(
        comodel_name='medical.ethnicity', string='Ethnicity')
    cause_of_death_pathology_id = fields.Many2one(
        comodel_name='medical.pathology', string='Cause of Death Pathology')
