# -*- coding: utf-8 -*-
# Copyright 2015-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MedicalInsuranceTemplate(models.Model):
    _name = 'medical.insurance.template'
    _description = 'Medical Insurance Templates'
    _inherits = {'product.product': 'product_id'}
    plan_number = fields.Char(
        required=True,
        help='Identification number for plan',
    )
    is_default = fields.Boolean(
        string='Default Plan',
        help='Check this if the plan should be the default when assigning'
        'company to patient',
    )
    insurance_company_id = fields.Many2one(
        string='Insurance Provider',
        comodel_name='medical.insurance.company',
        help='Insurance Provider',
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
        help='What type of entity is this insurance provided to?'
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_insurance_plan'] = True
        return super(MedicalInsuranceTemplate, self).create(vals)

    @api.multi
    @api.depends('product_id.name',
                 'insurance_company_id.name',
                 'plan_number',
                 )
    def name_get(self):
        result = []
        for record in self:
            name = "%s (%s #%s)" % (
                record.product_id.name,
                record.insurance_company_id.name,
                record.plan_number,
            )
            result.append((record.id, name))
        return result
