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


class MedicalPrescriptionLine(models.Model):
    _inherit = 'medical.prescription.order.line'

    sale_order_line_id = fields.Many2one(
        'sale.order.line',
    )
    sale_order_id = fields.Many2one(
        'sale.order',
        related='sale_order_line_id.order_id',
    )
    dispense_ids = fields.One2many(
        'procurement.order',
        related='order_line_id.procurement_ids',
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'Open'),
        ('matched', 'Matched Sale'),
        ('manual', 'To Invoice'),
        ('dispense', 'To Dispense'),
        ('dispense_except', 'Dispense Exception'),
        ('invoice_except', 'Invoice Exception'),
        ('cancel', 'Canceled'),
        ('dispensed', 'Dispensed'),
    ],
        default='draft',
    )
