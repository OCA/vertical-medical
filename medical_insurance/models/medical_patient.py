# -*- coding: utf-8 -*-
# Copyright 2015-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'
    insurance_plan_ids = fields.One2many(
        string='Insurance Plans',
        comodel_name='medical.insurance.plan',
        inverse_name='patient_id',
        help='Past & Present Insurance Plans',
    )
