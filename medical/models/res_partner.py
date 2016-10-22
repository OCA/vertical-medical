# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    relationship = fields.Char(
        'Relationship',
        size=25,
    )
    is_institution = fields.Boolean(
        string='Institution',
        help='Check if the party is a Medical Center',
    )
    relative_id = fields.Many2one(
        string='Contact',
        comodel_name='res.partner',
    )
    is_doctor = fields.Boolean(
        string='Health Prof',
        help='Check if the party is a health professional',
    )
    is_patient = fields.Boolean(
        string='Patient',
        help='Check if the party is a patient',
    )
    alias = fields.Char(
        string='Alias',
        size=256,
        help='Common name that the Party is reffered',
    )
    activation_date = fields.Date(
        string='Activation date',
        help='Date of activation of the party',
    )
    last_name = fields.Char(
        string='Last Name',
        size=256,
        help='Last Name',
    )
    is_work = fields.Boolean(string='Work')
    is_person = fields.Boolean(
        string='Person',
        help='Check if the party is a person.',
    )
    is_school = fields.Boolean(string='School')
    is_pharmacy = fields.Boolean(
        string='Pharmacy',
        help='Check if the party is a Pharmacy',
    )
    is_insurance_company = fields.Boolean(
        string='Insurance',
        help='Check if the party is a patient',
    )
    ref = fields.Char(
        size=256,
        string='ID/SSN',
        help='Patient Social Security Number or equivalent',
    )
    patient_ids = fields.One2many(
        'medical.patient',
        inverse_name='partner_id',
        string='Related Patients',
    )
