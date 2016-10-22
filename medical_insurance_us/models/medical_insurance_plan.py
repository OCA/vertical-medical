# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MedicalInsurancePlan(models.Model):
    _inherit = 'medical.insurance.plan'
    person_num = fields.Integer('Person Number')
