# -*- coding: utf-8 -*-
# Copyright 2012-2013 Federico Manuel Echeverri Choux
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalLabTestResult(models.Model):

    _name = 'medical.lab.test.result'
    _description = 'Medical Lab Test Results'
    _order = 'sequence'
    _inherits = {'medical.lab.test.criterion': 'criterion_id'}

    criterion_id = fields.Many2one(
        string='Criterion',
        comodel_name='medical.lab.test.criterion',
        required=True,
        ondelete='restrict',
        domain="[('test_type_ids', '=', lab_id.test_type_id)]",
    )
    result_actual = fields.Char(
        string='Result',
    )
    lab_id = fields.Many2one(
        string='Lab',
        comodel_name='medical.lab',
        required=True,
    )
    sequence = fields.Integer(
        default=5,
        required=True,
    )
    notes = fields.Text()
