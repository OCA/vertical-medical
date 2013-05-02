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

class PuerperiumMonitor(osv.Model):

    _name = 'oemedical.puerperium.monitor'
    _description = 'Puerperium Monitor'

    _columns = {
        'name' : fields.many2one('oemedical.patient',
                                     string='Patient ID'),
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
        'uterus_involution' : fields.integer('Fundal Height',
            help="Distance between the symphysis pubis and the uterine fundus " \
            "(S-FD) in cm"),
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
#            'currently_pregnant' : fields.function(fields.Boolean('Pregnant'), 'get_pregnancy_info')
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
            'stillbirths' : fields.integer('Stillbirths')
            'full_term' : fields.integer('Full Term', help="Full term pregnancies"),
            'menstrual_history' : fields.one2many('oemedical.patient.menstrual_history', 'name', 'Menstrual History')
            'mammography_history' : fields.one2many('oemedical.patient.mammography_history', 'name', 'Mammography History')
            'pap_history' : fields.one2many('oemedical.patient.pap_history', 'name', 'PAP smear History')
            'colposcopy_history' : fields.one2many('oemedical.patient.colposcopy_history', 'name', 'Colposcopy History')
            'pregnancy_history' : fields.one2many('oemedical.patient.pregnancy', 'name', 'Pregnancies')
            }

    def get_pregnancy_info(self, name):
        if name == 'currently_pregnant':
            for pregnancy_history in self.pregnancy_history:
                if pregnancy_history.current_pregnancy:
                    return True
        return False

OeMedicalPatient()

class PatientMenstrualHistory(osv.Model):

    _name = 'oemedical.patient.menstrual_history'
    _description =  'Menstrual History'
    _columns={
            'name' : fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        domain=[('patient', '=', Eval('name'))])
    evaluation_date = fields.Date('Date', help="Evaluation Date",
        required=True)
    lmp = fields.Date('LMP', help="Last Menstrual Period", required=True)
    lmp_length = fields.Integer('Length', required=True)
    is_regular = fields.Boolean('Regular')
    dysmenorrhea = fields.Boolean('Dysmenorrhea')
    frequency = fields.Selection([
        ('amenorrhea', 'amenorrhea'),
        ('oligomenorrhea', 'oligomenorrhea'),
        ('eumenorrhea', 'eumenorrhea'),
        ('polymenorrhea', 'polymenorrhea'),
        ], 'frequency', sort=False)
    volume = fields.Selection([
        ('hypomenorrhea', 'hypomenorrhea'),
        ('normal', 'normal'),
        ('menorrhagia', 'menorrhagia'),
        ], 'volume', sort=False)

    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_frequency():
        return 'eumenorrhea'

    @staticmethod
    def default_volume():
        return 'normal'


class PatientMammographyHistory(ModelSQL, ModelView):
    'Mammography History'
    __name__ = 'gnuhealth.patient.mammography_history'

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        domain=[('patient', '=', Eval('name'))])
    evaluation_date = fields.Date('Date', help=" Date")
    last_mammography = fields.Date('Date', help="Last Mammography",
        required=True)
    result = fields.Selection([
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
        ], 'result', help="Please check the lab test results if the module is \
            installed", sort=False)
    comments = fields.Char('Remarks')

    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_last_mammography():
        return Pool().get('ir.date').today()


class PatientPAPHistory(ModelSQL, ModelView):
    'PAP Test History'
    __name__ = 'gnuhealth.patient.pap_history'

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        domain=[('patient', '=', Eval('name'))])
    evaluation_date = fields.Date('Date', help=" Date")
    last_pap = fields.Date('Date', help="Last Papanicolau", required=True)
    result = fields.Selection([
        ('negative', 'Negative'),
        ('c1', 'ASC-US'),
        ('c2', 'ASC-H'),
        ('g1', 'ASG'),
        ('c3', 'LSIL'),
        ('c4', 'HSIL'),
        ('g4', 'AIS'),
        ], 'result', help="Please check the lab results if the module is \
            installed", sort=False)
    comments = fields.Char('Remarks')

    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_last_pap():
        return Pool().get('ir.date').today()


class PatientColposcopyHistory(ModelSQL, ModelView):
    'Colposcopy History'
    __name__ = 'gnuhealth.patient.colposcopy_history'

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True,
        required=True)
    evaluation = fields.Many2One('gnuhealth.patient.evaluation', 'Evaluation',
        domain=[('patient', '=', Eval('name'))])
    evaluation_date = fields.Date('Date', help=" Date")
    last_colposcopy = fields.Date('Date', help="Last colposcopy",
        required=True)
    result = fields.Selection([
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
        ], 'result', help="Please check the lab test results if the module is \
            installed", sort=False)
    comments = fields.Char('Remarks')

    @staticmethod
    def default_evaluation_date():
        return Pool().get('ir.date').today()

    @staticmethod
    def default_last_colposcopy():
        return Pool().get('ir.date').today()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
