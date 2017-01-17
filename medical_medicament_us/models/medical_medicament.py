# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


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
    gpi = fields.Selection(
        string='GPI',
        selection=[
            ('0', '0 (non-drug)'),
            ('1', '1 (generic)'),
            ('2', '2 (brand)'),
        ],
        default='0',
        help='Generic Product Identifier for medicament.',
    )
    control_code = fields.Selection(
        string='Control Code',
        selection=[
            ('0', 'Not Controlled'),
            ('1', 'C1'),
            ('2', 'C2'),
            ('3', 'C3'),
            ('4', 'C4'),
            ('5', 'C5'),
        ],
        help=(
            '** DEA Control Codes **\n\n'
            'CODE 0: Not controlled. \n\n'
            'CODE 1: Has no currently accepted medical use '
            'in the United States, a lack of accepted safety '
            'for use under medical supervision, and a high '
            'potential for abuse e.g. Heroin, Marijuana, etc.\n\n'
            'CODE 2: Has a high potential for abuse which may lead '
            'to severe psychological or physical dependence e.g. '
            'Morphine, Opium, Codeine, etc.\n\n'
            'CODE 3: Has a potential for abuse lower than code 1 '
            'or 2. Abuse can lead to moderate or low physical '
            'dependence or high psychological dependence e.g. '
            'combination products with less than 15mg of '
            'Hydrocodone per dosage unit (Vicodin), products '
            'not containing more than 90mg of Codeine per dosage unit '
            '(Tylenol with Codeine), and Buprenorphine (Suboxone).\n\n'
            'CODE 4: Low potential for abuse relative to code 3. '
            'Examples include: Alprazolam (Xanax), Carisoprodol (Soma), '
            'Clonazepam (Klonopin), Clorazepate (Tranxene), Diazepam '
            '(Valium), Lorazepam (Ativan), Midazolam (Versed), '
            'Temazepam (Restoril), and Triazolam (Halcion).\n\n'
            'CODE 5: Low potential for abuse relative to code 4, and '
            'consists primarily of preparations containing limited quantities '
            'of certain narcotics. Examples include: cough preparations '
            'containing no more than 200mg of Codeine per 100ml or per 100g '
            '(Robitussin AC, Phenergan with Codeine), and Ezogabine.'
        ),
    )
    brand_ids = fields.Many2many(
        string='Branded Medicaments',
        help='List of all brand-name medicaments equivalent to this one',
        compute='_compute_brand_ids',
        comodel_name='medical.medicament',
    )
    generic_ids = fields.Many2many(
        string='Generic Medicaments',
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
