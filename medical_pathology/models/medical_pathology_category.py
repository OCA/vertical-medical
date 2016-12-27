# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models, _
from openerp.exceptions import ValidationError


class MedicalPathologyCategory(models.Model):
    _name = 'medical.pathology.category'
    _description = 'Medical Pathology Category'

    name = fields.Char(
        required=True,
        translate=True,
    )
    notes = fields.Text(
        translate=True,
    )
    child_ids = fields.One2many(
        string='Children Categories',
        comodel_name='medical.pathology.category',
        inverse_name='parent_id',
        domain="[('code_type_id', '=', code_type_id)]",
    )
    parent_id = fields.Many2one(
        string='Parent Category',
        comodel_name='medical.pathology.category',
        domain="[('code_type_id', '=', code_type_id)]",
        index=True,
    )
    code_type_id = fields.Many2one(
        string='Code Type',
        comodel_name='medical.pathology.code.type',
        index=True,
    )

    @api.multi
    @api.constrains('parent_id')
    def _check_recursion_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_(
                'Error! You are attempting to create a recursive category.'
            ))
