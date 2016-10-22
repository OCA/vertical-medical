# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalInsuranceCompany(models.Model):
    _name = 'medical.insurance.company'
    _description = 'Medical Insurance Providers'
    _inherits = {'res.partner': 'partner_id', }
    partner_id = fields.Many2one(
        string='Related Partner',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_insurance_company'] = True
        return super(MedicalInsuranceCompany, self).create(vals)
