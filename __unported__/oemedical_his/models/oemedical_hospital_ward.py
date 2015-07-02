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

from openerp.osv import fields, orm
from openerp.tools.translate import _


class OeMedicalHospitalWard(orm.Model):
    _name = 'oemedical.hospital.ward'

    _columns = {
        'building': fields.many2one('oemedical.hospital.building',
                                    string='Building', ),
        'ac': fields.boolean(string='Air Conditioning'),
        'name': fields.char(size=256, string='Name', required=True,
                            help='Ward / Room code'),
        'floor': fields.integer(string='Floor Number'),
        'tv': fields.boolean(string='Television'),
        'gender': fields.selection([('men', 'Men Ward'),
                                    ('women', 'Women Ward'),
                                    ('unisex', 'Unisex')],
                                   string='Gender', required=True),
        'unit': fields.many2one('oemedical.hospital.unit', string='Unit', ),
        'private_bathroom': fields.boolean(string='Private Bathroom'),
        'telephone': fields.boolean(string='Telephone access'),
        'microwave': fields.boolean(string='Microwave'),
        'guest_sofa': fields.boolean(string='Guest sofa-bed'),
        'state': fields.selection([
            ('beds_available', 'Beds available'),
            ('full', 'Full'),
            ('na', 'Not available'),
        ], string='Status'),
        'private': fields.boolean(string='Private',
                                  help='Check this option for private room'),
        'number_of_beds': fields.integer(string='Number of beds',
                                         help='Number of patients per ward'),
        'internet': fields.boolean(string='Internet Access'),
        'bio_hazard': fields.boolean(string='Bio Hazard',
                                     help='Check this option if there is biological hazard'),
        'institution': fields.many2one('res.partner', string='Institution',
                                       help='Medical Center'),
        'refrigerator': fields.boolean(string='Refrigetator'),
        'extra_info': fields.text(string='Extra Info'),
    }

OeMedicalHospitalWard()