# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class RequestGroup(models.Model):
    _name = 'medical.request.group'
    _description = 'Request Group'
    _inherit = 'mail.thread'

    internal_identifier = fields.Char(
        string='Request Group ID',
        default='/',
        readonly=True,
    )
    name = fields.Char(
        string='Name',
        help='Name',
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        required=True,
        index=True,
        help='Patient Name',
    )
    service_id = fields.Many2one(
        string='Service',
        comodel_name='product.product',
        domain="[('type', '=', 'service')]",
    )
    center_id = fields.Many2one(
        string='Center',
        comodel_name='medical.center',
        required=True,
        index=True,
        help='Responsible Medical Center',
    )

    @api.model
    def create_resource_from_activity_definition(self, activity_definition,
                                                 is_billable):
        ''' This method should be defined by each resources that could be 
        created from a request group, based on an activity definition.'''
