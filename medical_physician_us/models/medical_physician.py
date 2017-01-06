# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MedicalPhysician(models.Model):
    _inherit = 'medical.physician'

    license_num = fields.Char(
        string='State License #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'license_num', 'ST-LIC',
        ),
        inverse=lambda s: s._inverse_identification(
            'license_num', 'ST-LIC',
        ),
        help='State medical license #',
    )
    dea_num = fields.Char(
        string='DEA #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'dea_num', 'DEA',
        ),
        inverse=lambda s: s._inverse_identification(
            'dea_num', 'DEA',
        ),
        help='Drug Enforcement Agency #',
    )
    npi_num = fields.Char(
        string='NPI #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'npi_num', 'NPI',
        ),
        inverse=lambda s: s._inverse_identification(
            'npi_num', 'NPI',
        ),
        help="National Provider Identifier",
    )
