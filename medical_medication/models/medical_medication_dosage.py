# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class MedicalMedicationDosage(models.Model):
    _name = 'medical.medication.dosage'
    _description = 'Medical Medication Dosage'

    name = fields.Char(
        required=True,
        translate=True,
    )
    abbreviation = fields.Char(
        help='Dosage abbreviation, such as tid in the US or tds in the UK',
    )
    code = fields.Char(
        help='Dosage Code, for example: SNOMED 229798009 = 3 times per day',
    )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]

    @api.multi
    @api.constrains('abbreviation')
    def _check_abbreviation_unique(self):
        for rec_id in self:
            if rec_id.abbreviation:
                domain = [('abbreviation', '=', rec_id.abbreviation)]
                res = self.search(domain)
                if len(res) > 1:
                    raise ValidationError(_(
                        'This abbreviation is already in use by %s' % (
                            res[0].name
                        ),
                    ))

    @api.multi
    @api.constrains('code')
    def _check_code_unique(self):
        for rec_id in self:
            if rec_id.code:
                domain = [('code', '=', rec_id.code)]
                res = self.search(domain)
                if len(res) > 1:
                    raise ValidationError(_(
                        'This code is already in use by %s' % res[0].name,
                    ))
