# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp.osv import fields, orm


class MedicalMedicationTemplate(orm.Model):
    _name = 'medical.medication.template'

    def _get_name(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = record.medicament_id.name
        return res

    _columns = {
        'medicament_id': fields.many2one('medical.medicament',
                                         string='Medicament', requered=True,
                                         help='Product Name',
                                         ondelete='cascade'),
        'name': fields.function(_get_name, type='char', string='Medicament',
                                help="", multi=False),
        'disease_id': fields.many2one('medical.pathology', string='Indication',
                                      help='Choose a disease for this '
                                           'medicament from the disease list. '
                                           'It can be an existing disease of '
                                           'the patient or a prophylactic.'),
        'start_treatment': fields.datetime(string='Start',
                                           help='Date of start of Treatment'),
        'end_treatment': fields.datetime(string='End',
                                         help='Date of start of Treatment'),
        'drug_form_id': fields.many2one('medical.drug.form', string='Form',
                                        help='Drug form, ' +
                                        'such as tablet or gel'),
        'drug_route_id': fields.many2one('medical.drug.route',
                                         string='Administration ' +
                                         'Route',
                                         help='Drug administration ' +
                                         'route code.'),
        'duration_period': fields.selection([
            ('minutes', 'minutes'),
            ('hours', 'hours'),
            ('days', 'days'),
            ('months', 'months'),
            ('years', 'years'),
            ('indefinite', 'indefinite'),
        ], string='Treatment period',
            help='Period that the patient must take the medication in minutes,'
                 'hours, days, months, years or indefinately'),
        'qty': fields.integer(string='x',
                              help='Quantity of units (eg, 2 capsules) of the '
                                   'medicament'),
        'frequency_unit': fields.selection([
            ('seconds', 'seconds'),
            ('minutes', 'minutes'),
            ('hours', 'hours'),
            ('days', 'days'),
            ('weeks', 'weeks'),
            ('wr', 'when required'),
        ], string='unit'),
        'dose': fields.float(string='Dose', help='Amount of medication (eg, '
                                                 '250 mg) per dose'),
        'duration': fields.integer(string='Treatment duration',
                                   help='Period that the patient must take the'
                                        ' medication. in minutes,'
                                        ' hours, days, months, years or '
                                        'indefinately'),
        'frequency_prn': fields.boolean(string='PRN',
                                        help='Use it as needed, pro re nata'),
        'frequency': fields.integer(string='Frequency',
                                    help='Time in between doses the patient '
                                         'must wait (ie, for 1 pill '
                                         'each 8 hours, put here 8 and select '
                                         '\"hours\" in the unit field'),
        'common_dose_id': fields.many2one('medical.medication.dosage',
                                          string='Frequency',
                                          help='Common / standard dosage '
                                          'frequency for this medicament'),
        'admin_times': fields.char(size=256, string='Admin hours',
                                   help='Suggested administration hours. '
                                        'For example, at 08:00, 13:00 and '
                                        '18:00 can be encoded like 08 13 18'),
        'dose_unit_id': fields.many2one(
            'product.uom', help='Unit of measure for that the medication is '
            'dosed in.'),
    }
