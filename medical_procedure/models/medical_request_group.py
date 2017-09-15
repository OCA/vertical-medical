# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _


class RequestGroup(models.Model):
    _inherit = 'medical.request.group'

    procedure_request_ids = fields.One2many(
        string="Associated Procedure Requests",
        comodel_name="medical.procedure.request",
        inverse_name="request_group_id",
    )
    request_group_ids = fields.One2many(
        string="Internal request groups",
        comodel_name="medical.request.group",
        inverse_name="request_group_id",
    )
    request_group_id = fields.Many2one(
        string="Request group",
        comodel_name="medical.request.group",
    )

    def _compute_request_group_ids(self):
        related_ids = []
        # here compute & fill related_ids with ids of related object
        self.request_group_ids.ids = related_ids

    def _prepare_procedure_request(self, activity_definition, is_billable,
                                   name=False,
                                   variable_fee=False, fixed_fee=False):
        return {
            'title': name or activity_definition.name,
            'subject_id': self.patient_id.id,
            'request_group_id': self.id,
            'service_id': activity_definition.resource_product_id.id,
            'center_id': self.center_id.id,
            'variable_fee': variable_fee,
            'fixed_fee': fixed_fee,
            'is_billable': is_billable,
        }

    @api.model
    def create_resource_from_activity_definition(self, activity_definition,
                                                 is_billable, name=False,
                                                 variable_fee=False,
                                                 fixed_fee=False):
        if activity_definition.model_id.model == \
                'medical.procedure.request':
            data = self._prepare_procedure_request(activity_definition,
                                                   is_billable,
                                                   name=name,
                                                   variable_fee=variable_fee,
                                                   fixed_fee=fixed_fee)
            self.env['medical.procedure.request'].create(data)
        return super(RequestGroup,
                     self).create_resource_from_activity_definition(
            activity_definition, is_billable)
