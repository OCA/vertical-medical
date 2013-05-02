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

class PatientPregnancy(osv.Model):
    
    _name = 'oemedical.patient.pregnancy'
    _description = 'Patient Pregnancy'
    _columns = {
                'name' : fields.many2one('oemedical.patient', 'Patient ID'),
                'gravida' : fields.integer('Pregnancy #', required=True),
                'warning' : fields.boolean('Warn', help='Check this box if this is pregancy is or was NOT normal'),
                'lmp' : fields.date('LMP', help="Last Menstrual Period", required=True),
#                'pdd' : fields.function(fields.date('Pregnancy Due Date'), 'get_pregnancy_data'),
                'prenatal_evaluations' : fields.one2many('oemedical.patient.prenatal.evaluation', 'name', 'Prenatal Evaluations'),
                'perinatal' : fields.one2many('oemedical.perinatal', 'name', 'Perinatal Info'),
                'puerperium_monitor' : fields.one2many('oemedical.puerperium.monitor', 'name', 'Puerperium monitor'),
                'current_pregnancy' : fields.boolean('Current Pregnancy', help='This field marks the current pregnancy'),
                'fetuses' : fields.integer('Fetuses', required=True),
                'monozygotic' : fields.boolean('Monozygotic'),
                'pregnancy_end_result' : fields.selection([
                                ('live_birth', 'Live birth'),
                                ('abortion', 'Abortion'),
                                ('stillbirth', 'Stillbirth'),
                                ('status_unknown', 'Status unknown'),
                                ], 'Result', sort=False,),
                'pregnancy_end_date' : fields.datetime('End of Pregnancy',),
#                'pregnancy_end_age' : fields.function(fields.Char('Weeks', help='Weeks at the end of pregnancy'), 'get_pregnancy_data'),
                'iugr' : fields.selection([
                                ('symmetric', 'Symmetric'),
                                ('assymetric', 'Assymetric'),
                                ], 'IUGR', sort=False),
                }

PatientPregnancy()

class PuerperiumMonitor(osv.Model):

    _name = 'oemedical.puerperium.monitor'
    _description = 'Puerperium Monitor'

    _columns = {
        'name' : fields.many2one('oemedical.patient', string='Patient ID'),
        'date' : fields.datetime('Date and Time', required=True),
        'systolic' : fields.integer('Systolic Pressure'),
        'diastolic' : fields.integer('Diastolic Pressure'),
        'frequency' : fields.integer('Heart Frequency'),
        'lochia_amount' : fields.selection([
            ('n', 'normal'),
            ('e', 'abundant'),
            ('h', 'hemorrhage'),
            ], 'Lochia amount', select=True),
        'lochia_color' : fields.selection([
            ('r', 'rubra'),
            ('s', 'serosa'),
            ('a', 'alba'),
            ], 'Lochia color', select=True),
        'lochia_odor' : fields.selection([
            ('n', 'normal'),
            ('o', 'offensive'),
            ], 'Lochia odor', select=True),
        'uterus_involution' : fields.integer('Fundal Height', help="Distance between the symphysis pubis and the uterine fundus (S-FD) in cm"),
        'temperature' : fields.float('Temperature'),
            }

PuerperiumMonitor()


class PerinatalMonitor(osv.Model):
    
    _name = 'oemedical.perinatal.monitor'
    _description = 'Perinatal monitor'
    _columns = {
            'name' : fields.many2one('oemedical.patient', string='patient_id'),
            'date' : fields.datetime('Date and Time'),
            'systolic' : fields.integer('Systolic Pressure'),
            'diastolic' : fields.integer('Diastolic Pressure'),
            'contractions' : fields.integer('Contractions'),
            'frequency' : fields.integer('Mother\'s Heart Frequency'),
            'dilation' : fields.integer('Cervix dilation'),
            'f_frequency' : fields.integer('Fetus Heart Frequency'),
            'meconium' : fields.boolean('Meconium'),
            'bleeding' : fields.boolean('Bleeding'),
            'fundal_height' : fields.integer('Fundal Height'),
            'fetus_position' : fields.selection([
                ('n', 'Correct'),
                ('o', 'Occiput / Cephalic Posterior'),
                ('fb', 'Frank Breech'),
                ('cb', 'Complete Breech'),
                ('t', 'Transverse Lie'),
                ('t', 'Footling Breech'),
                ], 'Fetus Position', select=True),
            }
