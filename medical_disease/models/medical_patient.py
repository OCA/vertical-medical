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

    @api.one
    def action_invalidate(self):
        super(MedicalPatient, self).action_invalidate()
        self.disease_ids.action_invalidate()

    @api.one
    def compute_count_disease_ids(self):
        self.count_disease_ids = len(self.disease_ids)

    disease_ids = fields.One2many(
        comodel_name='medical.patient.disease', inverse_name='patient_id',
        string='Diseases')
    count_disease_ids = fields.Integer(
        compute='compute_count_disease_ids', string='NB. Disease')
