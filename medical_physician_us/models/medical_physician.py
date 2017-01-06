# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MedicalPhysician(models.Model):
    _inherit = 'medical.physician'

    license_num = fields.Many2one(
        string='State License #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'license_num', 'ST-LIC',
        ),
        context=lambda s: s._context_identification(
            'license_num', 'ST-LIC',
        ),
        help='State medical license #',
    )
    dea_num = fields.Many2one(
        string='DEA #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'dea_num', 'DEA',
        ),
        context=lambda s: s._context_identification(
            'dea_num', 'DEA',
        ),
        help='Drug Enforcement Agency #',
    )
    npi_num = fields.Many2one(
        string='NPI #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'npi_num', 'NPI',
        ),
        context=lambda s: s._context_identification(
            'npi_num', 'NPI',
        ),
        help="National Provider Identifier",
    )
