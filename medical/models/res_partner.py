# -*- coding: utf-8 -*-
# #############################################################################
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
# #############################################################################

from openerp.osv import fields, orm


class ResPartner(orm.Model):
    _inherit = 'res.partner'

    _columns = {
        'relationship': fields.char(size=256, string='Relationship'),
        'is_institution': fields.boolean(string='Institution',
                                         help='Check if the party is a '
                                         'Medical Center'),
        'relative_id': fields.many2one('res.partner', string='Contact', ),
        'is_doctor': fields.boolean(string='Health Prof',
                                    help='Check if the party is a health '
                                    'professional'),
        'is_patient': fields.boolean(string='Patient',
                                     help='Check if the party is a patient'),
        'alias': fields.char(size=256, string='Alias',
                             help='Common name that the Party is reffered'),
        'activation_date': fields.date(string='Activation date',
                                       help='Date of activation of the party'),
        'lastname': fields.char(size=256, string='Last Name',
                                help='Last Name'),
        'is_work': fields.boolean(string='Work'),
        'is_person': fields.boolean(string='Person',
                                    help='Check if the party is a person.'),
        'is_school': fields.boolean(string='School'),
        'is_pharmacy': fields.boolean(string='Pharmacy',
                                      help='Check if the party is a Pharmacy'),
        'ref': fields.char(size=256, string='ID/SSN',
                           help='Patient Social Security Number or '
                           'equivalent'),
        'patient_ids': fields.one2many(
            'medical.patient', fields_id='medical_center_id',
            string='Related Patients'),
    }
