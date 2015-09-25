# -*- coding: utf-8 -*-
###############################################################################
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
###############################################################################

from openerp import fields, models


class MedicalInsurancePlan(models.Model):
    _name = 'medical.insurance.plan'

    name = fields.Char(
        required=True,
        help='Insurance plan name',
    )
    is_default = fields.Boolean(
        string='Default Plan',
        help='Check if this is the default plan when assigning this'
        ' insurance company to a patient',   
    )
    company_id = fields.Many2one(
        'res.partner',
        string='Insurance Company',
        required=True,
    )
    notes = fields.Text(
        string='Extra Info',
    )
    plan_id = fields.Many2one(
        'product.product',
        string='Plan',
    )

MedicalInsurancePlan()
