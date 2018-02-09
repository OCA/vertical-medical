# -*- coding: utf-8 -*-
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
# © 2015 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import fields, models, api


class MedicalInsuranceTemplate(models.Model):
    _name = 'medical.insurance.template'
    _description = 'Medical Insurance Templates'
    _inherits = {'product.product': 'product_id', }
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
