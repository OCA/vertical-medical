# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################

from openerp import fields, models


class MedicalInsurance(models.Model):
    _name = 'medical.insurance'

    def _compute_name(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = record.company.name
        return res

    name = fields.Char(
        compute='_compute_name',
        string='Name',
        help="",
    )
    company_id = fields.Many2one(
        'res.partner',
        string='Insurance Company',
        required=True,
    )
    patient_id = fields.Many2one(
        'medical.patient',
        string='Patient',
    )
    plan_id = fields.Many2one(
        'medical.insurance.plan',
        string='Plan',
        help='Insurance plan name'
    )
    insurance_type = fields.Selection([
        ('state', 'State'),
        ('labour_union', 'Labour Union / Syndical'),
        ('private', 'Private'),
    ],)
    number = fields.Char(
        required=True,
    )
    member_since = fields.Date(
        string='Member Since',
    )
    member_exp = fields.Date(
        string='Expiration Date',
    )
    notes = fields.Text(
        string='Extra Info',
    )
    owner_id = fields.Many2one(
        'res.partner',
        string='Owner',
    )

MedicalInsurance()
