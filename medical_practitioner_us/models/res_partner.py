# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html)

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    license_num = fields.Char(
        string='State License #',
        compute=lambda s: s._compute_identification(
            'license_num', 'ST-LIC',
        ),
        inverse=lambda s: s._inverse_identification(
            'license_num', 'ST-LIC',
        ),
        search=lambda s, *a: s._search_identification(
            'ST-LIC', *a
        ),
        help='State Medical License Number - '
             'constraints vary by type of license',
    )
    dea_num = fields.Char(
        string='DEA #',
        compute=lambda s: s._compute_identification(
            'dea_num', 'DEA',
        ),
        inverse=lambda s: s._inverse_identification(
            'dea_num', 'DEA',
        ),
        search=lambda s, *a: s._search_identification(
            'DEA', *a
        ),
        help='Drug Enforcement Agency Number - '
             '2 alpha characters and 7 digits',
    )
    npi_num = fields.Char(
        string='NPI',
        compute=lambda s: s._compute_identification(
            'npi_num', 'NPI',
        ),
        inverse=lambda s: s._inverse_identification(
            'npi_num', 'NPI',
        ),
        search=lambda s, *a: s._search_identification(
            'NPI', *a
        ),
        help='National Provider Identifier - 10 digits',
    )