PerinatalMonitor()


class OemedicalPerinatal(osv.Model):

    _name = 'oemedical.perinatal'
    _description =  'Perinatal Information'
    _columns={
            'name' : fields.many2one('oemedical.patient', string='Perinatal Infomation'),
            'admission_code' : fields.char('Admission Code', size=64),
            'gravida_number' : fields.integer('Gravida #'),
            'abortion' : fields.boolean('Abortion'),
            'admission_date' : fields.datetime('Admission date', help="Date when she was admitted to give birth"),
            'prenatal_evaluations' : fields.integer('Prenatal evaluations', help="Number of visits to the doctor during pregnancy"),
            'start_labor_mode' : fields.selection([
                ('n', 'Normal'),
                ('i', 'Induced'),
                ('c', 'c-section'),
                ], 'Labor mode', select=True),
            'gestational_weeks' : fields.integer('Gestational weeks'),
            'gestational_days' : fields.integer('Gestational days'),
            'fetus_presentation' : fields.selection([
                ('n', 'Correct'),
                ('o', 'Occiput / Cephalic Posterior'),
                ('fb', 'Frank Breech'),
                ('cb', 'Complete Breech'),
                ('t', 'Transverse Lie'),
                ('t', 'Footling Breech'),
                ], 'Fetus Presentation', select=True),
            'dystocia' : fields.boolean('Dystocia'),
            'placenta_incomplete' : fields.boolean('Incomplete Placenta'),
            'placenta_retained' : fields.boolean('Retained Placenta'),
            'episiotomy' : fields.boolean('Episiotomy'),
            'vaginal_tearing' : fields.boolean('Vaginal tearing'),
            'forceps' : fields.boolean('Use of forceps'),
            'monitoring' : fields.one2many('oemedical.perinatal.monitor', 'name', string='Monitors'),
            'puerperium_monitor' : fields.one2many('oemedical.puerperium.monitor', 'name','Puerperium monitor'),
            'medications': fields.one2many('oemedical.patient.medication','patient_id', string='Medications',),
            'dismissed' : fields.datetime('Dismissed from hospital'),
            'place_of_death' : fields.selection([
                ('ho', 'Hospital'),
                ('dr', 'At the delivery room'),
                ('hh', 'in transit to the hospital'),
                ('th', 'Being transferred to other hospital'),
                ], 'Place of Death'),
            'mother_deceased' : fields.boolean('Deceased', help="Mother died in the process"),
            'notes' : fields.text('Notes'),
            }
OemedicalPerinatal()


class OeMedicalPatient(osv.Model):

    _inherit='oemedical.patient'

    _columns = {
            'currently_pregnant' : fields.boolean('Currently Pregnant'),
#            'currently_pregnant' : fields.function(fields.Boolean('Pregnant'), 'get_pregnancy_info'),
            'fertile' : fields.boolean('Fertile', help="Check if patient is in fertile age"),
            'menarche' : fields.integer('Menarche age'),
            'menopausal' : fields.boolean('Menopausal'),
            'menopause' : fields.integer('Menopause age'),
            'mammography' : fields.boolean('Mammography', help="Check if the patient does periodic mammographys"),
            'mammography_last' : fields.date('Last mammography', help="Enter the date of the last mammography"),
            'breast_self_examination' : fields.boolean('Breast self-examination', help="Check if patient does and knows how to self examine her breasts"),
            'pap_test' : fields.boolean('PAP test',  help="Check if patient does periodic cytologic pelvic smear screening"),
            'pap_test_last' : fields.date('Last PAP test', help="Enter the date of the last Papanicolau test"),
            'colposcopy' : fields.boolean('Colposcopy', help="Check if the patient has done a colposcopy exam"),
            'colposcopy_last' : fields.date('Last colposcopy', help="Enter the date of the last colposcopy"),
            'gravida' : fields.integer('Gravida', help="Number of pregnancies"),
            'premature' : fields.integer('Premature', help="Premature Deliveries"),
            'abortions' : fields.integer('Abortions'),
            'stillbirths' : fields.integer('Stillbirths'),
            'full_term' : fields.integer('Full Term', help="Full term pregnancies"),
            'menstrual_history' : fields.one2many('oemedical.patient.menstrual_history', 'name', 'Menstrual History'),
            'mammography_history' : fields.one2many('oemedical.patient.mammography_history', 'name', 'Mammography History'),
            'pap_history' : fields.one2many('oemedical.patient.pap_history', 'name', 'PAP smear History'),
            'colposcopy_history' : fields.one2many('oemedical.patient.colposcopy_history', 'name', 'Colposcopy History'),
            'pregnancy_history' : fields.one2many('oemedical.patient.pregnancy', 'name', 'Pregnancies'),
            }

