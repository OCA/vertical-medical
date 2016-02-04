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

from openerp import fields, models, api


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'

    sale_order_line_ids = fields.One2many(
        comodel_name='sale.order.line',
        inverse_name='prescription_order_line_id',
        readonly=True,
    )
    sale_order_ids = fields.Many2many(
        comodel_name='sale.order',
        compute='_compute_orders',
        readonly=True,
    )
    name = fields.Char(
        default=lambda s: s._default_name(),
        required=True,
    )
    verify_method = fields.Selection([
        ('none', 'Not Verified'),
        ('doctor_phone', 'Called Doctor'),
    ],
        default='none',
        help='Method of Rx verification',
        related='prescription_order_id.verify_method',
    )
    receive_date = fields.Datetime(
        default=lambda s: fields.Datetime.now(),
        string='Receipt Date',
        help='When the Rx was received',
        related='prescription_order_id.receive_date',
    )

    @api.multi
    def _compute_orders(self, ):
        for rec_id in self:
            order_ids = self.env['sale.order']
            for line_id in rec_id.sale_order_line_ids:
                order_ids += line_id.order_id
            rec_id.order_ids = set(order_ids)

    @api.model
    def _default_name(self, ):
        return self.env['ir.sequence'].next_by_code(
            'medical.prescription.order.line'
        )
