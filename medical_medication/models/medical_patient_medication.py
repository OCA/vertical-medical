# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Ported to 8.0 & 9.0 by Dave Lasley - LasLabs (https://laslabs.com)
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

from openerp import fields, models, _


class MedicalPatientMedication(models.Model):
    _name = 'medical.patient.medication'
    _description = 'Medical Patient Medication'
    _inherit = ['abstract.medical.medication', 'medical.medication.template']
    _rec_name = 'patient_id'

    medication_template_id = fields.Many2one(
        string='Medication Template', 
        comodel_name='medical.medication.template',
        index=True,
        help=_('Template to apply to this medication'),
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        index=True,
        required=True,
        help=_('Patient that is taking this medication'),
    )
    physician_id = fields.Many2one(
        string='Physician',
        comodel_name='medical.physician',
        index=True,
        help=_('Physician who prescribed the medicament'),
    )
    active = fields.Boolean(
        help=_('Check if the patient is currently taking the medication'),
        default=True,
    )
    is_course_complete = fields.Boolean(
        string='Course Completed',
        help=_(
            'Check this if the patient is no longer taking this medication'
        ),
    )
    is_discontinued = fields.Boolean(
        help=_('Check this if the medication has been discontinued'),
    )
    discontinued_reason = fields.Char(
        help=_(
            'Short description explaining why the medication was discontinued'
        ),
    )
    date_start_treatment = fields.Datetime(
        help=_('When the patient began taking this medication'),
    )
    date_stop_treatment = fields.Datetime(
        help=_('When the patient is scheduled to stop this medication'),
    )
    adverse_reaction = fields.Text(
        help=_('Side effects or adverse reactions that patient experienced'),
    )
    notes = fields.Text(
        help=_('Any additional information regarding this treatment'),
    )
