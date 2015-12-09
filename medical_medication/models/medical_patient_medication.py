# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Ported to 8.0 by Dave Lasley - LasLabs (https://laslabs.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import fields, models


class MedicalPatientMedication(models.Model):
    _name = 'medical.patient.medication'
    _description = 'Medical Patient Medication'
    _inherit = ['abstract.medical.medication', 'medical.medication.template']
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(
        comodel_name='medical.patient', string='Patient', index=True,
        required=True)
    physician_id = fields.Many2one(
        comodel_name='medical.physician', string='Physician',
        help='Physician who prescribed the medicament', index=True,
        required=True)
    active = fields.Boolean(
        help='Check if the patient is currently taking the medication',
        default=True)
    is_course_complete = fields.Boolean(string='Course Completed')
    is_discontinued = fields.Boolean()
    date_start_treatment = fields.Datetime(required=True)
    date_stop_treatment = fields.Datetime()
    discontinued_reason = fields.Char(
        help='Short description for discontinuing the treatment')
    adverse_reaction = fields.Text(
        help='Side effects or adverse reactions that patient experienced')
    notes = fields.Text()
