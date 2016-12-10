# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    disease_ids = fields.One2many(
        string='Diseases',
        comodel_name='medical.patient.disease',
        inverse_name='patient_id',
        domain=[('is_allergy', '=', False)],
    )
    allergy_ids = fields.One2many(
        string='Allergies',
        comodel_name='medical.patient.disease',
        inverse_name='patient_id',
        domain=[('is_allergy', '=', True)],
    )
    count_allergy_ids = fields.Integer(
        string='Allergies',
        compute='_compute_count_allergy_ids',
    )

    @api.multi
    def _compute_count_allergy_ids(self):
        for record in self:
            record.count_allergy_ids = len(record.allergy_ids)
