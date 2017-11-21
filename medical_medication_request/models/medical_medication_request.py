# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalMedicationRequest(models.Model):
    # FHIR entity: Medication request
    # (https://www.hl7.org/fhir/medicationrequest.html)
    _name = 'medical.medication.request'
    _description = 'Medical Medication request'
    _inherit = 'medical.request'

    category = fields.Selection(
        [
            ('inpatient', 'Inpatient'),
            ('outpatient', 'Outpatient'),
            ('community', 'Community')
        ],
        required=True,
        default='inpatient',
    )   # FHIR Field: category
    product_id = fields.Many2one(
        comodel_name='product.product',
        domain=[('is_medication', '=', True)],
        required=True,
    )
    product_uom_id = fields.Many2one(
        'product.uom',
        'Unit of Measure',
        required=True,
    )
    qty = fields.Float(
        'Quantity',
        default=1.0,
        required=True,
    )
    medication_administration_ids = fields.One2many(
        comodel_name='medical.medication.administration',
        inverse_name='medication_request_id',
    )
    medication_request_ids = fields.One2many(
        inverse_name="medication_request_id",
    )  # FHIR Field: BasedOn

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.product_uom_id = self.product_id.uom_id.id

    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.medication.request') or '/'

    def _get_event_values(self):
        return {
            'medication_request_id': self.id,
            'product_id': self.product_id.id,
            'qty': self.qty,
            'product_uom_id': self.product_uom_id.id,
            'patient_id': self.patient_id.id,
            'name': self.name,
        }

    @api.multi
    def generate_event(self):
        self.ensure_one()
        return self.env['medical.medication.administration'].create(
            self._get_event_values())

    @api.multi
    def action_view_medication_administration(self):
        self.ensure_one()
        action = self.env.ref(
            'medical_medication_request.'
            'medical_medication_administration_action')
        result = action.read()[0]
        result['context'] = {
            'default_patient_id': self.patient_id.id,
            'default_medication_request_id': self.id,
            'default_name': self.name,
            'default_product_id': self.product_id.id,
            'default_product_uom_id': self.product_uom_id.id,
            'default_qty': self.qty
        }
        result['domain'] = "[('medication_request_id', '=', " + \
                           str(self.id) + ")]"
        if len(self.medication_administration_ids) == 1:
            result['views'] = [(False, 'form')]
            result['res_id'] = self.medication_administration_ids.id
        return result

    def _get_parent_field_name(self):
        return 'medication_request_id'

    def action_view_request_parameters(self):
        return {
            'view': 'medical_medication_request.'
                    'medical_medication_request_action',
            'view_form': 'medical.medication.request.view.form', }
