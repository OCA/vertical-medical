# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class MedicalPatientDisease(models.Model):
    _name = 'medical.patient.disease'
    _description = 'Medical Patient Disease'

    name = fields.Char(compute='_compute_name', store=True)
    treatment_description = fields.Char()
    expire_date = fields.Datetime(compute='_compute_expire_date', store=True)
    short_comment = fields.Char()
    pathology_id = fields.Many2one(
        string='Pathology',
        comodel_name='medical.pathology',
        index=True,
        required=True,
        help='Pathology (disease type) that patient was diagnosed with.',
    )
    physician_id = fields.Many2one(
        string='Physician',
        comodel_name='medical.physician',
        index=True,
        help='Physician that diagnosed this disease.'
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        required=True,
        index=True,
        help='Patient that was diagnosed with this disease.'
    )
    disease_severity = fields.Selection([
        ('1_mi', 'Mild'),
        ('2_mo', 'Moderate'),
        ('3_sv', 'Severe')
    ],
        string='Severity',
        help='Level of severity of this disease.',
    )
    state = fields.Selection([
        ('a', 'Acute'),
        ('c', 'Chronic'),
        ('u', 'Unchanged'),
        ('h', 'Healed'),
        ('i', 'Improving'),
        ('w', 'Worsening'),
    ],
        string='Status',
        help='Status of this disease.',
    )
    allergy_type = fields.Selection([
        ('da', 'Drug Allergy'),
        ('fa', 'Food Allergy'),
        ('ma', 'Misc Allergy'),
        ('mc', 'Misc Contraindication'),
    ],
        help='If the disease is an allergy, indicate the type.',
    )
    weeks_of_pregnancy = fields.Integer(
        string='Pregnancy Week #',
        help='Indicate how far along the pregnancy was when patient was'
        ' diagnosed with this disease.',
    )
    age = fields.Integer(
        string='Age When Diagnosed',
        help='Age of the patient when diagnosed with this disease.',
    )
    active = fields.Boolean(
        default=True,
        help='Uncheck this box to deactivate.',
    )
    is_infectious = fields.Boolean(
        string='Infectious Disease',
        help='Check this box to indicate that the disease is likely to be'
        ' transmitted.',
    )
    is_allergy = fields.Boolean(
        string='Allergic Disease',
        help='Check this box to indicate that the disease is an allergy.',
    )
    is_pregnant = fields.Boolean(
        string='Pregnancy Warning',
        help='Check this box to indicate that the patient was pregnant at'
        ' the time of disease diagnosis.'
    )
    is_on_treatment = fields.Boolean(
        string='Currently on Treatment',
        help='Check this box if the patient is currently receiving treatment'
        ' for this disease',
    )
    treatment_start_date = fields.Date(
        help='If the patient is receiving treatment, document the start date'
        ' here.',
    )
    treatment_end_date = fields.Date(
        help='If the patient is/was receiving treament, document the end date'
        ' here.',
    )
    diagnosed_date = fields.Date(
        string='Date of Diagnosis',
        help='Document when the patient was diagnosed with this disease.',
    )
    healed_date = fields.Date(
        string='Date of Healing',
        help='Document when the patient was fully relieved of this disease.',
    )
    notes = fields.Text(
        help='Any additional information that may be helpful.',
    )

    @api.multi
    @api.depends('short_comment', 'pathology_id', 'pathology_id.name')
    def _compute_name(self):
        for rec_id in self:
            name = rec_id.pathology_id.name
            if rec_id.short_comment:
                name = '%s - %s' % (name, rec_id.short_comment)
            rec_id.name = name

    @api.multi
    @api.depends('active')
    def _compute_expire_date(self):
        for rec_id in self:
            if rec_id.active:
                rec_id.expire_date = False
            else:
                rec_id.expire_date = fields.Datetime.now()

    @api.multi
    def action_invalidate(self):
        for rec_id in self:
            rec_id.active = False

    @api.multi
    def action_revalidate(self):
        for rec_id in self:
            rec_id.active = True
