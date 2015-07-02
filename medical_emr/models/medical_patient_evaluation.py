# -*- coding: utf-8 -*-
###############################################################################
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
###############################################################################

from openerp.osv import fields, orm


class MedicalPatientEvaluation(orm.Model):
    _name = 'medical.patient.evaluation'
    _rec_name = 'patient_id'
    _columns = {
        'patient_id': fields.many2one('medical.patient', 'Patient'),
        'information_source': fields.char(
            size=256, string='Source',
            help="Source of" "Information, eg : Self, relative, friend ..."
        ),
        'info_diagnosis': fields.text(
            string='Presumptive Diagnosis: Extra Info'),
        'orientation': fields.boolean(
            string='Orientation',
            help='Check this box if the patient is disoriented in time and/or'
            ' space'
        ),
        'weight': fields.float(string='Weight',
                               help='Weight in Kilos'),
        'evaluation_type': fields.selection([
            ('a', 'Ambulatory'),
            ('e', 'Emergency'),
            ('i', 'Inpatient'),
            ('pa', 'Pre-arranged appointment'),
            ('pc', 'Periodic control'),
            ('p', 'Phone call'),
            ('t', 'Telemedicine'),
        ], string='Type'),
        'malnutrition': fields.boolean(
            string='Malnutrition',
            help='Check this box if the patient show signs of malnutrition. If'
            ' associated  to a disease, please encode the correspondent'
            ' disease on the patient disease history. For example, Moderate'
            ' protein-energy malnutrition, E44.0 in ICD-10 encoding'
        ),
        'actions': fields.one2many('medical.directions',
                                   'evaluation_id', string='Procedures',
                                   help='Procedures / Actions to take'),
        'height': fields.float(string='Height',
                               help='Height in centimeters, eg 175'),
        'dehydration': fields.boolean(
            string='Dehydration',
            help='Check this box if the patient show signs of dehydration. If'
            ' associated  to a disease, please encode the correspondent'
            ' disease on the patient disease history. For example,'
            ' Volume Depletion, E86 in ICD-10 encoding'
        ),
        'tag': fields.integer(
            string='Last TAGs',
            help='Triacylglycerol(triglicerides) level. Can be approximative'
        ),
        'tremor': fields.boolean(
            string='Tremor',
            help='If associated  to a disease, please encode it on the patient'
            ' disease history'
        ),
        'present_illness': fields.text(string='Present Illness'),
        'evaluation_date': fields.many2one(
            'medical.appointment', string='Appointment',
            help='Enter or select the date / ID of the appointment related to'
            ' this evaluation'
        ),
        'evaluation_start': fields.datetime(string='Start', required=True),
        'loc': fields.integer(string='Level of Consciousness'),
        'user_id': fields.many2one('res.users', string='Last Changed by',
                                   readonly=True),
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
        'doctor': fields.many2one('medical.physician', string='Doctor',
                                  readonly=True),
        'knowledge_current_events': fields.boolean(
            string='Knowledge of Current Events',
            help='Check this box if the patient can not respond to public'
            ' notorious events'),
        'next_evaluation': fields.many2one('medical.appointment',
                                           string='Next Appointment',),
        'signs_and_symptoms': fields.one2many(
            'medical.signs_and_symptoms', 'evaluation_id',
            string='Signs and Symptoms',
            help="Enter the Signs and Symptoms for the patient in this"
            " evaluation."
        ),
        'loc_motor': fields.selection([
            ('1', 'Makes no movement'),
            ('2', 'Extension to painful stimuli - decerebrate response -'),
            ('3',
             'Abnormal flexion to painful stimuli (decorticate response)'),
            ('4', 'Flexion / Withdrawal to painful stimuli'),
            ('5', 'Localizes painful stimuli'),
            ('6', 'Obeys commands'),
        ], string='Glasgow - Motor'),
        'reliable_info': fields.boolean(
            string='Reliable',
            help="Uncheck this option"
            "if the information provided by the source seems not reliable"
        ),
        'systolic': fields.integer(string='Systolic Pressure'),
        'vocabulary': fields.boolean(
            string='Vocabulary',
            help='Check this box if the patient lacks basic intelectual'
            ' capacity, when she/he can not describe elementary objects'
        ),
        'praxis': fields.boolean(
            string='Praxis',
            help='Check this box if the patient is unable to make voluntary'
            'movements'
        ),
        'hip': fields.float(string='Hip',
                            help='Hip circumference in centimeters, eg 100'),
        'memory': fields.boolean(
            string='Memory',
            help='Check this box if the patient has problems in short or long'
            ' term memory'
        ),
        'abstraction': fields.boolean(
            string='Abstraction',
            help='Check this box if the patient presents abnormalities in'
            ' abstract reasoning'
        ),
        'derived_from': fields.many2one('medical.physician',
                                        string='Derived from',
                                        help='Physician who derived the case'),
        'specialty': fields.many2one('medical.specialty',
                                     string='Specialty',),
        'loc_verbal': fields.selection([
            ('1', 'Makes no sounds'),
            ('2', 'Incomprehensible sounds'),
            ('3', 'Utters inappropriate words'),
            ('4', 'Confused, disoriented'),
            ('5', 'Oriented, converses normally'),
        ], string='Glasgow - Verbal'),
        'glycemia': fields.float(
            string='Glycemia',
            help='Last blood glucose level. Can be approximative.'
        ),
        'head_circumference': fields.float(string='Head Circumference',
                                           help='Head circumference'),
        'bmi': fields.float(string='Body Mass Index'),
        'respiratory_rate': fields.integer(
            string='Respiratory Rate',
            help='Respiratory rate expressed in breaths per minute'
        ),
        'derived_to': fields.many2one(
            'medical.physician', string='Derived to',
            help='Physician to whom escalate / derive the case'
        ),
        'hba1c': fields.float(
            string='Glycated Hemoglobin',
            help='Last Glycated Hb level. Can be approximative.'
        ),
        'violent': fields.boolean(
            string='Violent Behaviour',
            help='Check this box if the patient is agressive or violent at the'
            ' moment'
        ),
        'directions': fields.text(string='Plan'),
        'evaluation_summary': fields.text(string='Evaluation Summary'),
        'cholesterol_total': fields.integer(string='Last Cholesterol'),
        'diagnostic_hypothesis': fields.one2many(
            'medical.diagnostic_hypothesis',
            'evaluation_id', string='Hypotheses / DDx',
            help='Presumptive Diagnosis. If no diagnosis can be made'
            ', encode the main sign or symptom.'),
        'judgment': fields.boolean(
            string='Jugdment',
            help='Check this box if the patient can not interpret basic'
            ' scenario solutions'
        ),
        'temperature': fields.float(string='Temperature',
                                    help='Temperature in celcius'),
        'osat': fields.integer(string='Oxygen Saturation',
                               help='Oxygen Saturation(arterial).'),
        'secondary_conditions': fields.one2many(
            'medical.secondary_condition', 'evaluation_id',
            string='Secondary Conditions',
            help="Other, Secondary conditions found on the patient"),
        'evaluation_endtime': fields.datetime(string='End', required=True),
        'notes': fields.text(string='Notes'),
        'calculation_ability': fields.boolean(
            string='Calculation Ability',
            help='Check this box if the patient can not do simple arithmetic'
            ' problems'
        ),
        'bpm': fields.integer(string='Heart Rate',
                              help='Heart rate expressed in beats per minute'),
        'chief_complaint': fields.char(size=256, string='Chief Complaint',
                                       required=True,
                                       help='Chief Complaint'),
        'loc_eyes': fields.selection([
            ('1', 'Does not Open Eyes'),
            ('2', 'Opens eyes in response to painful stimuli'),
            ('3', 'Opens eyes in response to voice'),
            ('4', 'Opens eyes spontaneously'),
        ], string='Glasgow - Eyes'),
        'abdominal_circ': fields.float(string='Waist'),
        'object_recognition': fields.boolean(
            string='Object Recognition',
            help='Check this box if the patient suffers from any sort of'
            ' gnosia disorders, such as agnosia, prosopagnosia ...'
        ),
        'diagnosis': fields.many2one('medical.pathology',
                                     string='Presumptive Diagnosis',),
        'whr': fields.float(string='WHR', help='Waist to hip ratio'),
        'ldl': fields.integer(
            string='Last LDL',
            help='Last LDL Cholesterol reading. Can be approximative'
        ),
        'notes_complaint': fields.text(string='Complaint details'),
        'hdl': fields.integer(string='Last HDL'),
        'diastolic': fields.integer(string='Diastolic Pressure'),
    }



