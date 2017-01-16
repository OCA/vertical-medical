# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class MedicalPhysicianService(models.Model):
    """ Services provided by the Physician at a specific medical center.

    A physician could have "surgeries" on one center but only
    "general consultation" in another center, or the same service
    with different prices at each medical center.
    """

    _name = 'medical.physician.service'
    _inherits = {'product.product': 'product_id'}
    _description = 'Medical Physician Services'

    product_id = fields.Many2one(
        string='Related Product',
        help='Product related information for service type',
        comodel_name='product.product',
        required=True,
        ondelete='restrict',
    )
    physician_id = fields.Many2one(
        string='Physician',
        help='The physician for the appointment',
        comodel_name='medical.physician',
        required=True,
        index=True,
        ondelete='cascade',
    )
    center_ids = fields.Many2many(
        string='Medical Centers',
        comodel_name='medical.center',
        help='The medical center(s) that this service apply to.'
    )
    center_count = fields.Integer(
        compute='_compute_center_count',
        help='Amount of centers this service is offered at.',
    )

    @api.multi
    def _compute_center_count(self):
        for record in self:
            record.center_count = len(record.center_ids)
