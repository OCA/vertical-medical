# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPathologyGroup(models.Model):
    _name = 'medical.pathology.group'
    _description = 'Medical Pathology Group'
    _sql_constraints = [
        ('code', 'UNIQUE(code)', 'Pathology group codes must be unique.'),
    ]

    name = fields.Char(required=True, translate=True)
    notes = fields.Text(translate=True)
    code = fields.Char(
        required=True,
        help='For example MDG6 code will contain the Millennium Development'
        ' Goals #6 diseases: Tuberculosis, Malaria and HIV/AIDS',
    )
    description = fields.Text(
        string='Short Description',
        required=True,
        translate=True,
    )
