# -*- coding: utf-8 -*-
# Copyright 2012-2013 Federico Manuel Echeverri Choux
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import fields, models


class MedicalLabPatient(models.Model):
    _name = 'medical.lab.patient'
    _description = 'Medical Labs - Patient'
    _inherits = {'medical.lab': 'lab_id'}

    lab_id = fields.Many2one(
        string='Lab',
        comodel_name='medical.lab',
        required=True,
        ondelete='cascade',
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('done', 'Tested'),
            ('cancel', 'Cancelled'),
        ],
        readonly=True,
        default='draft',
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        required=True,
    )
