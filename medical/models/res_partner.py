# -*- coding: utf-8 -*-
# #############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
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
# #############################################################################

from openerp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    relationship = fields.Char(
        'Relationship',
        size=25,
    )
    is_institution = fields.Boolean(
        string='Institution',
        help='Check if the party is a Medical Center',
    )
    relative_id = fields.Many2one(
        string='Contact',
        comodel_name='res.partner',
    )
    is_doctor = fields.Boolean(
        string='Health Prof',
        help='Check if the party is a health professional',
    )
    is_patient = fields.Boolean(
        string='Patient',
        help='Check if the party is a patient',
    )
    alias = fields.Char(
        string='Alias',
        size=256,
        help='Common name that the Party is reffered',
    )
    activation_date = fields.Date(
        string='Activation date',
        help='Date of activation of the party',
    )
    last_name = fields.Char(
        string='Last Name',
        size=256,
        help='Last Name',
    )
    is_work = fields.Boolean(string='Work')
    is_person = fields.Boolean(
        string='Person',
        help='Check if the party is a person.',
    )
    is_school = fields.Boolean(string='School')
    is_pharmacy = fields.Boolean(
        string='Pharmacy',
        help='Check if the party is a Pharmacy',
    )
    is_insurance_company = fields.Boolean(
        string='Insurance',
        help='Check if the party is a patient',
    )
    ref = fields.Char(
        size=256,
        string='ID/SSN',
        help='Patient Social Security Number or equivalent',
    )
    patient_ids = fields.One2many(
        'medical.patient',
        fields_id='medical_center_id',
        string='Related Patients',
    )
