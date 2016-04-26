# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MedicalMedicamentGcn(models.Model):
    _name = 'medical.medicament.gcn'
    _description = 'Medical Medicament GCN'

    gcn = fields.Char(
        string='GCN',
        help='Generic Code Number',
    )
    medicament_id = fields.Many2one(
        string='Medicament',
        comodel_name='medical.medicament',
    )
