# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalPrescriptionOrder(models.Model):
    _name = 'medical.prescription.order'
    _description = 'Medical Prescription Order'

    name = fields.Char(
        required=True,
        default=lambda s: s._default_name()
    )
    patient_id = fields.Many2one(
        comodel_name='medical.patient',
        string='Patient',
        required=True,
        help='Primary patient that this is regarding',
    )
    physician_id = fields.Many2one(
        comodel_name='medical.physician',
        string='Physician',
        required=True,
        help='Physician that issued prescription',
    )
    partner_id = fields.Many2one(
        comodel_name='medical.pharmacy',
        string='Pharmacy',
    )
    prescription_order_line_ids = fields.One2many(
        comodel_name='medical.prescription.order.line',
        inverse_name='prescription_order_id',
        string='Prescription Order Line',
    )
    notes = fields.Text()
    is_pregnancy_warning = fields.Boolean(
        string='Pregnant',
        help='Check this if the primary patient on prescription is pregnant',
    )
    is_verified = fields.Boolean(
        string='Verified',
        help='Check this is the prescription has been confirmed as valid',
    )
    date_prescription = fields.Datetime(
        string='Prescription Date',
        default=lambda s: fields.Datetime.now(),
    )
    active = fields.Boolean(
        compute='_compute_active',
        store=True,
    )

    @api.model
    def _default_name(self):
        return self.env['ir.sequence'].next_by_code(
            'medical.prescription.order',
        )

    @api.multi
    @api.depends('prescription_order_line_ids',
                 'prescription_order_line_ids.active',
                 )
    def _compute_active(self):
        for rec_id in self:
            if not rec_id.prescription_order_line_ids:
                rec_id.active = True
                continue
            rec_id.active = any(
                rec_id.prescription_order_line_ids.mapped('active')
            )
