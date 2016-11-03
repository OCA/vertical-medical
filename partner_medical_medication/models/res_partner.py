# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    medical_patient_ids = fields.Many2many(
        'medical.patient',
        string="Partner's Patients (Including Self)",
        compute='_compute_medical_patient_ids',
    )

    @api.multi
    @api.depends('child_ids')
    def _compute_medical_patient_ids(self):
        for record in self:
            if record.id:
                patients = self.env['medical.patient'].search([
                    ('partner_id', 'child_of', record.id),
                ])
                record.medical_patient_ids = [(6, 0, patients.ids)]
            else:
                record.medical_patient_ids = [(6, 0, [])]
