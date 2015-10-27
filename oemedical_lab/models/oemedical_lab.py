# coding=utf-8

#    Copyright (C) 2012-2013  Federico Manuel Echeverri Choux

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import time
from mx import DateTime
import datetime

from openerp.osv import fields, orm
from openerp.tools.translate import _

# Add Lab test information to the Patient object

class oemedical_patient (orm.Model):
#    _name = "oemedical.patient"
    _inherit = "medical.patient"

    _columns = {
        'lab_test_ids': fields.one2many('oemedical.patient.lab.test','patient_id','Lab Tests Required'),
        }

    
class test_type (orm.Model):
    _name = "oemedical.test_type"
    _description = "Type of Lab test"
    _columns = {
        'name' : fields.char ('Test',size=128,help="Test type, eg X-Ray, hemogram,biopsy..."),
        'code' : fields.char ('Code',size=128,help="Short name - code for the test"),
        'info' : fields.text ('Description'),
        'product_id' : fields.many2one('product.product', 'Service', required=True),
        'critearea': fields.one2many('oemedical_test.critearea','test_type_id','Test Cases'),


    }
    _sql_constraints = [
            ('code_uniq', 'unique (name)', 'The Lab Test code must be unique')]


class lab (orm.Model):
    _name = "oemedical.lab"
    _description = "Lab Test"
    _columns = {
        'name' : fields.char ('ID', size=128, help="Lab result ID"),
        'test' : fields.many2one ('oemedical.test_type', 'Test type', help="Lab test type"),
        'patient' : fields.many2one ('medical.patient', 'Patient', help="Patient ID"), 
        'pathologist' : fields.many2one ('medical.physician','Pathologist',help="Pathologist"),
        'requestor' : fields.many2one ('medical.physician', 'Physician', help="Doctor who requested the test"),
        'results' : fields.text ('Results'),
        'diagnosis' : fields.text ('Diagnosis'),
        'critearea': fields.one2many('oemedical_test.critearea','oemedical_lab_id','Test Cases'),
        'date_requested' : fields.datetime ('Date requested'),
        'date_analysis' : fields.datetime ('Date of the Analysis'),        
        }

    _defaults = {
        'date_requested': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'date_analysis': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'name' : lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'oemedical.lab'),         
         }


    _sql_constraints = [
                ('id_uniq', 'unique (name)', 'The test ID code must be unique')]




class oemedical_lab_test_units(orm.Model):
    _name = "oemedical.lab.test.units"
    _columns = {
        'name' : fields.char('Unit', size=25),
        'code' : fields.char('Code', size=25),
        }
    _sql_constraints = [
            ('name_uniq', 'unique(name)', 'The Unit name must be unique')]
    


class oemedical_test_critearea(orm.Model):
    _name = "oemedical_test.critearea"
    _description = "Lab Test Critearea"    
    _columns ={
       'name' : fields.char('Test', size=64),
       'result' : fields.text('Result'),
       'normal_range' : fields.text('Normal Range'),
       'units' : fields.many2one('oemedical.lab.test.units', 'Units'),
       'test_type_id' : fields.many2one('oemedical.test_type','Test type'),
       'oemedical_lab_id' : fields.many2one('oemedical.lab','Test Cases'),
       'sequence' : fields.integer('Sequence'),       
       }
    _defaults = {
         'sequence' : lambda *a : 1,        
         }
    _order="sequence"


    

class oemedical_patient_lab_test(orm.Model):
    _name = 'oemedical.patient.lab.test'
    def _get_default_dr(self, cr, uid, context={}):
        partner_id = self.pool.get('res.partner').search(cr,uid,[('user_id','=',uid)])
        if partner_id:
            dr_id = self.pool.get('medical.physician').search(cr,uid,[('name','=',partner_id[0])])
            if dr_id:
                return dr_id[0]
            #else:
            #    raise osv.except_osv(_('Error !'),
            #            _('There is no physician defined ' \
            #                    'for current user.'))
        else:
            return False
        
    _columns = {
        'name' : fields.many2one('oemedical.test_type','Test Type'),
        'date' : fields.datetime('Date'),
        'state' : fields.selection([('draft','Draft'),('tested','Tested'),('cancel','Cancel')],'State',readonly=True),
        'patient_id' : fields.many2one('medical.patient','Patient'),
        'doctor_id' : fields.many2one('medical.physician','Doctor', help="Doctor who Request the lab test."), 
        #'invoice_status' : fields.selection([('invoiced','Invoiced'),('tobe','To be Invoiced'),('no','No Invoice')],'Invoice Status'),
        }
    
    _defaults={
       'date' : lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
       'state' : lambda *a : 'draft',
       'doctor_id' : _get_default_dr,        
       #'invoice_status': lambda *a: 'tobe',
       }
    



