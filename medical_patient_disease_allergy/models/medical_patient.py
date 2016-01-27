# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2016-TODAY LasLabs, Inc. [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api, fields


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
    def action_invalidate(self, ):
        for rec_id in self:
            super(MedicalPatient, rec_id).action_invalidate()
            for disease_id in rec_id.allergy_ids:
                disease_id.action_invalidate()

    @api.multi
    def _compute_count_allergy_ids(self, ):
        for rec_id in self:
            rec_id.count_allergy_ids = len(rec_id.allergy_ids)
