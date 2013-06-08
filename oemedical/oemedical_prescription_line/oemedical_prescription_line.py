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


class OeMedicalPrescriptionLine(osv.Model):
    _name = 'oemedical.prescription.line'

    def _get_medicament(self, cr, uid, ids, name, args, context=None):
        print '_get_medicament', name, args, context
        result = {}
        return result

    def _get_dose(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = record.template.dose
        return res

    def _get_frecuency(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = 1
        return res


    def _get_duration(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = 1
        return res

    def _get_qty(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = 1
        return res

    def _get_frecuency_unit(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        return res

    def _get_admin_times(self, cr, uid, ids, name, args, context=None):
        res = {}
        return res

    def _get_start_treatment(self, cr, uid, ids, field_name, arg, context=None):
        ops = self.browse(cr, uid, ids, context=context)
        res = {}
        for op in ops:
            res[op.id] = False
        return res

    def _get_end_treatment(self, cr, uid, ids, field_name, arg, context=None):
        ops = self.browse(cr, uid, ids, context=context)
        res = {}
        for op in ops:
            res[op.id] = False
        return res

    def _get_duration_period(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = 'days'
        return res

    _columns = {
        'name': fields.integer(string='Refills #'), 
        'prescription_order_id': fields.many2one('oemedical.prescription.order', string='Prescription ID', ),
        'review': fields.datetime(string='Review'),
        'short_comment': fields.char(size=256, string='Comment', help='Short comment on the specific drug'),
        'template': fields.many2one('oemedical.medication.template', string='Medication', ),
        'allow_substitution': fields.boolean(string='Allow substitution'),
        'prnt': fields.boolean(string='Print', help='Check this box to print this line of the prescription.'),
        'quantity': fields.integer(string='Units',  help="Number of units of the medicament. Example : 30 capsules of amoxicillin"),
        'medicament': fields.function(_get_medicament, type='many2one', relation="oemedical.medicament", string='Medicament', help="", multi=False),
        'indication': fields.function(_get_medicament, type='many2one', relation="oemedical.pathology", string='Indication', help="", multi=False),
        'start_treatment': fields.function(_get_medicament, type='datetime',  string='Start', help="", multi=False),
        'end_treatment': fields.function(_get_medicament, type='datetime',  string='End', help="", multi=False),
        'dose': fields.function(_get_dose, type='float',  string='Dose', help="Amount of medication (eg, 250 mg) per dose", multi=False),
        'dose_unit' : fields.function(_get_medicament, type='many2one', relation="oemedical.dose.unit", string='Dose Unit', help="", multi=False),
        'qty': fields.function(_get_qty, type='integer',  string='X', help="", multi=False),
        'form': fields.function(_get_medicament, type='many2one', relation="oemedical.drug.form", string='Form', help="", multi=False),
        'route': fields.function(_get_medicament, type='many2one', relation="oemedical.drug.route", string='Route', help="", multi=False),
        'common_dosage': fields.function(_get_medicament, type='many2one', relation="oemedical.medication.dosage", string='Frecuency', help="", multi=False),
        'admin_times': fields.function(_get_admin_times, type='char', string='Admin Hours', help="", multi=False),
        'frequency': fields.function(_get_frecuency, type='integer',  string='Frecuency', help="", multi=False),
        'frequency_unit': fields.function(_get_frecuency_unit, string='Unit', type='selection', selection=[
                                (None, ''),
                                ('seconds', 'seconds'),
                                ('minutes', 'minutes'),
                                ('hours', 'hours'),
                                ('days', 'days'),
                                ('weeks', 'weeks'),
                                ('wr', 'when required'),
                                    ]),
        'frequency_prn': fields.function(_get_medicament, type='boolean',  string='PRN', help="", multi=False),
        'duration': fields.function(_get_duration, type='integer',  string='Treatment duration', help="", multi=False),
        'duration_period': fields.function(_get_duration_period, string='Treatment period', type='selection', selection=[
                                (None, ''),
                                ('minutes', 'minutes'),
                                ('hours', 'hours'),
                                ('days', 'days'),
                                ('months', 'months'),
                                ('years', 'years'),
                                ('indefinite', 'indefinite'),
                                    ]),
    }

    _defaults = {
        'prnt' : True,

                }


OeMedicalPrescriptionLine()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
