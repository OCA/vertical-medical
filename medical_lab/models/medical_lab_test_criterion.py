# -*- coding: utf-8 -*-
# Copyright 2012-2013 Federico Manuel Echeverri Choux
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import fields, models


class MedicalLabTestCriterion(models.Model):

    _name = 'medical.lab.test.criterion'
    _description = 'Medical Lab Test Criteria'
    _order = 'sequence'

    name = fields.Char(
        string='Test Name',
        size=128,
        required=True,
    )
    description = fields.Text()
    result_expect = fields.Char(
        string='Normal Range',
    )
    uom_id = fields.Many2one(
        string='Unit of Measure',
        comodel_name='product.uom',
    )
    test_type_ids = fields.Many2many(
        string='Test Types',
        comodel_name='medical.lab.test.type',
        ondelete='restrict',
        help='This criterion is related to these test types.',
    )
    sequence = fields.Integer(
        default=5,
        required=True,
    )
