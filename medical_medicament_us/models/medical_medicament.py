# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


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
        ('0', 'Not Controlled'),
        ('1', 'C1'),
        ('2', 'C2'),
        ('3', 'C3'),
        ('4', 'C4'),
        ('5', 'C5'),
    ],
        help='Federal drug scheduling code for medicament.',
    )
    brand_ids = fields.Many2many(
        help='List of all brand-name medicaments equivalent to this one',
        compute='_compute_brand_ids',
        comodel_name='medical.medicament',
    )
    generic_ids = fields.Many2many(
        help='List of all generic medicaments equivalent to this one',
        compute='_compute_generic_ids',
        comodel_name='medical.medicament',
    )

    @api.multi
    def _compute_brand_ids(self):
        for record in self:
            record.brand_ids = self.search([
                ('gcn_id.id', '=', record.gcn_id.id),
                ('gpi', '=', '2'),
            ])

    @api.multi
    def _compute_generic_ids(self):
        for record in self:
            record.generic_ids = self.search([
                ('gcn_id.id', '=', record.gcn_id.id),
                ('gpi', '=', '1'),
            ])
