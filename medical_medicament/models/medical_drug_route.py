# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MedicalDrugRoute(models.Model):
    _name = 'medical.drug.route'
    _description = 'Medical Drug Route'

    name = fields.Char(required=True, translate=True)
    code = fields.Char()

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Drug Route name must be unique!'),
    ]
