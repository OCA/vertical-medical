# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import api, fields, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    disease_ids = fields.One2many(
        comodel_name='medical.patient.disease',
        inverse_name='patient_id',
        string='Diseases',
    )
    count_disease_ids = fields.Integer(
        compute='compute_count_disease_ids',
        string='Diseases',
    )

    @api.multi
    def compute_count_disease_ids(self, ):
        for rec_id in self:
            rec_id.count_disease_ids = len(rec_id.disease_ids)

    @api.multi
    def action_invalidate(self, ):
        for rec_id in self:
            super(MedicalPatient, rec_id).action_invalidate()
            rec_id.disease_ids.action_invalidate()

    @api.multi
    def action_revalidate(self, ):
        for rec_id in self:
            rec_id.active = True
            rec_id.partner_id.active = True
            disease_ids = self.env['medical.patient.disease'].search([
                ('patient_id', '=', self.id),
                ('active', '=', False),
            ])
            disease_ids.action_revalidate()
