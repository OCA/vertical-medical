# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import fields, models


class MedicalMedicamentGcn(models.Model):
    _name = 'medical.medicament.gcn'
    _description = 'Medical Medicament GCN'

    name = fields.Char(
        string='GCN',
        help='Generic Code Number',
    )
    medicament_ids = fields.One2many(
        string='Medicament',
        comodel_name='medical.medicament',
        inverse_name='gcn_id',
    )
