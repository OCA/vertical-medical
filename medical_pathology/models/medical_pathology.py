# -*- coding: utf-8 -*-
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class MedicalPathology(models.Model):
    _name = 'medical.pathology'
    _description = 'Medical Pathology'

    name = fields.Char(
        required=True,
        translate=True,
    )
    code = fields.Char(
        required=True,
    )
    code_type_id = fields.Many2one(
        string='Code Type',
        comodel_name='medical.pathology.code.type',
        index=True,
    )
    notes = fields.Text(
        translate=True,
    )
    category_id = fields.Many2one(
        string='Category of Pathology',
        comodel_name='medical.pathology.category',
        domain="[('code_type_id', '=', code_type_id)]",
        index=True,
    )
    child_ids = fields.One2many(
        string='Children Pathologies',
        comodel_name='medical.pathology',
        inverse_name='parent_id',
        domain="[('code_type_id', '=', code_type_id)]",
    )
    parent_id = fields.Many2one(
        string='Parent Pathology',
        comodel_name='medical.pathology',
        domain="[('code_type_id', '=', code_type_id)]",
        index=True,
    )

    _sql_constraints = [
        ('code_and_type_uniq',
         'UNIQUE(code, code_type_id)',
         'Pathology codes must be unique per code type.'),
    ]

    @api.multi
    @api.constrains('parent_id')
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_(
                'You are attempting to create a recursive pathology.'
            ))
