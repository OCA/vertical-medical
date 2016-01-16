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


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.one
    def _compute_prescription_order_and_patient_ids(self, ):
        prescription_ids = self.env['medical.prescription.order']
        patient_ids = self.env['medical.patient']
        for line_id in self.prescription_order_line_ids:
            if line_id.prescription_order_id not in prescription_ids:
                prescription_ids += line_id.prescription_order_id
            if line_id.patient_id not in patient_ids:
                patient_ids += line_id.patient_id
        self.write({
            'prescription_order_ids': prescription_ids,
            'is_prescription': len(prescription_ids) > 0,
            'patient_ids': patient_ids,
        })

    patient_ids = fields.Many2many(
        string='Patients',
        comodel_name='medical.patient',
        compute='_compute_prescription_order_and_patient_ids',
        readonly=True,
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        comodel_name='medical.pharmacy',
    )
    prescription_order_ids = fields.Many2many(
        string='Prescriptions',
        comodel_name='medical.prescription.order',
        compute='_compute_prescription_order_and_patient_ids',
        readonly=True,
    )
    prescription_order_line_ids = fields.Many2many(
        string='Prescription Lines',
        comodel_name='medical.prescription.order.line',
        # readonly=True,
    )
    is_prescription = fields.Boolean(
        readonly=True,
        default=False,
        compute='_compute_prescription_order_and_patient_ids'
    )
