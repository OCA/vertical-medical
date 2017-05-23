# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api
from odoo.exceptions import UserError


class MedicalPractitioner(models.Model):
    _name = 'medical.practitioner'
    _description = 'Medical Practitioner'
    _inherit = 'medical.abstract.entity'

    login_user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        readonly=True
    )

    role_ids = fields.Many2many(
        string='Roles',
        comodel_name='medical.role',
        relation='medical_practitioner_role',
        column1='practitioner_id',
        column2='role_id'
    )

    @api.constrains('user_id')
    def _no_duplicates(self):
        if self.env[MedicalPractitioner].search([('user_id', '=', self.user_id)]).__len__() > 1:
            raise UserError('User must be unique')
