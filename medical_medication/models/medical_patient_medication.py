# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, _


class MedicalPatientMedication(models.Model):
    _name = 'medical.patient.medication'
    _description = 'Medical Patient Medication'
    _inherit = ['abstract.medical.medication', 'medical.medication.template']
    _rec_name = 'patient_id'

    medication_template_id = fields.Many2one(
        string='Medication Template',
        comodel_name='medical.medication.template',
        index=True,
        help=_('Template to apply to this medication'),
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        index=True,
        required=True,
        help=_('Patient that is taking this medication'),
    )
    physician_id = fields.Many2one(
        string='Physician',
        comodel_name='medical.physician',
        index=True,
        help=_('Physician who prescribed the medicament'),
    )
    active = fields.Boolean(
        help=_('Check if the patient is currently taking the medication'),
        default=True,
    )
    is_course_complete = fields.Boolean(
        string='Course Completed',
        help=_(
            'Check this if the patient is no longer taking this medication'
        ),
    )
    is_discontinued = fields.Boolean(
        help=_('Check this if the medication has been discontinued'),
    )
    discontinued_reason = fields.Char(
        help=_(
            'Short description explaining why the medication was discontinued'
        ),
    )
    date_start_treatment = fields.Datetime(
        help=_('When the patient began taking this medication'),
    )
    date_stop_treatment = fields.Datetime(
        help=_('When the patient is scheduled to stop this medication'),
    )
    adverse_reaction = fields.Text(
        help=_('Side effects or adverse reactions that patient experienced'),
    )
    notes = fields.Text(
        help=_('Any additional information regarding this treatment'),
    )
