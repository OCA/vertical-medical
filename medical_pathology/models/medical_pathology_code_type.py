# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import models, fields


class MedicalPathologyCodeType(models.Model):
    _name = 'medical.pathology.code.type'
    _description = 'Medical Pathology Code Type'

    name = fields.Char(
        required=True,
    )
