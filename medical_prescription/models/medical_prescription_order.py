# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api


class MedicalPrescriptionOrder(models.Model):
    _name = 'medical.prescription.order'
    _description = 'Medical Prescription Order'

    name = fields.Char(required=True, default=lambda s: s._default_name())
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
    is_pregnancy_warning = fields.Boolean()
    is_verified = fields.Boolean()
    date_prescription = fields.Datetime(default=fields.Datetime.now())

    @api.model
    def _default_name(self):
        return self.env['ir.sequence'].next_by_code(
            'medical.prescription.order'
        )
