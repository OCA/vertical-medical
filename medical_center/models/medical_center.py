# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class MedicalCenter(models.Model):
    _name = 'medical.center'
    _description = 'Medical Center'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
        index=True,
    )

    @api.model
    def create(self, vals):
        vals.update({
            'is_company': True,
            'customer': False,
            'type': self._name,
        })
        return super(MedicalCenter, self).create(vals)
