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


class MedicalInsuranceTemplate(models.Model):
    _name = 'medical.insurance.template'
    _description = 'Medical Insurance Templates'
    _inherits = {'product.product': 'product_id', }

    name = fields.Char(
        required=True,
        readonly=True,
        compute='_compute_name',
        help='Insurance Plan Name',
    )
    code = fields.Char(
        required=True,
        help='Insurance Plan template code',
    )
    description = fields.Char(
        required=True,
        help='Insurance Plan template description',
    )
    plan_number = fields.Char(
        required=False,
        help='Identification number for plan',
    )
    is_default = fields.Boolean(
        string='Default Plan',
        help='Check this if the plan should be the default when assigning '
        'company to patient',
    )
    insurance_company_id = fields.Many2one(
        string='Insurance Provider',
        comodel_name='medical.insurance.company',
        help='Insurance Provider',
        required=True,
    )
    notes = fields.Text(
        string='Extra Info',
        help='Additional Information',
    )
    product_id = fields.Many2one(
        string='Insurance Product',
        comodel_name='product.product',
        required=True,
        ondelete='cascade',
    )
    insurance_affiliation = fields.Selection([
        ('state', 'State'),
        ('labor_union', 'Labor Union / Syndical'),
        ('private', 'Private'),
    ],
        help='What type of entity is this insurance provided to?',
    )

    @api.multi
    @api.depends('insurance_company_id', 'code')
    def _compute_name(self):
        for rec in self:
            rec.name = '[%s] %s' % (rec.insurance_company_id.name, rec.code)

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_insurance_plan'] = True
        return super(MedicalInsuranceTemplate, self).create(vals)
