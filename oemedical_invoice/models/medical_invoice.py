# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010  Adrián Bernardi, Mario Puntin
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
from openerp.osv import fields, orm

import datetime
import time


class patient_data (orm.Model):
    _name = "medical.patient"
    _inherit = "medical.patient"

    _columns = {
        'receivable': fields.related(
            'name', 'credit', type='float',
            string='Receivable',
            readonly=True,
            help='Total amount this patient owes you'),
    }


# Add Invoicing information to the Appointment

class appointment (orm.Model):
    _name = "medical.appointment"
    _inherit = "medical.appointment"

    def copy(self, cr, uid, id, default=None, context=None):
        default.update({'validity_status': 'tobe'})
        return super(appointment, self).copy(cr, uid, id, default, context)

    def onchange_appointment_date(self, cr, uid, ids, apt_date):
        if apt_date:
            validity_date = datetime.datetime.fromtimestamp(
                time.mktime(time.strptime(apt_date, "%Y-%m-%d %H:%M:%S")))
            validity_date = validity_date + datetime.timedelta(days=7)
            v = {'appointment_validity_date': str(validity_date)}
            return {'value': v}
        return {}

    _columns = {
        'no_invoice': fields.boolean('Invoice exempt'),
        'appointment_validity_date': fields.datetime('Validity Date'),
        'validity_status': fields.selection(
            [('invoiced', 'Invoiced'),
             ('tobe', 'To be Invoiced')], 'Status'),
        'consultations': fields.many2one(
            'product.product', 'Consultation Service',
            domain=[('type', '=', "service")],
            help="Consultation Services", required=True),
    }
    _defaults = {
        'validity_status': lambda *a: 'tobe',
        'no_invoice': lambda *a: True
    }

# Add Invoicing information to the Lab Test


class labtest (orm.Model):
    _name = "medical.patient.lab.test"
    _inherit = "medical.patient.lab.test"

    _columns = {
        'no_invoice': fields.boolean('Invoice exempt'),
        'invoice_status': fields.selection(
            [('invoiced', 'Invoiced'),
             ('tobe', 'To be Invoiced')],
            'Invoice Status'),
    }

    _defaults = {
        'invoice_status': lambda *a: 'tobe',
        'no_invoice': lambda *a: True

    }


class patient_prescription_order (orm.Model):

    _name = "medical.prescription.order"
    _inherit = "medical.prescription.order"

    _columns = {
        'no_invoice': fields.boolean('Invoice exempt'),
        'invoice_status': fields.selection(
            [('invoiced', 'Invoiced'),
             ('tobe', 'To be Invoiced')],
            'Invoice Status'),
    }

    _defaults = {
        'invoice_status': lambda *a: 'tobe',
        'no_invoice': lambda *a: True
    }
