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


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.one
    def _compute_patient_ids(self, ):
        patient_ids = self.env['medical.patient']
        for line_id in self.order_line:
            patient_id = line_id.patient_id
            if patient_id not in patient_ids:
                patient_ids += patient_id
        self.patient_ids = patient_ids 

    patient_ids = fields.Many2many(
        string='Patients',
        comodel_name='medical.patient',
        compute='_compute_patient_ids',
        readonly=True,
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        comodel_name='medical.pharmacy',
    )

    state = fields.Selection(selection_add=[
        ('rx_verify', 'Rx Verification'),
    ])
