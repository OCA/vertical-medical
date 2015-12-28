# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
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

from openerp import fields, models, api


class MedicalInsuranceTemplate(models.Model):
    _name = 'medical.insurance.template'
    _inherits = {'product.product': 'product_id', }
    name = fields.Char(
        required=True,
        help='Insurance Plan Name',
    )
    plan_number = fields.Char(
        required=True,
    )
    is_default = fields.Boolean(
        string='Default Plan',
        help='Check this if the plan should be the default when assigning'
        'company to patient',
    )
    insurance_company_id = fields.Many2one(
        string='Insurance Company',
        comodel_name='medical.insurance.company',
    )
    notes = fields.Text(
        string='Extra Info',
    )
    product_id = fields.Many2one(
        string='Insurance Product',
        comodel_name='product.product',
    )
    insurance_affiliation = fields.Selection([
        ('state', 'State'),
        ('labor_union', 'Labor Union / Syndical'),
        ('private', 'Private'),
    ],
        help='What type of entity is this insurance provided to?'
    )


    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_insurance_plan'] = True
        return super(MedicalInsuranceTemplate, self).create(vals)
