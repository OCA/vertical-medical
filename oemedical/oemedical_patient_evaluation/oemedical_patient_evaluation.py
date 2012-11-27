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


class OeMedicalPatientEvaluation(osv.osv):
    _name = 'oemedical.patient.evaluation'

    _columns = {
        'information_source': fields.char(size=256, string='Source', required=True),
        'info_diagnosis': fields.text(string='Presumptive Diagnosis: Extra Info'),
        'orientation': fields.boolean(string='Orientation'),
        'weight': fields.float(string='Weight'),
        #'evaluation_type': fields.selection([], string='Type'),
        'malnutrition': fields.boolean(string='Malnutrition'),
        #'actions': fields.one2many('oemedical.directions', 'relation_id', string='Procedures', ),
        'height': fields.float(string='Height'),
        'dehydration': fields.boolean(string='Dehydration'),
        'tag': fields.integer(string='Last TAGs'),
        'tremor': fields.boolean(string='Tremor'),
        'present_illness': fields.text(string='Present Illness'),
        'evaluation_date': fields.many2one('oemedical.appointment', string='Appointment', ),
        'evaluation_start': fields.datetime(string='Start'),
        'loc': fields.integer(string='Level of Consciousness'),
        'user_id': fields.many2one('res.users', string='Last Changed by', ),
        #'mood': fields.selection([], string='Mood'),
        'doctor': fields.many2one('oemedical.physician', string='Doctor', ),
        'knowledge_current_events': fields.boolean(string='Knowledge of Current Events'),
        'next_evaluation': fields.many2one('oemedical.appointment', string='Next Appointment', ),
        #'signs_and_symptoms': fields.one2many('oemedical.signs_and_symptoms', 'relation_id', string='Signs and Symptoms', ),
        #'loc_motor': fields.selection([], string='Glasgow - Motor'),
        'reliable_info': fields.boolean(string='Reliable'),
        'systolic': fields.integer(string='Systolic Pressure'),
        'vocabulary': fields.boolean(string='Vocabulary'),
        'praxis': fields.boolean(string='Praxis'),
        'hip': fields.float(string='Hip'),
        'memory': fields.boolean(string='Memory'),
        'abstraction': fields.boolean(string='Abstraction'),
        'patient': fields.many2one('oemedical.patient', string='Patient', ),
        'derived_from': fields.many2one('oemedical.physician', string='Derived from', ),
        'specialty': fields.many2one('oemedical.specialty', string='Specialty', ),
        #'loc_verbal': fields.selection([], string='Glasgow - Verbal'),
        'glycemia': fields.float(string='Glycemia'),
        'head_circumference': fields.float(string='Head Circumference'),
        'bmi': fields.float(string='Body Mass Index'),
        'respiratory_rate': fields.integer(string='Respiratory Rate'),
        'derived_to': fields.many2one('oemedical.physician', string='Derived to', ),
        'hba1c': fields.float(string='Glycated Hemoglobin'),
        'violent': fields.boolean(string='Violent Behaviour'),
        'directions': fields.text(string='Plan'),
        'evaluation_summary': fields.text(string='Evaluation Summary'),
        'cholesterol_total': fields.integer(string='Last Cholesterol'),
        #'diagnostic_hypothesis': fields.one2many('oemedical.diagnostic_hypothesis', 'relation_id', string='Hypotheses / DDx', ),
        'judgment': fields.boolean(string='Jugdment'),
        'temperature': fields.float(string='Temperature'),
        'rec_name': fields.char(size=256, string='Name', required=True),
        'osat': fields.integer(string='Oxygen Saturation'),
        #'secondary_conditions': fields.one2many('oemedical.secondary_condition', 'relation_id', string='Secondary Conditions', ),
        'evaluation_endtime': fields.datetime(string='End'),
        'notes': fields.text(string='Notes'),
        'calculation_ability': fields.boolean(string='Calculation Ability'),
        'bpm': fields.integer(string='Heart Rate'),
        'chief_complaint': fields.char(size=256, string='Chief Complaint', required=True),
        #'loc_eyes': fields.selection([], string='Glasgow - Eyes'),
        'abdominal_circ': fields.float(string='Waist'),
        'object_recognition': fields.boolean(string='Object Recognition'),
        'diagnosis': fields.many2one('oemedical.pathology', string='Presumptive Diagnosis', ),
        'whr': fields.float(string='WHR'),
        'ldl': fields.integer(string='Last LDL'),
        'notes_complaint': fields.text(string='Complaint details'),
        'hdl': fields.integer(string='Last HDL'),
        'diastolic': fields.integer(string='Diastolic Pressure'),
    }

OeMedicalPatientEvaluation()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
