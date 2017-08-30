# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class MedicalProcedureRequestSettings(models.Model):
    _name = 'medical.procedure.request.settings'
    _description = 'Medical Procedure Request Settings'
    _inherit = 'res.config.settings'

    group_procedure = fields.Selection([
        (0, 'Manage Procedures as single entities for actions to be '
            'performed'),
        (1, 'Manage Request Groups in order to have grouping options for '
            'procedures')],
        "Relating options on Procedures",
        implied_group='medical_request_group.group_request_group',
        help="""This allows you to create a group of related procedure requests 
        that can be used to capture intended activities that have 
        inter-dependencies to be performed on a patient.""",
    )


