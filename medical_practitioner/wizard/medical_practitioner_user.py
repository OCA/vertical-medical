# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api


class MedicalPractitionerUserWizard(models.TransientModel):
    _name = 'medical.practitioner.user.wizard'

    def _default_practitioner(self):
        return self.env['medical.practitioner'].browse(self._context.get('active_id'))

    login = fields.Char(
        string='login',
        required=True
    )
    email = fields.Char(
        required=True
    )
    login_user_id = fields.Many2one(
        comodel_name='res.users',
        string='Base user',
        help='Used in order to copy permissions',
        required=True
    )
    practitioner_id = fields.Many2one(
        comodel_name='medical.practitioner',
        string='Practitioner',
        default=_default_practitioner,
        required=True
    )

    @api.one
    def create_user(self):
        self.ensure_one()
        if self.practitioner_id.login_user_id:
            return self.practitioner_id.login_user_id
        sudo_user = self.env['res.users'].sudo()
        values = {
            'login': self.login,
            'active': True,
            'partner_id': self.practitioner_id.partner_id.id
        }
        user = sudo_user.browse(self.login_user_id.id).copy(default=values)
        self.practitioner_id.write({
            'login_user_id': user.id,
            'email': self.email
        })
        return user
