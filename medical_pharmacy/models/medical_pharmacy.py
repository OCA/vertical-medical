# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class MedicalPharmacy(models.Model):
    """
    Medical pharmacy attributes on res.partner
    """
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
