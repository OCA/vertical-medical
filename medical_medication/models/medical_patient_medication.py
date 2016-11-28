# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPatientMedication(models.Model):
    _name = 'medical.patient.medication'
    _description = 'Medical Patient Medication'
    _inherit = ['abstract.medical.medication', 'medical.medication.template']
    _rec_name = 'patient_id'

    medication_template_id = fields.Many2one(
        string='Medication Template',
        comodel_name='medical.medication.template',
        index=True,
        help='Template to apply to this medication',
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        index=True,
        required=True,
        help='Patient that is taking this medication',
    )
    physician_id = fields.Many2one(
        string='Physician',
        comodel_name='medical.physician',
        index=True,
        help='Physician who prescribed the medicament',
    )
    active = fields.Boolean(
        help='Check if the patient is currently taking the medication',
        default=True,
    )
    is_course_complete = fields.Boolean(
        string='Course Completed',
        help='Check this if the patient is no longer taking this medication',
    )
    is_discontinued = fields.Boolean(
        help='Check this if the medication has been discontinued',
    )
    discontinued_reason = fields.Char(
        help='Short description explaining why the medication was'
             ' discontinued',
    )
    date_start_treatment = fields.Datetime(
        help='When the patient began taking this medication',
    )
    date_stop_treatment = fields.Datetime(
        help='When the patient is scheduled to stop this medication',
    )
    adverse_reaction = fields.Text(
        help='Side effects or adverse reactions that patient experienced',
    )
    notes = fields.Text(
        help='Any additional information regarding this treatment',
    )
