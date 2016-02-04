# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
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

from openerp import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        related='prescription_order_line_id.patient_id',
    )
    prescription_order_line_id = fields.Many2one(
        string='Prescription Line',
        comodel_name='medical.prescription.order.line',
    )
    medication_id = fields.Many2one(
        string='Medication',
        comodel_name='medical.patient.medication',
        related='prescription_order_line_id.medical_medication_id',
    )
    dispense_qty = fields.Float(
        default=0.0,
        readonly=True,
        compute='_compute_dispense_qty',
    )
