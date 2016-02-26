# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'
    insurance_plan_ids = fields.Many2many(
        string='Insurance Plans',
        comodel_name='medical.insurance.plan',
        help='Past & Present Insurance Plans',
    )
