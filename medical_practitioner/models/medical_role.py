# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields


class MedicalRole(models.Model):
    _name = 'medical.role'
    _description = 'Practitioner Roles'

    name = fields.Char(
        required=True
    )

    description = fields.Char(
        required=True
    )
