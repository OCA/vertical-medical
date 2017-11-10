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

from odoo import api, fields, models


class MedicalInsurancePlan(models.Model):
    _name = 'medical.insurance.plan'
    _description = 'Medical Insurance Providers'
    _inherits = {'medical.insurance.template': 'insurance_template_id', }

    insurance_template_id = fields.Many2one(
        string='Plan Template',
        comodel_name='medical.insurance.template',
        required=True,
        ondelete='cascade',
        help='Insurance Plan Template',
    )
    patient_id = fields.Many2one(
        'medical.patient',
        string='Patient',
        required=True,
    )
    number = fields.Char(
        required=False,
        help='Identification number for insurance account',
    )
    member_since = fields.Date(
        string='Member Since',
    )
    member_exp = fields.Date(
        string='Expiration Date',
    )
    active = fields.Boolean(
        default=True,
    )

    @api.multi
    def name_get(self):
        result = []
        for plan in self.sudo():
            name = '%s %s' % (plan.name, plan.patient_id.name)
            result.append((plan.id, name))
        return result
