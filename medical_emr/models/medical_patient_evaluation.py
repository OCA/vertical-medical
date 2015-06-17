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


class MedicalPatientEvaluation(orm.Model):
    _name = 'medical.patient.evaluation'
    _rec_name = 'patient_id'

    # STATES = {'signed': [('readonly', True)]}

    _columns = {
        'patient_id': fields.many2one('medical.patient', 'Patient'),
        'appointment_id': fields.many2one('medical.appointment',
                                          domain="[('patient_id', '=', "
                                                 "patient_id)]",
                                          string='Appointment',
                                          help='Select the related appointment'
                                               ' for this evaluation'),
        'evaluation_start': fields.datetime(string='Start', required=True),
        'evaluation_endtime': fields.datetime(string='End', required=True),
        'state': fields.selection([
            ('in_progress', 'In progress'),
            ('done', 'Done'),
            ('signed', 'Signed'),
        ], string='State', index=True, readonly=True),

        'next_appointment': fields.many2one('medical.appointment',
                                            string='Next Appointment', ),
        'physician_id': fields.many2one('medical.physician',
                                        string='Physician',
                                        readonly=True),
        'specialty': fields.many2one('medical.specialty',
                                     string='Specialty', ),
        'visit_type': fields.selection([
            (None, ''),
            ('new', 'New health condition'),
            ('followup', 'Followup'),
            ('chronic', 'Chronic condition checkup'),
            ('well_child', 'Well Child visit'),
            ('well_woman', 'Well Woman visit'),
            ('well_man', 'Well Man visit'),
            ], string='Visit'),
        'urgency': fields.selection([
            (None, ''),
            ('a', 'Normal'),
            ('b', 'Urgent'),
            ('c', 'Medical Emergency'),
            ], string='Urgency'),
        'information_source': fields.char(size=256, string='Source',
                                          help='Source of Information, eg : '
                                               'Self, relative, friend ...'),
        'reliable_info': fields.boolean(string='Reliable',
                                        help='Uncheck this option '
                                             'if the information provided by '
                                             'the source seems not reliable'),
        'derived_from': fields.many2one('medical.physician',
                                        string='Derived from',
                                        help='Physician who derived the case'),
        'derived_to': fields.many2one('medical.physician',
                                      string='Derived to',
                                      help='Physician to whom escalate / '
                                           'derive the case'),
        'evaluation_type': fields.selection([
            (None, ''),
            ('ambulatory', 'Ambulatory'),
            ('outpatient', 'Outpatient'),
            ('inpatient', 'Inpatient'),
        ], string='Type'),
        'chief_complaint': fields.char(size=256, string='Chief Complaint',
                                       required=True,
                                       help='Chief Complaint'),
        'notes_complaint': fields.text(string='Complaint details'),
        'present_illness': fields.text(string='Present Illness'),

        'evaluation_summary': fields.text(string='Evaluation Summary'),
        'glycemia': fields.float(string='Glycemia',
                                 help='Last blood glucose level. Can be '
                                      'approximative.'),
        'hba1c': fields.float(string='Glycated Hemoglobin',
                              help='Last Glycated Hb level. '
                                   'Can be approximative'),
        'cholesterol_total': fields.integer(string='Last Cholesterol'),
        'hdl': fields.integer(string='Last HDL'),
        'ldl': fields.integer(string='Last LDL',
                              help='Last LDL Cholesterol reading. Can be '
                                   'approximative'),
        'tag': fields.integer(string='Last TAGs',
                              help='Triacylglycerol(triglicerides) level. '
                                   'Can be approximative'),
        'systolic': fields.integer(string='Systolic Pressure'),
        'diastolic': fields.integer(string='Diastolic Pressure'),
        'bpm': fields.integer(string='Heart Rate',
                              help='Heart rate expressed in beats per minute'),
        'respiratory_rate': fields.integer(string='Respiratory Rate',
                                           help='Respiratory rate expressed '
                                                'in breaths per minute'),
        'osat': fields.integer(string='Oxygen Saturation',
                               help='Oxygen Saturation(arterial).'),
        'malnutrition': fields.boolean(string='Malnutrition',
                                       help='Check this box if the patient '
                                            'show signs of malnutrition. If '
                                            'associated  to a disease, please '
                                            'encode the correspondent disease '
                                            'on the patient disease history. '
                                            'For example, Moderate '
                                            'protein-energy malnutrition, '
                                            'E44.0 in ICD-10 encoding'),
        'dehydration': fields.boolean(string='Dehydration',
                                      help='Check this box if the patient '
                                           'show signs of dehydration. If '
                                           'associated  to a disease, please '
                                           'encode the  correspondent disease '
                                           'on the patient disease history. '
                                           'For example, Volume Depletion, '
                                           'E86 in ICD-10 encoding'),
        'temperature': fields.float(string='Temperature',
                                    help='Temperature in celcius'),
        'weight': fields.float(string='Weight',
                               help='Weight in Kilos'),
        'height': fields.float(string='Height',
                               help='Height in centimeters, eg 175'),
        'bmi': fields.float(string='Body Mass Index'),
        'head_circumference': fields.float(string='Head Circumference',
                                           help='Head circumference'),
        'abdominal_circ': fields.float(string='Waist'),
        'hip': fields.float(string='Hip',
                            help='Hip circumference in centimeters, eg 100'),
        'whr': fields.float(string='WHR', help='Waist to hip ratio'),
        'loc': fields.integer(string='Level of Consciousness',
                              help='Level of Consciousness - on Glasgow Coma '
                                   'Scale :  < 9 severe - 9-12 Moderate, '
                                   '> 13 minor',),
        'loc_eyes': fields.selection([
            ('1', 'Does not Open Eyes'),
            ('2', 'Opens eyes in response to painful stimuli'),
            ('3', 'Opens eyes in response to voice'),
            ('4', 'Opens eyes spontaneously'),
        ], string='Glasgow - Eyes'),
        'loc_verbal': fields.selection([
            ('1', 'Makes no sounds'),
            ('2', 'Incomprehensible sounds'),
            ('3', 'Utters inappropriate words'),
            ('4', 'Confused, disoriented'),
            ('5', 'Oriented, converses normally'),
        ], string='Glasgow - Verbal'),
        'loc_motor': fields.selection([
            ('1', 'Makes no movement'),
            ('2', 'Extension to painful stimuli - decerebrate response -'),
            ('3',
             'Abnormal flexion to painful stimuli (decorticate response)'),
            ('4', 'Flexion / Withdrawal to painful stimuli'),
            ('5', 'Localizes painful stimuli'),
            ('6', 'Obeys commands'),
        ], string='Glasgow - Motor'),
        'tremor': fields.boolean(string='Tremor',
                                 help='If associated  to a disease, please '
                                      'encode it on the patient'
                                      ' disease history'),
        'violent': fields.boolean(string='Violent Behaviour',
                                  help='Check this box if the patient is '
                                       'agressive or violent at the moment'),
        'mood': fields.selection([
            ('n', 'Normal'),
            ('s', 'Sad'),
            ('f', 'Fear'),
            ('r', 'Rage'),
            ('h', 'Happy'),
            ('d', 'Disgust'),
            ('e', 'Euphoria'),
            ('fl', 'Flat'),
        ], string='Mood'),
        'orientation': fields.boolean(string='Orientation',
                                      help='Check this box if the patient is '
                                           'disoriented in time and/or'
                                           ' space'),
        'memory': fields.boolean(string='Memory',
                                 help='Check this box if the patient has '
                                      'problems in short or long term memory'),
        'knowledge_current_events': fields.boolean(
            string='Knowledge of Current Events',
            help='Check this box if the patient can not respond to public'
                 ' notorious events'),
        'judgment': fields.boolean(string='Jugdment',
                                   help='Check this box if the patient can not'
                                        ' interpret basic scenario solutions'),
        'abstraction': fields.boolean(string='Abstraction',
                                      help='Check this box if the patient '
                                           'presents abnormalities in abstract'
                                           ' reasoning'),
        'vocabulary': fields.boolean(string='Vocabulary',
                                     help='Check this box if the patient '
                                          'lacks basic intelectual capacity, '
                                          'when she/he can not describe '
                                          'elementary objects'),
        'calculation_ability': fields.boolean(string='Calculation Ability',
                                              help='Check this box if the '
                                                   'patient can not do simple '
                                                   'arithmetic problems'),
        'object_recognition': fields.boolean(string='Object Recognition',
                                             help='Check this box if the '
                                                  'patient suffers from any '
                                                  'sort of gnosia disorders, '
                                                  'such as agnosia, '
                                                  'prosopagnosia ...'),
        'praxis': fields.boolean(string='Praxis',
                                 help='Check this box if the patient is unable'
                                      ' to make voluntary movements'),
        'diagnosis': fields.many2one('medical.pathology',
                                     string='Presumptive Diagnosis', ),
        'secondary_conditions': fields.one2many(
            'medical.secondary.condition', 'evaluation_id',
            string='Secondary Conditions',
            help="Other, Secondary conditions found on the patient"),
        'diagnostic_hypothesis': fields.one2many(
            'medical.diagnostic_hypothesis',
            'evaluation_id', string='Hypotheses / DDx',
            help='Presumptive Diagnosis. If no diagnosis can be made'
                 ', encode the main sign or symptom.'),
        'signs_and_symptoms': fields.one2many('medical.signs_and_symptoms',
                                              'evaluation_id',
                                              string='Signs and Symptoms',
                                              help='Enter the Signs and '
                                                   'Symptoms for the patient '
                                                   'in this evaluation.'),
        'info_diagnosis': fields.text(
            string='Presumptive Diagnosis: Extra Info'),
        'directions': fields.text(string='Plan'),
        'actions': fields.one2many('medical.directions',
                                   'evaluation_id', string='Procedures',
                                   help='Procedures / Actions to take'),
        'notes': fields.text(string='Notes'),
        'user_id': fields.many2one('res.users', 'Responsible',
                                   track_visibility='onchange'),
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
