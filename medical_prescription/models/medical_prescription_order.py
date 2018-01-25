# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import fields, models, api


class MedicalPrescriptionOrder(models.Model):
    _name = 'medical.prescription.order'
    _description = 'Medical Prescription Order'

    notes = fields.Text()
    name = fields.Char(
        required=True,
        default=lambda s: s._default_name()
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        required=True,
        help='Primary patient this is regarding',
    )
    physician_id = fields.Many2one(
        string='Physician',
        comodel_name='medical.physician',
        required=True,
        help='Physician that issued prescription',
    )
    partner_id = fields.Many2one(
        string='Pharmacy',
        comodel_name='medical.pharmacy',
    )
    prescription_order_line_ids = fields.One2many(
        string='Prescription Order Lines',
        comodel_name='medical.prescription.order.line',
        inverse_name='prescription_order_id',
    )
    is_pregnancy_warning = fields.Boolean(
        string='Pregnant',
        help='Check this if the primary patient on prescription is pregnant',
    )
    is_verified = fields.Boolean(
        string='Verified',
        help='Check this if the prescription has been confirmed as valid',
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
