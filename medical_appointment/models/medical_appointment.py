# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
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
##############################################################################

from openerp import fields, models, exceptions, api, _
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import timedelta, datetime


class MedicalAppointment(models.Model):
    _name = 'medical.appointment'
    _inherit = 'medical.history.abstract'
    _description = 'Medical Appointments'

    STATES = {
        'draft': [('readonly', False)]
    }

    user_id = fields.Many2one(
        string='Responsible',
        help='User that created appointment',
        comodel_name='res.users',
        readonly=True,
        states=STATES,
        default=lambda self: self.env.user,
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
        help='Date and Time of Scheduled Appointment'
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
    comments = fields.Text(
        string='Comments',
        help='Any additional notes',
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
    insitution_id = fields.Many2one(
        string='Medical Center',
        help='Medical center that appointment is located at',
        domain="[('is_institution', '=', True)]",
    )
    consultation_ids = fields.Many2one(
        string='Consultation Services',
        help='Services that appointment is being scheduled for',
        comodel_name='medical.physician.services',
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

    def _default_stage_id(self, ):
        ''' Gives default stage_id '''
        stage_id = self.env['medical.appointment.stage'].search([
            ('is_default', '=', True)
        ],
            order='sequence',
            limit=1,
        )
        return stage_id

    @api.multi
    def _group_stage_ids(self, domain, read_group_order=None,
                         access_rights_uid=None, ):

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
        result = stage_obj.sudo(access_rights_uid).name_get(stage_ids)

        # restore order of the search
        stage_id_ints = [s.id for s in stage_ids]
        result.sort(lambda x, y: cmp(stage_id_ints.index(x[0]),
                                     stage_id_ints.index(y[0])))

        fold = {}
        for stage_id in stage_ids:
            fold[stage_id.id] = stage_id.fold or False

        return result, fold

    @api.multi
    @api.constrains('physician_id', 'appointment_date', 'duration')
    def _check_not_double_booking(self, ):
        for rec_id in self:
            date_start = fields.Datetime.from_string(rec_id.appointment_date)
            duration_delta = timedelta(minutes=rec_id.duration)
            date_end = date_start + duration_delta
            domain = [
                ('appointment_date', '>=', date_start),
                ('appointment_date', '<=', date_end),
                ('physician_id', '=', rec_id.physician_id.id),
                ('id', '!=', rec_id.id),
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
    def _change_stage(self, vals, ):
        ''' @TODO: replace in SMD-118 '''

        stage_proxy = self.env['medical.appointment.stage']
        stage_name = stage_proxy.name_get(vals['stage_id'])[0][1]

        for rec_id in self:

            history_entry_ids = self.history_entry_new('STAGE', vals)
            date_start = vals.get(
                'appointment_date', rec_id.appointment_date
            )
            localized_datetime = fields.Datetime.context_timestamp(
                datetime.strptime(date_start, DEFAULT_SERVER_DATETIME_FORMAT),
            )
            context = self._context.copy()
            context.update({
                'appointment_date': localized_datetime.strftime(
                    self.env.user.lang.date_format
                ),
                'appointment_time': localized_datetime.strftime(
                    self.env.user.lang.time_format
                )
            })
            email_template_name = None

            if stage_name == 'Pending Review':
                # Should create template and change name here
                email_template_name = 'email_template_appointment_confirmation'

            elif stage_name == 'Confirm':
                email_template_name = 'email_template_appointment_confirmation'

            elif stage_name == 'Canceled':
                # Should create template and change name here
                email_template_name = 'email_template_appointment_confirmation'

            if email_template_name:
                email_template_proxy = self.env['email.template']
                model_obj = self.env['ir.model.data']
                _, template_id = model_obj.get_object_reference(
                    'medical', email_template_name
                )
                map(
                    lambda t: email_template_proxy.send_mail(
                        template_id, t, True, context=context
                    ), self
                )

        history_entry_ids.state_complete()

    @api.model
    def _get_appointments(self, physician_ids, institution_ids,
                          date_start, date_end, ):
        """
        Get appointments between given dates, excluding pending review
        and cancelled ones
        """

        model_obj = self.env['ir.model.data']
        _, pending_review_id = model_obj.get_object_reference(
            'medical', 'stage_appointment_in_review'
        )
        _, cancelled_id = model_obj.get_object_reference(
            'medical', 'stage_appointment_cancelled'
        )

        domain = [
            ('physician_id', 'in', [p.id for p in physician_ids]),
            ('date_end', '>', date_start),
            ('appointment_date', '<', date_end),
            ('stage_id', 'not in', [pending_review_id.id,
                                    cancelled_id.id])
        ]

        if institution_ids:
            domain += [
                ('institution_id', 'in', [i.id for i in institution_ids])
            ]

        return self.search(domain)

    def _set_clashes_state_to_review(self, physician_ids, institution_ids,
                                     date_start, date_end, ):
        model_obj = self.env['ir.model.data']
        _, review_stage_id = model_obj.get_object_reference(
            'medical', 'stage_appointment_in_review',
        )
        if not review_stage_id:
            raise exceptions.ValidationError(
                _('No default stage defined for review')
            )

        current_appointment_ids = self._get_appointments(
            physician_ids, institution_ids, date_start, date_end,
        )
        if current_appointment_ids:
            current_appointment_ids.stage_id = review_stage_id
