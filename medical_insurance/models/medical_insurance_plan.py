# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


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
    )
    number = fields.Char(
        required=True,
        help='Identification number for insurance account',
    )
    member_since = fields.Date(
        string='Member Since',
    )
    member_exp = fields.Date(
        string='Expiration Date',
    )
