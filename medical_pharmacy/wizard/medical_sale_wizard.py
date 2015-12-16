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

from openerp import models, fields, api


class MedicalSaleWizardAbstract(models.AbstractModel):
    _name = 'medical.sale.wizard.abstract'
    _description = 'Abstract for introspection of Medical Sale Wizards'


class MedicalSaleWizard(models.TransientModel):
    _name = 'medical.sale.wizard'
    _inherit = 'sale.order'
    _description = 'Temporary order info for Sale2Rx workflow'
    
    partner_id = fields.Many2one(
        string='Customer',
        comodel_name='res.partner',
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        comodel_name='medical.pharmacy',
    )
    line_wizard_ids = fields.One2many(
        'medical.sale.line.wizard',
        required=True,
    )
    order_date = fields.Datetime()

    @api.multi
    def _to_vals(self, ):
        ''' Generator of values dicts for ORM methods '''
        for sale_id in self:
            line_ids = [l.id for l in line_id.order_line]
            vals = {
                'prescription_order_id': line_id.prescription_order_id.id,
                'prescription_line_page_ids': (6, 0, page_ids),
                'medical_medication_id': line_id.medical_medication_id.id,
                'is_substitutable': line_id.is_substitutable,
            }
            if line_id.id:
                vals['fax_rx_id'] = line_id.id
            yield vals
    

class MedicalSaleLineWizard(models.TransientModel, MedicalSaleWizardAbstract):
    _name = 'medical.sale.line.wizard'
    _description = 'Temporary order line info for Sale2Rx workflow'
    
    sale_wizard_id = fields.Many2one(
        'medical.sale.wizard',
        readonly=True,
        required=True,
    )
    medicament_id = fields.Many2one(
        string='Medicament',
        comodel_name='medical.medicament',
        required=True,
    )
