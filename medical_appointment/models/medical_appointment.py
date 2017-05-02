# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models, exceptions, api, _
from datetime import timedelta


class MedicalAppointment(models.Model):
    _name = 'medical.appointment'
    _description = 'Medical Appointments'
    _inherit = 'mail.thread'

    STATES = {
        'draft': [('readonly', False)]
    }

    user_id = fields.Many2one(
        string='Responsible',
        help='User that created appointment',
        comodel_name='res.users',
        readonly=True,
        states=STATES,
        default=lambda s: s.env.user,
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        required=True,
        select=True,
        help='Patient Name',
    )
    name = fields.Char(
        string='Appointment ID',
        default='/',
        readonly=True,
    )
    force_schedule = fields.Boolean(
        help='Check this to ignore any double bookings and schedule anyways',
    )
    appointment_date = fields.Datetime(
        string='Date and Time',
        select=True,
        required=True,
        help='Date and Time of Scheduled Appointment'
    )
    appointment_end_date = fields.Datetime(
        string='End Date and Time',
        readonly=True,
        select=True,
        store=True,
        compute='_compute_appointment_end_date',
    )
    date_end = fields.Datetime(
        string='Stop Displaying On',
        help='When to stop displaying appointment',
    )
    duration = fields.Float(
        string='Duration',
        help='Duration of appointment (in minutes)',
        default=30.0,
    )
    physician_id = fields.Many2one(
        string='Physician',
        comodel_name='medical.physician',
        select=True,
        required=True,
        help='Scheduled Physician',
    )
    alias = fields.Char(
        string='Alias',
        help='Alias for appointment',
    )
    appointment_type = fields.Selection([
        ('ambulatory', 'Ambulatory'),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
    ],
        string='Type',
        help='Type of appointment',
        required=True,
        default='outpatient',
    )
    institution_id = fields.Many2one(
        string='Medical Center',
        help='Medical center that appointment is located at',
        comodel_name='res.partner',
        domain="[('type', '=', 'medical.center')]",
    )
    consultation_ids = fields.Many2one(
        string='Consultation Services',
        help='Services that appointment is being scheduled for',
        comodel_name='medical.physician.service',
        domain="[('physician_id', '=', physician_id)]",
    )
    urgency = fields.Selection([
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
    ],
        string='Urgency Level',
        help='Urgency level of this appointment',
        default='a',
    )
    specialty_id = fields.Many2one(
        string='Specialty',
        help='Medical Specialty / Sector',
        comodel_name='medical.specialty',
    )
    stage_id = fields.Many2one(
        string='Stage',
        help='Current appointment stage',
        comodel_name='medical.appointment.stage',
        track_visibility='onchange',
        default=lambda s: s._default_stage_id(),
    )

    _group_by_full = {
        'stage_id': lambda s: s._group_stage_ids(),
    }

    @api.multi
    @api.depends('appointment_date', 'duration')
    def _compute_appointment_end_date(self):
        for rec_id in self:
            start_date = fields.Datetime.from_string(rec_id.appointment_date)
            rec_id.appointment_end_date = fields.Datetime.to_string(
                start_date + timedelta(minutes=rec_id.duration)
            )

    @api.model
    def _default_stage_id(self):
        ''' Gives default stage_id '''
        stage_id = self.env['medical.appointment.stage'].search([
            ('is_default', '=', True)
        ],
            order='sequence',
            limit=1,
        )
        return stage_id

    @api.multi
    def _group_stage_ids(self, read_group_order=None,
                         access_rights_uid=None):

        access_rights_uid = access_rights_uid or self.env.user
        stage_obj = self.env['medical.appointment.stage']
        order = stage_obj._order

        # lame hack to allow reverting search, should just work in trivial case
        # @TODO: fix this
        if read_group_order == 'stage_id desc':
            order = "%s desc" % order
        search_domain = []

        # perform search
        stage_ids = stage_obj.sudo(access_rights_uid).search(
            search_domain, order=order
        )
        result = stage_ids.name_get()

        # restore order of the search
        stage_id_ints = [s.id for s in stage_ids]
        result.sort(lambda x, y: cmp(stage_id_ints.index(x[0]),
                                     stage_id_ints.index(y[0])))

        fold = {}
        for stage_id in stage_ids:
            fold[stage_id.id] = stage_id.fold or False

        return result, fold

    @api.multi
    @api.constrains('physician_id', 'appointment_date', 'duration',
                    'force_schedule')
    def _check_not_double_booking(self):
        for rec_id in self:
            if rec_id.force_schedule:
                continue
            domain = [
                ('physician_id', '=', rec_id.physician_id.id),
                ('id', '!=', rec_id.id),
                ('appointment_date', '<=', rec_id.appointment_end_date),
                ('appointment_end_date', '>=', rec_id.appointment_date),
            ]
            if len(self.sudo().search(domain)):
                raise exceptions.ValidationError(_(
                    'Physician is in an appointment during the selected '
                    'time. Select `Force Schedule` if you would like to '
                    'schedule anyways.'
                ))

    @api.multi
    def write(self, vals, ):
        result = super(MedicalAppointment, self).write(vals)
        if 'stage_id' in vals:
            self._change_stage(vals)
        return result

    @api.multi
    def _change_stage(self, vals):
        ''' @TODO: replace in SMD-118 '''

        stage_id = self.env['medical.appointment.stage'].browse(
            vals['stage_id']
        )
        stage_name = stage_id.name_get()[0][1]

        for rec_id in self:

            date_start = vals.get(
                'appointment_date', rec_id.appointment_date
            )
            localized_datetime = fields.Datetime.context_timestamp(
                rec_id, fields.Datetime.from_string(date_start),
            )
            context = self._context.copy()
            context.update({
                'appointment_date': fields.Datetime.to_string(
                    localized_datetime
                ),
                'appointment_time': fields.Datetime.to_string(
                    localized_datetime
                )
            })
            email_template_name = None

            if stage_name == 'Pending Review':
                # Should create template and change name here
                email_template_name = 'email_template_appointment_confirmation'

            elif stage_name == 'Confirm':
                email_template_name = 'email_template_appointment_confirmation'

            elif stage_name == 'Cancelled':
                # Should create template and change name here
                email_template_name = 'email_template_appointment_confirmation'

            if email_template_name:
                email_template_proxy = self.env['mail.template']
                model_obj = self.env['ir.model.data']
                _, template_id_int = model_obj.get_object_reference(
                    'medical_appointment', email_template_name
                )
                template_id = email_template_proxy.browse(template_id_int)
                template_id.send_mail(rec_id.id, True)

    @api.model
    def _get_appointments(self, physician_ids, institution_ids,
                          date_start, date_end):
        """
        Get appointments between given dates, excluding pending review
        and cancelled ones
        """

        model_obj = self.env['ir.model.data']
        _, pending_review_id_int = model_obj.get_object_reference(
            'medical_appointment', 'stage_appointment_in_review'
        )
        _, cancelled_id_int = model_obj.get_object_reference(
            'medical_appointment', 'stage_appointment_cancelled'
        )

        domain = [
            ('physician_id', 'in', [p.id for p in physician_ids]),
            ('appointment_date', '>=', date_start),
            ('appointment_date', '<=', date_end),
            ('stage_id', 'not in', [pending_review_id_int, cancelled_id_int])
        ]

        if len(institution_ids):
            domain.append(
                ('institution_id', 'in', [i.id for i in institution_ids])
            )

        return self.search(domain)

    @api.model
    def _set_clashes_state_to_review(self, physician_ids, institution_ids,
                                     date_start, date_end):
        model_obj = self.env['ir.model.data']
        _, review_stage_id_int = model_obj.get_object_reference(
            'medical_appointment', 'stage_appointment_in_review',
        )
        if not review_stage_id_int:
            raise exceptions.ValidationError(
                _('No default stage defined for review')
            )

        current_appointment_ids = self._get_appointments(
            physician_ids, institution_ids, date_start, date_end,
        )
        if len(current_appointment_ids):
            current_appointment_ids.write({
                'stage_id': review_stage_id_int,
            })
