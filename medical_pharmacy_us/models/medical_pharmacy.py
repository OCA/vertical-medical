# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MedicalPharmacy(models.Model):
    _inherit = 'medical.pharmacy'

    nabp_num = fields.Many2one(
        string='NAPB #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'napb_num', 'NAPB',
        ),
        help='National Boards of Pharmacy Id #',
    )
    medicaid_num = fields.Many2one(
        string='Medicaid #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'medicaid_num', 'MEDICAID',
        ),
        help='Medicaid Id #',
    )
    npi_num = fields.Many2one(
        string='NPI #',
        comodel_name='res.partner.id_number',
        compute=lambda s: s._compute_identification(
            'npi_num', 'NPI',
        ),
        help="National Provider Identifier",
    )