#    def get_pregnancy_info(self, name):
#        if name == 'currently_pregnant':
#            for pregnancy_history in self.pregnancy_history:
#                if pregnancy_history.current_pregnancy:
#                    return True
#        return False

OeMedicalPatient()


class PatientMenstrualHistory(osv.Model):

    _name = 'oemedical.patient.menstrual_history'
    _description =  'Menstrual History'
    _columns={
            'name' : fields.many2one('oemedical.patient', 'Patient', readonly=True, required=True),
            'evaluation' : fields.many2one('oemedical.patient.evaluation', 'Evaluation'),
            'evaluation_date' : fields.date('Date', help="Evaluation Date",  required=True),
            'lmp' : fields.date('LMP', help="Last Menstrual Period", required=True),
            'lmp_length' : fields.integer('Length', required=True),
            'is_regular' : fields.boolean('Regular'),
            'dysmenorrhea' : fields.boolean('Dysmenorrhea'),
            'frequency' : fields.selection([
                                    ('amenorrhea', 'amenorrhea'),
                                    ('oligomenorrhea', 'oligomenorrhea'),
                                    ('eumenorrhea', 'eumenorrhea'),
                                    ('polymenorrhea', 'polymenorrhea'),
                                    ], 'frequency', sort=False),
            'volume' : fields.selection([
                                    ('hypomenorrhea', 'hypomenorrhea'),
                                    ('normal', 'normal'),
                                    ('menorrhagia', 'menorrhagia'),
                                    ], 'volume', sort=False),

            }

PatientMenstrualHistory()


class PatientMammographyHistory(osv.Model):

    _name = 'oemedical.patient.mammography_history'
    _description =  'Mammography History'
    _columns={
            'name' : fields.many2one('oemedical.patient', 'Patient', readonly=True, required=True),
            'evaluation' : fields.many2one('oemedical.patient.evaluation', 'Evaluation'),
            'evaluation_date' : fields.date('Date', help=" Date"),
            'last_mammography' : fields.date('Date', help="Last Mammography", required=True),
            'result' : fields.selection([
                ('normal', 'normal'),
                ('abnormal', 'abnormal'),
                ], 'result', help="Please check the lab test results if the module is installed", sort=False),
            'comments' : fields.char('Remarks'),
            }

PatientMammographyHistory()


class PatientPAPHistory(osv.Model):

    _name = 'oemedical.patient.pap_history'
    _description =  'PAP Test History'
    _columns={
            'name' : fields.many2one('oemedical.patient', 'Patient', readonly=True, required=True),
            'evaluation' : fields.many2one('oemedical.patient.evaluation', 'Evaluation'),
            'evaluation_date' : fields.date('Date', help=" Date"),
            'last_pap' : fields.date('Date', help="Last Papanicolau", required=True),
            'result' : fields.selection([
                            ('negative', 'Negative'),
                            ('c1', 'ASC-US'),
                            ('c2', 'ASC-H'),
                            ('g1', 'ASG'),
                            ('c3', 'LSIL'),
                            ('c4', 'HSIL'),
                            ('g4', 'AIS'),
                            ], 'result', help="Please check the lab results if the module is installed", sort=False),
            'comments' : fields.char('Remarks'),
            }
PatientPAPHistory()


class PatientColposcopyHistory(osv.Model):

    _name = 'oemedical.patient.colposcopy_history'
    _description =  'Colposcopy History'
    _columns={
            'name' : fields.many2one('oemedical.patient', 'Patient', readonly=True, required=True),
            'evaluation' : fields.many2one('oemedical.patient.evaluation', 'Evaluation'),
            'evaluation_date' : fields.date('Date', help=" Date"),
            'last_colposcopy' : fields.date('Date', help="Last colposcopy", required=True),
            'result' : fields.selection([
                            ('normal', 'normal'),
                            ('abnormal', 'abnormal'),
                            ], 'result', help="Please check the lab test results if the module is installed", sort=False),
            'comments' : fields.char('Remarks'),
            }

PatientColposcopyHistory()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
