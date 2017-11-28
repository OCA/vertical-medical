# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalInsurancePlan(models.Model):
    _name = 'medical.insurance.plan'
    _description = 'Medical Insurance Plans'

    name = fields.Char(
        related='insurance_template_id.name',
        stored=True,
        readonly=True,
        required=False,
    )
    insurance_template_id = fields.Many2one(
        string='Plan Template',
        comodel_name='medical.insurance.template',
        required=True,
        ondelete='restrict',
        help='Insurance Plan Template',
    )
    patient_id = fields.Many2one(
        'medical.patient',
        string='Patient',
        required=True,
        ondelete='restrict',
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
    notes = fields.Text(
        string='Extra Info',
        help='Additional Information',
    )

    plan_number = fields.Char(
        related='insurance_template_id.plan_number',
        stored=True,
        readonly=True,
    )
    product_id = fields.Many2one(
        related='insurance_template_id.product_id',
        stored=True,
        readonly=True,
    )
    insurance_company_id = fields.Many2one(
        related='insurance_template_id.insurance_company_id',
        stored=True,
        readonly=True,
    )
    insurance_affiliation = fields.Selection(
        related='insurance_template_id.insurance_affiliation',
        stored=True,
        readonly=True,
    )
