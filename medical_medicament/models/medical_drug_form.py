# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MedicalDrugForm(models.Model):
    _name = 'medical.drug.form'
    _description = 'Medical Drug Form'

    name = fields.Char(
        required=True,
        translate=True,
    )
    code = fields.Char()

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Drug form must be unique!'),
    ]
