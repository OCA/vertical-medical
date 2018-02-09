# -*- coding: utf-8 -*-
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
# © 2015 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'
    insurance_plan_ids = fields.One2many(
        string='Insurance Plans',
        comodel_name='medical.insurance.plan',
        inverse_name='patient_id',
        help='Past & Present Insurance Plans',
    )
