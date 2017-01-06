# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    social_security = fields.Many2one(
        string='Social Security #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'social_security', 'SSN',
        ),
        help='Social Security Number',
    )
    driver_license_us = fields.Many2one(
        string='US License',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'drivers_license_us', 'DL-US',
        ),
        help='US Driver\s License',
    )
    passport_us = fields.Many2one(
        string='US Passport',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'drivers_license_us', 'DL-US',
        ),
        help='US Passport',
    )
