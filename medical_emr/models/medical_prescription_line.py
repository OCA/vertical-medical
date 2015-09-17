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


class MedicalPrescriptionLine(orm.Model):
    _name = 'medical.prescription.line'

    def _get_medicament(self, cr, uid, ids, name, args, context=None):
        result = {}
        return result

    def onchange_template(self, cr, uid, ids, medication, context=None):
        medication_obj = self.pool.get('medical.medication.template')
        medication_template = medication_obj.browse(cr, uid, medication,
                                                    context=None)
        res = {'value': {
            'disease_id': medication_template.disease_id.id,
            'drug_form_id': medication_template.drug_form_id.id,
            'drug_route_id': medication_template.drug_route_id.id,
            'dose': medication_template.dose,
            'dose_unit_id': medication_template.dose_unit_id.id,
            'qty': medication_template.qty,
            'admin_times': medication_template.admin_times,
            'common_dose_id': medication_template.common_dosage_id.id,
            'frequency': medication_template.frequency,
            'frequency_unit': medication_template.frequency_unit,
        }}
        return res

    _columns = {
        'prescription_id': fields.many2one('medical.prescription.order',
                                           string='Prescription ID', ),
        'template_id': fields.many2one('medical.medication.template',
                                       string='Medication', ),
        'disease_id': fields.many2one(
            'medical.pathology', string='Indication',
            help='Choose a disease for this medicament from the disease list. '
            'It can be an existing disease of the patient or a prophylactic.'),
        'is_substitutable': fields.boolean(string='Allow substitution'),
        'is_printed': fields.boolean(
            string='Print',
            help='Check this box to print this line of the prescription.'),
        'quantity': fields.integer(string='Units',
                                   help='Number of units of the medicament. '
                                   'Example: 30 capsules of amoxicillin'),
        'active_component': fields.char(size=256, string='Active component',
                                        help='Active Component'),
        'start_treatment': fields.datetime(string='Start'),
        'end_treatment': fields.datetime(string='End'),
        'dose': fields.float('Dose', digits=(16, 2),
                             help='Amount of medication (eg, 20 mg) per dose'),
        'dose_unit_id': fields.many2one('product.uom',
                                        string='Dose Unit',
                                        help='Amount of ' +
                                        'medication (eg, 250 mg) '
                                        'per dose'),
        'qty': fields.integer('x'),
        'drug_form_id': fields.many2one('medical.drug.form', string='Form',
                                        help='Drug form, ' +
                                        'such as tablet or gel'),
        'drug_route_id': fields.many2one('medical.drug.route', string='Route',
                                         help='Drug form, ' +
                                         'such as tablet or gel'),
        'common_dose_id': fields.many2one(
            'medical.medication.dosage', string='Frequency',
            help='Drug form, such as pill or gel'),
        'admin_times': fields.char('Admin Hours', size=255),
        'frequency': fields.integer('Frequency'),
        'frequency_unit': fields.selection([
            (None, ''),
            ('seconds', 'seconds'),
            ('minutes', 'minutes'),
            ('hours', 'hours'),
            ('days', 'days'),
            ('weeks', 'weeks'),
            ('wr', 'when required'),
        ], 'Unit'),
        'frequency_prn': fields.boolean(string='Frequency prn', help=''),
        'duration': fields.integer('Treatment duration'),
        'duration_period': fields.selection([
            (None, ''),
            ('minutes', 'minutes'),
            ('hours', 'hours'),
            ('days', 'days'),
            ('months', 'months'),
            ('years', 'years'),
            ('indefinite', 'indefinite'),
        ], 'Treatment period'),
        'refills': fields.integer(string='Refills #'),
        'review': fields.datetime(string='Review'),
        'short_comment': fields.char(size=256, string='Comment',
                                     help='Short comment on the specific '
                                          'drug'),

    }

    _defaults = {
        'is_printed': True,

    }
