# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class MedicalPharmacy(models.Model):
    _name = 'medical.pharmacy'
    _description = 'Medical Pharmacy'
    _inherits = {'res.partner': 'partner_id', }

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
        index=True,
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals.update({
            'is_pharmacy': True,
            'customer': False,
            'is_company': True,
        })
        return super(MedicalPharmacy, self).create(vals)

    @api.multi
    def onchange_state(self, state_id):
        return self.partner_id.onchange_state(state_id)
