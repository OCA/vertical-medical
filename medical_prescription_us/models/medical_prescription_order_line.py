# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


# @TODO: Abstract control codes into core, add months till expire
DELTA_MAP = {
    '0': 12,
    '1': 1,
    '2': 1,
    '3': 6,
    '4': 6,
    '5': 6,
}


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'
    refill_qty_original = fields.Float(
        string='Refill Qty',
        help='Amount of refills originally allowed in this prescription',
    )
    refill_qty_remain = fields.Float(
        string='Refill Remain',
        help='Amount of refills remaining in the prescription',
    )
    ndc_id = fields.Many2one(
        string='NDC',
        comodel_name='medical.medicament.ndc',
    )
    gcn_id = fields.Many2one(
        string='GCN',
        comodel_name='medical.medicament.gcn',
    )

    @api.model
    def create(self, vals):
        if not vals.get('date_stop_treatment'):
            try:
                date_start = fields.Datetime.from_string(
                    vals['date_start_treatment']
                )
                medicament = self.env['medical.medicament'].browse(
                    vals['medicament_id']
                )
                delta = relativedelta(
                    months=DELTA_MAP[medicament.control_code]
                )
                vals['date_stop_treatment'] = fields.Datetime.to_string(
                    date_start + delta
                )
            except KeyError:
                pass
        return super(MedicalPrescriptionOrderLine, self).create(vals)

    @api.multi
    @api.constrains('refill_qty_original')
    def _check_refill_qty_original(self):
        for rec_id in self:
            if rec_id.refill_qty_original < 0:
                raise ValidationError(_(
                    'Refill quantity cannot be less than 0.'
                ))
