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


class OeMedicalPrescriptionOrder(osv.osv):
    _name = 'oemedical.prescription.order'

    _columns = {
        'patient': fields.many2one('oemedical.patient', string='Patient',
                                   required=True),
        'pregnancy_warning': fields.boolean(string='Pregancy Warning',
                                            readonly=True),
        'notes': fields.text(string='Prescription Notes'),
        'prescription_line': fields.one2many('oemedical.prescription.line',
                                             'prescription_order_id',
                                             string='Prescription line', ),
        'pharmacy': fields.many2one('res.partner', string='Pharmacy', ),
        'prescription_date': fields.datetime(string='Prescription Date'),
        'prescription_warning_ack': fields.boolean(
            string='Prescription verified'),
        'user_id': fields.many2one('res.users', string='Prescribing Doctor',
                                   required=True),
        'prescription_id': fields.char(size=256, string='Prescription ID',
                                       required=True,
                                    help='Type in the ID of this prescription'),
        'name': fields.char(size=256, string='Appointment ID', required=True),
    }
    
    _defaults = {
         'name': lambda obj, cr, uid, context: 
            obj.pool.get('ir.sequence').get(cr, uid, 
                                            'oemedical.prescription.order'),
                 }

OeMedicalPrescriptionOrder()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
