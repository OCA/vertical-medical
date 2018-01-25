# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    relationship = fields.Char(
        size=25,
    )
    relative_id = fields.Many2one(
        string='Contact',
        comodel_name='res.partner',
    )
    alias = fields.Char(
        string='Alias',
        size=256,
        help='Common name the partner is referred to as',
    )
    activation_date = fields.Date(
        string='Activation Date',
        help='Date the partner was activated',
    )
    ref = fields.Char(
        size=256,
        string='ID/SSN',
        help='Patient Social Security Number or equivalent',
    )
    patient_ids = fields.One2many(
        comodel_name='medical.patient',
        fields_id='medical_center_id',
        string='Related Patients',
    )
    is_doctor = fields.Boolean(
        string='Health Prof',
        help='Check if the partner is a health professional',
    )
    is_patient = fields.Boolean(
        string='Patient',
        help='Check if the partner is a patient',
    )
    is_work = fields.Boolean(
        string='Work',
        help='Check if the partner is a place of work',
    )
    is_person = fields.Boolean(
        string='Person',
        help='Check if the partner is a person',
    )
    is_school = fields.Boolean(
        string='School',
    )
    is_pharmacy = fields.Boolean(
        string='Pharmacy',
        help='Check if the partner is a pharmacy',
    )
    is_insurance_company = fields.Boolean(
        string='Insurance',
        help='Check if the partner is a patient',
    )
    is_institution = fields.Boolean(
        string='Institution',
        help='Check if the partner is a medical center',
    )
