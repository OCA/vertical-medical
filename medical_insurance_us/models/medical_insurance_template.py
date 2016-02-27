# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalInsuranceTemplate(models.Model):
    _inherit = 'medical.insurance.template'
    group_number = fields.Char(
        required=True,
    )
    rx_bin = fields.Char(
        required=True,
        help='RX BIN Number',
    )
    rx_pcn = fields.Char(
        required=True,
        help='RX Processor Control Number (PCN)',
    )
    rx_group = fields.Char(
        required=True,
        help='RX Group Number',
    )
    insurance_type = fields.Selection([
        ('ppo', 'PPO'),
        ('hmo', 'HMO'),
        ('fsa', 'FSA'),
    ],
        required=True,
    )
    insurance_affiliation = fields.Selection(selection_add=[
        ('medicaid', 'Medicaid'),
        ('employer', 'Employer'),
    ])
