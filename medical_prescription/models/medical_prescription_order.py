# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
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
# #############################################################################

from openerp import fields, models, api


class MedicalPrescriptionOrder(models.Model):
    _name = 'medical.prescription.order'
    _description = 'Medical Prescription Order'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('medical.prescription.order')

    name = fields.Char(required=True, default=_get_default_name)
    patient_id = fields.Many2one(
        comodel_name='medical.patient', string='Patient', required=True)
    physician_id = fields.Many2one(
        comodel_name='medical.physician', string='Physician', required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Pharmacy')
    prescription_order_line_ids = fields.One2many(
        comodel_name='medical.prescription.order.line',
        inverse_name='prescription_order_id', string='Prescription Order Line')
    notes = fields.Text()
    is_pregnant = fields.Boolean()
    is_verified = fields.Boolean()
    prescription_date = fields.Datetime(default=fields.Datetime.now())
