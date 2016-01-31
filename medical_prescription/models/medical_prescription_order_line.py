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
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import fields, models


class MedicalPrescriptionOrderLine(models.Model):
    _name = 'medical.prescription.order.line'
    _inherit = ['abstract.medical.medication']
    _inherits = {'medical.patient.medication': 'medical_medication_id'}
    _rec_name = 'medical_medication_id'

    prescription_order_id = fields.Many2one(
        comodel_name='medical.prescription.order',
        string='Prescription Order')
    medical_medication_id = fields.Many2one(
        comodel_name='medical.patient.medication', string='Medication',
        required=True, ondelete='cascade')
    is_substitutable = fields.Boolean()
    qty = fields.Float(string='Quantity')
