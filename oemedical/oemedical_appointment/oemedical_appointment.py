# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
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
#/#############################################################################
from osv import osv
from osv import fields
import time


class OeMedicalAppointment(osv.Model):
    _name = 'oemedical.appointment'

    _columns = {
        'patient_id': fields.many2one('oemedical.patient', string='Patient',
                                   required=True, select=True,
                                   help='Patient Name'),
        'name': fields.char(size=256, string='Appointment ID', readonly=True),
        'appointment_date': fields.datetime(string='Date and Time'),
        'appointment_day': fields.date(string='Date'),
        'appointment_hour': fields.selection([
            ('01', '01'),
            ('02', '02'),
            ('03', '03'),
            ('04', '04'),
            ('05', '05'),
            ('06', '06'),
            ('07', '07'),
            ('08', '08'),
            ('09', '09'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
             ],
            string='Hour'),
        'appointment_minute': fields.selection([
            ('05', '05'),
            ('10', '10'),
            ('15', '15'),
            ('20', '20'),
            ('25', '25'),
            ('30', '30'),
            ('35', '35'),
            ('40', '40'),
            ('45', '45'),
            ('50', '50'),
            ('55', '55'),
             ],
            string='Minute'),

        'duration': fields.float('Duration'),
        'doctor': fields.many2one('oemedical.physician',
                                  string='Physician',select=True, 
                                  help='Physician\'s Name'),
        'alias' : fields.char(size=256, string='Alias', ),
        'comments': fields.text(string='Comments'),
        'appointment_type': fields.selection([
            ('ambulatory', 'Ambulatory'),
            ('outpatient', 'Outpatient'),
            ('inpatient', 'Inpatient'),
        ], string='Type'),
        'institution': fields.many2one('res.partner',
                                       string='Health Center',
                                       help='Medical Center'
                                        , domain="[('category_id', '=', 'Doctor Office')]"),
        'consultations': fields.many2one('product.product',
                                         string='Consultation Services',
                                          help='Consultation Services'
                                        , domain="[('type', '=', 'service'), ]"),
        'urgency': fields.selection([
            ('a', 'Normal'),
            ('b', 'Urgent'),
            ('c', 'Medical Emergency'), ],
            string='Urgency Level'),
        'speciality': fields.many2one('oemedical.specialty',
                                      string='Specialty', 
                                      help='Medical Specialty / Sector'),
        'state': fields.selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('waiting', 'Wating'),
            ('in_consultation', 'In consultation'),
            ('done', 'Done'),
            ('canceled', 'Canceled'),
             ],
            string='State'),
        'history_ids' : fields.one2many('oemedical.appointment.history','appointment_id_history','History lines', states={'start':[('readonly',True)]}),

    }
    
    _defaults = {
        'name': lambda obj, cr, uid, context: 
            obj.pool.get('ir.sequence').get(cr, uid, 'oemedical.appointment'),
        'duration': 30.00,
        'urgency': 'a',
        'state': 'draft',

                 }

    def create(self, cr, uid, vals, context=None):
        val_history = {}
        ait_obj = self.pool.get('oemedical.appointment.history')



        val_history['name'] = uid
        val_history['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        val_history['action'] = "--------------------------------  Changed to Comfirm  ------------------------------------\n"

        vals['history_ids'] = val_history

        print "create", vals['history_ids'], val_history, '     ------    ', vals

        return super(OeMedicalAppointment, self).create(cr, uid, vals, context=context)

    def button_back(self, cr, uid, ids, context=None):

        val_history = {}
        ait_obj = self.pool.get('oemedical.appointment.history')

        for order in self.browse(cr, uid, ids, context=context):
            if order.state == 'confirm':
                self.write(cr, uid, ids, {'state':'draft'} ,context=context)
                val_history['action'] = "--------------------------------  Changed to Draft  ------------------------------------\n"
            if order.state == 'waiting':
                val_history['action'] = "--------------------------------  Changed to Confirm  ------------------------------------\n"
                self.write(cr, uid, ids, {'state':'confirm'} ,context=context)
            if order.state == 'in_consultation':
                val_history['action'] = "--------------------------------  Changed to Waiting  ------------------------------------\n"
                self.write(cr, uid, ids, {'state':'waiting'} ,context=context)
            if order.state == 'done':
                val_history['action'] = "--------------------------------  Changed to In Consultation  ------------------------------------\n"
                self.write(cr, uid, ids, {'state':'in_consultation'} ,context=context)
            if order.state == 'canceled':
                val_history['action'] = "--------------------------------  Changed to Draft  ------------------------------------\n"
                self.write(cr, uid, ids, {'state':'draft'} ,context=context)

        val_history['appointment_id_history'] = ids[0]
        val_history['name'] = uid
        val_history['date'] = time.strftime('%Y-%m-%d %H:%M:%S')

        ait_obj.create(cr, uid, val_history)

        return True

    def button_confirm(self, cr, uid, ids, context=None):

        val_history = {}
        ait_obj = self.pool.get('oemedical.appointment.history')

        self.write(cr, uid, ids, {'state':'confirm'} ,context=context)

        val_history['appointment_id_history'] = ids[0]
        val_history['name'] = uid
        val_history['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        val_history['action'] = "--------------------------------  Changed to Comfirm  ------------------------------------\n"
        ait_obj.create(cr, uid, val_history)

        return True

    def button_waiting(self, cr, uid, ids, context=None):

        val_history = {}
        ait_obj = self.pool.get('oemedical.appointment.history')

        self.write(cr, uid, ids, {'state':'waiting'} ,context=context)

        val_history['appointment_id_history'] = ids[0]
        val_history['name'] = uid
        val_history['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        val_history['action'] = "--------------------------------  Changed to Waiting  ------------------------------------\n"
        ait_obj.create(cr, uid, val_history)

        return True

    def button_in_consultation(self, cr, uid, ids, context=None):

        val_history = {}
        ait_obj = self.pool.get('oemedical.appointment.history')

        self.write(cr, uid, ids, {'state':'in_consultation'} ,context=context)

        val_history['appointment_id_history'] = ids[0]
        val_history['name'] = uid
        val_history['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        val_history['action'] = "--------------------------------  Changed to In Consultation  ------------------------------------\n"
        ait_obj.create(cr, uid, val_history)

        return True

    def button_done(self, cr, uid, ids, context=None):

        val_history = {}
        ait_obj = self.pool.get('oemedical.appointment.history')

        self.write(cr, uid, ids, {'state':'done'} ,context=context)

        val_history['appointment_id_history'] = ids[0]
        val_history['name'] = uid
        val_history['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        val_history['action'] = "--------------------------------  Changed to Done  ------------------------------------\n"
        ait_obj.create(cr, uid, val_history)

        return True

    def button_cancel(self, cr, uid, ids, context=None):

        val_history = {}
        ait_obj = self.pool.get('oemedical.appointment.history')

        self.write(cr, uid, ids, {'state':'canceled'} ,context=context)

        val_history['appointment_id_history'] = ids[0]
        val_history['name'] = uid
        val_history['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        val_history['action'] = "--------------------------------  Changed to Canceled  ------------------------------------\n"
        ait_obj.create(cr, uid, val_history)

        return True


OeMedicalAppointment()

class OeMedicalAppointment_history(osv.Model):
    _name = 'oemedical.appointment.history'

    _columns = {
        'appointment_id_history' :  fields.many2one('oemedical.appointment','History', ondelete='cascade'),
        'date': fields.datetime(string='Date and Time'),
        'name': fields.many2one('res.users', string='User', help=''),
	    'action' : fields.text('Action'),
    }
    
    _defaults = {
                 }

OeMedicalAppointment_history()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
