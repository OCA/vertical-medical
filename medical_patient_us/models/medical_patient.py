# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    social_security = fields.Char(
        string='Social Security #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'social_security', 'SSN',
        ),
        inverse=lambda s: s._inverse_identification(
            'social_security', 'SSN',
        ),
        help='Social Security Number',
    )
    driver_license_us = fields.Char(
        string='US License',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'drivers_license_us', 'DL-US',
        ),
        inverse=lambda s: s._inverse_identification(
            'drivers_license_us', 'DL-US',
        ),
        help='US Driver\s License',
    )
    passport_us = fields.Char(
        string='US Passport',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'passport_us', 'PSPRT-US',
        ),
        inverse=lambda s: s._inverse_identification(
            'passport_us', 'PSPRT-US',
        ),
        help='US Passport',
    )
