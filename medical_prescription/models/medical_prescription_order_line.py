# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MedicalPrescriptionOrderLine(models.Model):
    _name = 'medical.prescription.order.line'
    _inherit = ['abstract.medical.medication']
    _inherits = {'medical.patient.medication': 'medical_medication_id'}
    _rec_name = 'medical_medication_id'

    prescription_order_id = fields.Many2one(
        comodel_name='medical.prescription.order',
        string='Prescription Order',
        required=True,
    )
    medical_medication_id = fields.Many2one(
        comodel_name='medical.patient.medication',
        string='Medication',
        required=True,
        ondelete='cascade',
    )
    is_substitutable = fields.Boolean()
    qty = fields.Float(
        string='Quantity',
    )
    name = fields.Char(
        required=True,
        default=lambda s: s._default_name(),
    )

    @api.model
    def _default_name(self):
        return self.env['ir.sequence'].next_by_code(
            'medical.prescription.order.line'
        )

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = [
            '|', '|', '|', '|',
            ('medicament_id.product_id.name', operator, name),
            ('medicament_id.strength', operator, name),
            ('medicament_id.strength_uom_id.name', operator, name),
            ('medicament_id.drug_form_id.code', operator, name),
            ('patient_id.name', operator, name),
        ]
        recs = self.search(domain + args, limit=limit)
        return recs.name_get()
