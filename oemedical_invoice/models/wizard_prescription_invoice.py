# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010  Adrián Bernardi, Mario Puntin
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging

from openerp.osv import fields, orm
from openerp.tools.translate import _

logging.basicConfig(level=logging.DEBUG)


class make_medical_prescription_invoice(orm.TransientModel):
    _name="medical.prescription.invoice"

    def create_prescription_invoice(self, cr, uid, ids, context={}):
        
        invoice_obj = self.pool.get('account.invoice')
        pres_request_obj = self.pool.get('oemedical.prescription.order')
    
#        prescriptions = ids
# Don't use this. It will be 1 (and it would go to the invoice status of the first prescription )

# To get the IDs of the prescriptions, use the context value array for active_ids


        prescriptions = context.get ('active_ids')
            
        pats = []



        for pres_id in prescriptions:
            pres=pres_request_obj.browse(cr, uid, pres_id)
            pats.append(pres.patient_id.user_id.id)
            logging.debug('pres = %s; pats = %s', repr(pres), repr(pats))
    
        if pats.count(pats[0]) == len(pats):
            invoice_data = {}
            for pres_id in prescriptions:
                pres = pres_request_obj.browse(cr, uid, pres_id)

# Check if the prescription is invoice exempt, and stop the invoicing process
                if pres.no_invoice :
                    raise  orm.except_orm(_('UserError'), _('The prescription is invoice exempt'))                
    
                if pres.invoice_status == 'invoiced':
                    logging.debug('pres.invoice_status = %s', repr(pres.invoice_status))
                    if len(prescriptions) > 1:
                        raise  orm.except_orm(_('UserError'), _('At least one of the selected prescriptions is already invoiced'))
                    else:
                        raise  orm.except_orm(_('UserError'), _('Prescription already invoiced'))
                if pres.invoice_status == 'no':
                    if len(prescriptions) > 1:
                        raise  orm.except_orm(_('UserError'), _('At least one of the selected prescriptions can not be invoiced'))
                    else:
                        raise  orm.except_orm(_('UserError'), _('You can not invoice this prescription'))
    
            logging.debug('pres.name = %s', repr(pres.name))
            if pres.patient_id.user_id.id:
                invoice_data['partner_id'] = pres.patient_id.user_id.id
                res = self.pool.get('res.partner').address_get(cr, uid, [pres.patient_id.user_id.partner_id.id], ['contact', 'invoice'])
                invoice_data['address_contact_id'] = res['contact']
                invoice_data['address_invoice_id'] = res['invoice']
                invoice_data['account_id'] = pres.patient_id.user_id.partner_id.property_account_receivable.id
                invoice_data['fiscal_position'] = pres.patient_id.user_id.partner_id.property_account_position and pres.patient_id.user_id.partner_id.property_account_position.id or False
                invoice_data['payment_term'] = pres.patient_id.user_id.partner_id.property_payment_term and pres.patient_id.user_id.partner_id.property_payment_term.id or False
    
            prods_data = {}
            for pres_id in prescriptions:
                pres = pres_request_obj.browse(cr, uid, pres_id)
                logging.debug('pres.name = %s; pres.prescription_line = %s', pres.name, pres.prescription_line)
                
# Check for empty prescription lines

                if not pres.prescription_line:
                    raise  orm.except_orm(_('UserError'), _('You need to have at least one prescription item in your invoice'))            
                
                for pres_line in pres.prescription_line:
                    logging.debug('pres_line = %s; pres_line.medicament.name = %s; pres_line.quantity = %s', pres_line, pres_line.template.medicament_id.product_id.product_tmpl_id.name, pres_line.quantity)
    
                    if prods_data.has_key(pres_line.template.medicament_id.product_id.product_tmpl_id.name):
                        prods_data[pres_line.template.medicament_id.product_id.product_tmpl_id.name]['quantity'] += pres_line.quantity
                    else:
                        if pres_line.template.medicament_id.product_id.product_tmpl_id.property_account_income.id:
                            a = pres_line.template.medicament_id.product_id.product_tmpl_id.property_account_income.id
                        else:
                            raise orm.except_orm(_('UserError'), _('Income Account is not configured in your Product.'))
                        if not a:
                            a = pres_line.template.medicament_id.product_id.product_tmpl_id.categ_id.property_account_income_categ.id

                        prods_data[pres_line.template.medicament_id.product_id.product_tmpl_id.name] = {'product_id':pres_line.template.medicament_id.product_id.id,
                                        'name':pres_line.template.medicament_id.product_id.product_tmpl_id.name,
                                        'quantity':pres_line.quantity,
                                        'account_id':a,
                                        'price_unit':pres_line.template.medicament_id.product_id.product_tmpl_id.list_price}
                    
    
            product_lines = []
            for prod_id, prod_data in prods_data.items():
                logging.debug('product_id = %s', repr(prod_data['product_id']))
                product_lines.append((0, 0, {'product_id':prod_data['product_id'],
                        'name':prod_data['name'],
                        'quantity':prod_data['quantity'],
                        'account_id':prod_data['account_id'],
                        'price_unit':prod_data['price_unit']}))
                
            invoice_data['invoice_line'] = product_lines
            invoice_id = invoice_obj.create(cr, uid, invoice_data)
            
            pres_request_obj.write(cr, uid, prescriptions, {'invoice_status':'invoiced'})
    
            return {
                'domain': "[('id','=', " + str(invoice_id) + ")]",
                'name': 'Create Prescription Invoice',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'account.invoice',
                'type': 'ir.actions.act_window'
            }
    
        else:
            raise  orm.except_orm(_('UserError'), _('When multiple prescriptions are selected, patient must be the same'))


make_medical_prescription_invoice()


