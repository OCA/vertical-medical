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
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, models


class MedicalInsuranceCompany(models.Model):
    _name = 'medical.insurance.company'
    _description = 'Medical Insurance Providers'
    _inherit = 'medical.abstract.entity'

    insurance_template_ids = fields.One2many(
        comodel_name='medical.insurance.template',
        string='Plan templates',
        inverse_name='insurance_company_id',
    )
