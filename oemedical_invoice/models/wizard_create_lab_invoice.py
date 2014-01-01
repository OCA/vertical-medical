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

from osv import fields, osv
import pooler
from tools.translate import _
import sys

logging.basicConfig(level=logging.DEBUG)

class create_test_invoice(osv.osv_memory):
    _name='medical.lab.test.invoice'

    def create_lab_invoice(self, cr, uid, ids, context={}):

        invoice_obj = self.pool.get('account.invoice')
        test_request_obj = self.pool.get('medical.patient.lab.test')


        tests = context.get ('active_ids')
        logging.debug('tests = %s', repr(tests))
        
        pats = []
        for test_id in tests:
            #pats.append(test_request_obj.browse(cr, uid, test_id).patient_id)
            cur_test = test_request_obj.browse(cr, uid, test_id)
            logging.debug('cur_test = %s; pats = %s', repr(cur_test), repr(pats))
            pats.append(cur_test.patient_id)
    
        logging.debug('pats = %s', repr(pats))
    
        if pats.count(pats[0]) == len(pats):
            invoice_data = {}
            for test_id in tests:
                #test = self.browse(cr, uid, test_id)
                test = test_request_obj.browse(cr, uid, test_id)
                logging.debug('test = %s', repr(test))
                if test.invoice_status == 'invoiced':
                    if len(tests) > 1:
                        raise  osv.except_osv(_('UserError'), _('At least one of the selected lab tests is already invoiced'))
                    else:
                        raise  osv.except_osv(_('UserError'), _('Lab test already invoiced'))
                if test.invoice_status == 'no':
                    if len(tests) > 1:
                        raise  osv.except_osv(_('UserError'), _('At least one of the selected lab tests can not be invoiced'))
                    else:
                        raise  osv.except_osv(_('UserError'), _('You can not invoice this lab test'))
    
            logging.debug('test.patient_id = %s; test.patient_id.id = %s', test.patient_id, test.patient_id.id)
            if test.patient_id.name.id:
                invoice_data['partner_id'] = test.patient_id.name.id
                res = self.pool.get('res.partner').address_get(cr, uid, [test.patient_id.name.id], ['contact', 'invoice'])
                invoice_data['address_contact_id'] = res['contact']
                invoice_data['address_invoice_id'] = res['invoice']
                invoice_data['account_id'] = test.patient_id.name.property_account_receivable.id
                invoice_data['fiscal_position'] = test.patient_id.name.property_account_position and test.patient_id.name.property_account_position.id or False
                invoice_data['payment_term'] = test.patient_id.name.property_payment_term and test.patient_id.name.property_payment_term.id or False
    
            prods_data = {}

            tests = context.get ('active_ids')
            logging.debug('tests = %s', repr(tests))
        
            for test_id in tests:
                test = test_request_obj.browse(cr, uid, test_id)
                logging.debug('test.name = %s; test.name.product_id = %s; test.name.product_id.id = %s', test.name, test.name.product_id, test.name.product_id.id)
    
                if prods_data.has_key(test.name.product_id.id):
                    logging.debug('prods_data = %s; test.name.product_id.id = %s', prods_data, test.name.product_id.id)
                    prods_data[test.name.product_id.id]['quantity'] += 1
                else:
                    logging.debug('test.name.product_id.id = %s', test.name.product_id.id)
                    a = test.name.product_id.product_tmpl_id.property_account_income.id
                    if not a:
                        a = test.name.product_id.categ_id.property_account_income_categ.id
                    prods_data[test.name.product_id.id] = {'product_id':test.name.product_id.id,
                                    'name':test.name.product_id.name,
                                    'quantity':1,
                                    'account_id':a,
                                    'price_unit':test.name.product_id.lst_price}
                    logging.debug('prods_data[test.name.product_id.id] = %s', prods_data[test.name.product_id.id])
    
            product_lines = []
            for prod_id, prod_data in prods_data.items():
                product_lines.append((0, 0, {'product_id':prod_data['product_id'],
                        'name':prod_data['name'],
                        'quantity':prod_data['quantity'],
                        'account_id':prod_data['account_id'],
                        'price_unit':prod_data['price_unit']}))
                
            invoice_data['invoice_line'] = product_lines
            invoice_id = invoice_obj.create(cr, uid, invoice_data)
            
            test_request_obj.write(cr, uid, tests, {'invoice_status':'invoiced'})
    
            return {
                'domain': "[('id','=', " + str(invoice_id) + ")]",
                'name': 'Create Lab Invoice',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'account.invoice',
                'type': 'ir.actions.act_window'
            }
    
        else:
            raise  osv.except_osv(_('UserError'), _('When multiple lab tests are selected, patient must be the same'))


create_test_invoice()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
