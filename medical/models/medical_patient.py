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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################
from openerp import models, fields, api
from datetime import datetime
from openerp.tools.translate import _
from dateutil.relativedelta import relativedelta


class MedicalPatient(models.Model):
    '''
    The concept of Patient included in medical.
    '''
    _name = 'medical.patient'
    _description = 'Medical Patient'
    _inherits = {'res.partner': 'partner_id', }

    @api.one
    def _compute_age(self):
        """
        age computed depending of the birth date of the
        membership request
        """
        now = datetime.now()
        if self.dob:
            dob = fields.Datetime.from_string(self.dob)

            if self.deceased:
                dod = fields.Datetime.from_string(self.dod)
                delta = relativedelta(dod, dob)
                deceased = _(' (deceased)')
            else:
                delta = relativedelta(now, dob)
                deceased = ''
            years_months_days = str(delta.years) + _('y ') + str(
                delta.months) + _('m ') + str(delta.days) + _('d')\
                + deceased
        else:
            years_months_days = _('No DoB !')
        self.age = years_months_days

    @api.one
    def action_invalidate(self):
        self.active = False
        self.partner_id.active = False
        self.dod = fields.Datetime.now()

    age = fields.Char(compute='_compute_age')
    identification_code = fields.Char(
        string='Internal Identification',
        help='Patient Identifier provided by the Health Center.'
        '(different from the Social Security Number)')
    general_info = fields.Text(string='General Information')
    dob = fields.Date(string='Date of Birth')
    dod = fields.Datetime(string='Deceased Date')
    active = fields.Boolean(default=True)
    deceased = fields.Boolean()
    partner_id = fields.Many2one(
        comodel_name='res.partner', required=True, ondelete='cascade',
        index=True)
    gender = fields.Selection(
        selection=[
            ('m', 'Male'),
            ('f', 'Female'),
        ])
    medical_center_id = fields.Many2one(
        comodel_name='res.partner', domain="[('is_institution', '=', True)]",
        string='Medical Center')
    marital_status = fields.Selection(
        selection=[
            ('s', 'Single'),
            ('m', 'Married'),
            ('w', 'Widowed'),
            ('d', 'Divorced'),
            ('x', 'Separated'),
            ('z', 'law marriage'),
        ])

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_patient'] = True
        if not vals.get('identification_code'):
            sequence = self.env['ir.sequence'].get('medical.patient')
            vals['identification_code'] = sequence
        return super(MedicalPatient, self).create(vals)
