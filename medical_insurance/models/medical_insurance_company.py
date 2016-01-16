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


class MedicalInsuranceCompany(models.Model):
    _name = 'medical.insurance.company'
    _description = 'Medical Insurance Providers'
    _inherits = {'res.partner': 'partner_id', }
    partner_id = fields.Many2one(
        string='Related Partner',
        comodel_name='res.partner',
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_insurance_company'] = True
        return super(MedicalInsuranceCompany, self).create(vals)
