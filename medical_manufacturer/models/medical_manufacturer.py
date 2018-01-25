# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, fields, models


class MedicalManufacturer(models.Model):
    _name = 'medical.manufacturer'
    _description = 'Medical Manufacturer'
    _inherits = {'res.partner': 'partner_id', }

    partner_id = fields.Many2one(
        string='Partner',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
        index=True,
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals.update({
            'is_manufacturer': True,
            'customer': False,
            'is_company': True,
        })
        return super(MedicalManufacturer, self).create(vals)
