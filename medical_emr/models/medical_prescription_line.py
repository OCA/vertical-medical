# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Ported to 8.0 by Dave Lasley - LasLabs (https://laslabs.com)
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


class MedicalPrescriptionLine(orm.Model):
    _name = 'medical.prescription.line'



    def _get_medicament(self, cr, uid, ids, name, args, context=None):
        medication_obj = self.pool.get('medical.medication.template')
        result = {}

#        if name == 'form':
#            result = {'value': { 
#                        'form' : medication_obj.browse(cr, uid, medication, context = None).form.id ,
#                         } }
        return result

#    def _get_dose(self, cr, uid, ids, field_name, arg, context=None):
#        res = {}
#        for record in self.browse(cr, uid, ids, context=context):
#            res[record.id] = record.template.dose
#        return res

#    def _get_frecuency(self, cr, uid, ids, field_name, arg, context=None):
#        res = {}
#        for record in self.browse(cr, uid, ids, context=context):
#            res[record.id] = 1
#        return res


#    def _get_duration(self, cr, uid, ids, field_name, arg, context=None):
#        res = {}
#        for record in self.browse(cr, uid, ids, context=context):
#            res[record.id] = 1
#        return res

#    def _get_qty(self, cr, uid, ids, field_name, arg, context=None):
#        res = {}
#        for record in self.browse(cr, uid, ids, context=context):
#            res[record.id] = 1
#        return res

#    def _get_frecuency_unit(self, cr, uid, ids, field_name, arg, context=None):
#        res = {}
#        return res

#    def _get_admin_times(self, cr, uid, ids, name, args, context=None):
#        res = {}
#        return res

#    def _get_start_treatment(self, cr, uid, ids, field_name, arg, context=None):
#        ops = self.browse(cr, uid, ids, context=context)
#        res = {}
#        for op in ops:
#            res[op.id] = False
#        return res

#    def _get_end_treatment(self, cr, uid, ids, field_name, arg, context=None):
#        ops = self.browse(cr, uid, ids, context=context)
#        res = {}
#        for op in ops:
#            res[op.id] = False
#        return res

#    def _get_duration_period(self, cr, uid, ids, field_name, arg, context=None):
#        res = {}
#        for line in self.browse(cr, uid, ids, context=context):
#            res[line.id] = 'days'
#        return res

    def onchange_template(self, cr, uid, ids, medication, context=None):
        medication_obj = self.pool.get('medical.medication.template')
        res = {}
        res = {'value': { 
                        'indication' : medication_obj.browse(cr, uid, medication, context = None).indication.id ,
                        'form' : medication_obj.browse(cr, uid, medication, context = None).form.id ,
                        'route' : medication_obj.browse(cr, uid, medication, context = None).route.id ,
                        'dose' : medication_obj.browse(cr, uid, medication, context = None).dose ,
                        'dose_unit' : medication_obj.browse(cr, uid, medication, context = None).dose_unit.id ,
                        'qty' : medication_obj.browse(cr, uid, medication, context = None).qty ,
                        'admin_times' : medication_obj.browse(cr, uid, medication, context = None).admin_times ,
                        'common_dosage' : medication_obj.browse(cr, uid, medication, context = None).common_dosage.id ,
                        'frequency' : medication_obj.browse(cr, uid, medication, context = None).frequency ,
                        'frequency_unit' : medication_obj.browse(cr, uid, medication, context = None).frequency_unit ,
                         } }
        return res


    _columns = {
        'name': fields.many2one('medical.prescription.order', string='Prescription ID', ),
        'template': fields.many2one('medical.medication.template', string='Medication', ),
        'indication': fields.many2one('medical.pathology', string='Indication', help='Choose a disease for this medicament from the disease list. It'\
                        ' can be an existing disease of the patient or a prophylactic.'),
        'allow_substitution': fields.boolean(string='Allow substitution'),
        'prnt': fields.boolean(string='Print', help='Check this box to print this line of the prescription.'),
        'quantity': fields.integer(string='Units',  help="Number of units of the medicament. Example : 30 capsules of amoxicillin"),
        'active_component': fields.char(size=256, string='Active component', help='Active Component'),
        'start_treatment': fields.datetime(string='Start'),
        'end_treatment': fields.datetime(string='End'),
        'dose' : fields.float('Dose', digits=(16, 2), help="Amount of medication (eg, 250 mg) per dose"),
        'dose_unit': fields.many2one('product.uom', string='Dose Unit', help='Amount of medication (eg, 250 mg) per dose'),
        'qty' : fields.integer('x'),
        'form': fields.many2one('medical.drug.form', string='Form', help='Drug form, such as tablet or gel'),
        'route': fields.many2one('medical.drug.route', string='Route', help='Drug form, such as tablet or gel'),
        'common_dosage': fields.many2one('medical.medication.dosage', string='Frequency', help='Drug form, such as tablet or gel'),
	    'admin_times' : fields.char('Admin Hours', size=255),
        'frequency' : fields.integer('Frequency'),
        'frequency_unit': fields.selection([
                                (None, ''),
                                ('seconds', 'seconds'),
                                ('minutes', 'minutes'),
                                ('hours', 'hours'),
                                ('days', 'days'),
                                ('weeks', 'weeks'),
                                ('wr', 'when required'),
                                    ],'Unit'),
        'frequency_prn': fields.boolean(string='Frequency prn', help=''),
        'duration' : fields.integer('Treatment duration'),
        'duration_period': fields.selection([
                                (None, ''),
                                ('minutes', 'minutes'),
                                ('hours', 'hours'),
                                ('days', 'days'),
                                ('months', 'months'),
                                ('years', 'years'),
                                ('indefinite', 'indefinite'),
                                    ],'Treatment period'),
        'refills': fields.integer(string='Refills #'), 
        'review': fields.datetime(string='Review'),
        'short_comment': fields.char(size=256, string='Comment', help='Short comment on the specific drug'),

    }

    _defaults = {
        'prnt' : True,

                }



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
