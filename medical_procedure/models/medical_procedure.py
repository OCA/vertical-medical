# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo import fields, models


class MedicalProcedure(models.Model):
    _name = 'medical.procedure'

    name = fields.Char(
        required=True,
        help='Name of procedure, such as "Behavioral therapy"',
    )
    code = fields.Char(
        help='Short name or code for procedure',
        required=True,
    )
    description = fields.Text()
    active = fields.Boolean(
        default=True,
    )
