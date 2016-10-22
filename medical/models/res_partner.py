# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


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

    @api.multi
    @api.constrains('birthdate_date')
    def _check_birthdate_date(self):
        """ It will not allow birth dates in the future. """
        now = datetime.now()
        for record in self:
            if not record.birthdate_date:
                continue
            birthdate = fields.Datetime.from_string(record.birthdate_date)
            if birthdate > now:
                raise ValidationError(_(
                    'Patients cannot be born in the future.',
                ))

    @api.model
    def create(self, vals):
        """ It overrides create to bind appropriate medical entity. """
        if all((
            vals.get('type', '').startswith('medical.'),
            not self.env.context.get('medical_entity_no_create'),
        )):
            model = self.env[vals['type']].with_context(
                medical_entity_no_create=True,
            )
            medical_entity = model.create(vals)
            return medical_entity.partner_id
        return super(ResPartner, self).create(vals)
