# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    type = fields.Selection(selection_add=[
        ('medical.patient', 'Medical Patient'),
    ])
    alias = fields.Char(
        string='Alias',
        help='Common name that the Party is referred',
    )
    patient_ids = fields.One2many(
        string='Related Patients',
        comodel_name='medical.patient',
        inverse_name='partner_id',
    )

    @api.model
    def create(self, vals):
        """ It overloads create to bind appropriate medical entity """
        try:
            if all((
                vals['type'].startswith('medical.'),
                not self.env.context.get('medical_entity_no_create'),
            )):
                model = self.env[vals['type']].with_context(
                    medical_entity_no_create=True,
                )
                medical_entity = model.create(vals)
                return medical_entity.partner_id
        except (AttributeError, KeyError):
            pass
        return super(ResPartner, self).create(vals)
