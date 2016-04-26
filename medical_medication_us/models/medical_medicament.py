# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalMedicament(models.Model):
    _inherit = 'medical.medicament'
    ndc_ids = fields.One2many(
        string='NDCs',
        comodel_name='medical.medicament.ndc',
        inverse_name='medicament_id',
        ondelete='cascade',
        help='National Drug Codes for medicament.',
    )
    gcn_id = fields.Many2one(
        string='GCN',
        comodel_name='medical.medicament.gcn',
        help='Generic Code Number for medicament.',
    )
    gpi = fields.Selection([
        ('0', '0 (non-drug)'),
        ('1', '1 (generic)'),
        ('2', '2 (brand)'),
    ],
        string='GPI',
        default='0',
        help='Generic Product Identifier for medicament.',
    )
    control_code = fields.Selection([
        ('1', 'C1'),
        ('2', 'C2'),
        ('3', 'C3'),
        ('4', 'C4'),
        ('5', 'C5'),
    ],
        help='Federal drug scheduling code for medicament.',
    )
