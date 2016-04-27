# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models
from openerp.exceptions import ValidationError


class MedicalMedicamentAttribute(models.Model):
    _name = 'medical.medicament.attribute'
    name = fields.Char(
        help="Full Name of Attribute"
    )
    code = fields.Char(
        help="Short Code of Attribute"
    )
    category = fields.Selection([
        ('clarity', 'Clarity'),
        ('coating', 'Coating'),
        ('color', 'Color'),
        ('flavor', 'Flavor'),
        ('score', 'Score'),
        ('shape', 'Shape'),
    ])
    medicament_ids = fields.Many2many(
        string='Medicaments',
        comodel_name='medical.medicament',
    )
    _sql_constraints = [
        ('code_uniq', 'UNIQUE(category, code)',
         'Attribute code must be unique per category.'),
        ('name_uniq', 'UNIQUE(category, name)',
         'Attribute name must be unique per category.'),
    ]
