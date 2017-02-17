# -*- coding: utf-8 -*-
# Copyright 2012-2013 Federico Manuel Echeverri Choux
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models


class MedicalPatient(models.Model):
    _inherit = "medical.patient"

    lab_test_ids = fields.One2many(
        string='Lab Tests',
        comodel_name='medical.lab.patient',
        inverse_name='patient_id',
    )
