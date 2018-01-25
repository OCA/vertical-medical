# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, fields, models


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'

    sale_order_line_ids = fields.One2many(
        string='Sale Order Lines',
        comodel_name='sale.order.line',
        inverse_name='prescription_order_line_id',
        readonly=True,
    )
    sale_order_ids = fields.Many2many(
        string='Sale Orders',
        comodel_name='sale.order',
        compute='_compute_orders',
        readonly=True,
    )
    verify_method = fields.Selection(
        selection=[
            ('none', 'Not Verified'),
            ('doctor_phone', 'Called Doctor'),
        ],
        default='none',
        help='Method of Rx verification',
        related='prescription_order_id.verify_method',
    )
    receive_date = fields.Datetime(
        default=lambda s: fields.Datetime.now(),
        string='Receive Date',
        help='When the Rx was received',
        related='prescription_order_id.receive_date',
    )

    @api.multi
    def _compute_orders(self):
        for record in self:
            order_ids = []
            for line_id in record.sale_order_line_ids:
                order_ids.append(line_id.order_id.id)
            record.sale_order_ids = self.env['sale.order'].browse(
                set(order_ids)
            )
