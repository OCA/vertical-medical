# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class MedicalPathologyCategory(models.Model):
    _name = 'medical.pathology.category'
    _description = 'Medical Pathology Category'

    name = fields.Char(
        required=True,
        translate=True
    )
    child_ids = fields.One2many(
        string='Children Categories',
        comodel_name='medical.pathology.category',
        inverse_name='parent_id',
    )
    parent_id = fields.Many2one(
        string='Parent Category',
        comodel_name='medical.pathology.category',
        index=True,
    )

    @api.multi
    @api.constrains('parent_id')
    def _check_recursion_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_(
                'Error! You are attempting to create a recursive category.'
            ))
