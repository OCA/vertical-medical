# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MedicalMedicamentAttribute(models.Model):
    _name = 'medical.medicament.attribute'
    name = fields.Char(
        help="Full Name of Attribute",
        required=True,
    )
    code = fields.Char(
        help="Short Code of Attribute",
    )
    attribute_type_id = fields.Many2one(
        string='Attribute Type',
        comodel_name='medical.medicament.attribute.type',
        required=True,
    )
    medicament_ids = fields.Many2many(
        string='Medicaments',
        comodel_name='medical.medicament',
    )
    parent_id = fields.Many2one(
        string='Parent',
        comodel_name='medical.medicament.attribute',
        domain="[('attribute_type_id', '=', attribute_type_id)]",
    )
    child_ids = fields.One2many(
        string='Children',
        comodel_name='medical.medicament.attribute',
        inverse_name='parent_id',
        domain="[('attribute_type_id', '=', attribute_type_id)]",
    )
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name, attribute_type_id)',
         'Attribute name must be unique per category.'),
    ]
