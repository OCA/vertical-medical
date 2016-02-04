# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalMedicament(models.Model):
    _inherit = 'medical.medicament'
    ndc = fields.Char(
        string='NDC',
        help='National Drug Code for medication'
    )
    control_code = fields.Selection([
        ('c1', 'C1'),
        ('c2', 'C2'),
        ('c3', 'C3'),
        ('c4', 'C4'),
        ('c5', 'C5'),
    ],
        help='Federal drug scheduling code',
    )
