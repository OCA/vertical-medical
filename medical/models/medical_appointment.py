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

import time
from datetime import datetime, timedelta

from openerp.osv import fields, orm
from openerp.tools.translate import _
from openerp import SUPERUSER_ID
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT

import logging

_logger = logging.getLogger(__name__)


class MedicalAppointmentStage(orm.Model):
    """ Model for case stages. This models the main stages of an appointment
        management flow. Main CRM objects (leads, opportunities, project
        issues, ...) will now use only stages, instead of state and stages.
        Stages are for example used to display the kanban view of records.
    """
    _name = "medical.appointment.stage"
    _description = "Stage of Appointment"
    _rec_name = 'name'
    _order = "sequence"

    _columns = {
        'name': fields.char('Stage Name', size=64, required=True,
                            translate=True),
        'sequence': fields.integer('Sequence',
                                   help="Used to order stages. Lower "
                                        "is better."),
        'requirements': fields.text('Requirements'),
        'fold': fields.boolean('Folded in Kanban View',
                               help='This stage is folded in the kanban '
                                    'view when there are no records in that '
                                    'stage to display.'),


        'is_default': fields.boolean('Default?',
                                     help="If checked, this stage will be "
                                          "selected when creating new "
                                          "appointments."),
    }

    _defaults = {'sequence': 1, 'fold': False, }


class MedicalAppointment(orm.Model):
    _name = 'medical.appointment'

    def _get_default_stage_id(self, cr, uid, context=None):
        """ Gives default stage_id """
        stage_ids = self.pool['medical.appointment.stage'].search(
            cr, uid, [('is_default', '=', True)], order='sequence', limit=1,
            context=context)
        if stage_ids:
            return stage_ids[0]
        return False

    def _read_group_stage_ids(self, cr, uid, ids, domain,
                              read_group_order=None, access_rights_uid=None,
                              context=None):
        access_rights_uid = access_rights_uid or uid
        stage_obj = self.pool.get('medical.appointment.stage')
        order = stage_obj._order
        # lame hack to allow reverting search, should just work in trivial case
        if read_group_order == 'stage_id desc':
            order = "%s desc" % order
        search_domain = []
        # perform search
        stage_ids = stage_obj._search(cr, uid, search_domain, order=order,
                                      access_rights_uid=access_rights_uid,
                                      context=context)
        result = stage_obj.name_get(cr, access_rights_uid, stage_ids,
                                    context=context)
        # restore order of the search
        result.sort(lambda x, y: cmp(stage_ids.index(x[0]),
                                     stage_ids.index(y[0])))

        fold = {}
        for stage in stage_obj.browse(cr, access_rights_uid, stage_ids,
                                      context=context):
            fold[stage.id] = stage.fold or False
        return result, fold

    _columns = {
        'user_id': fields.many2one('res.users', 'Responsible', readonly=True,
                                   states={'draft': [('readonly', False)]}),
        'patient_id': fields.many2one('medical.patient', string='Patient',
                                      required=True, select=True,
                                      help='Patient Name'),
        'name': fields.char(size=256, string='Appointment ID', readonly=True),
        'appointment_date': fields.datetime(string='Date and Time'),
        'date_end': fields.datetime(string='do not display'),
        'duration': fields.float('Duration'),
        'physician_id': fields.many2one('medical.physician',
                                        string='Physician', select=True,
                                        required=True,
                                        help='Physician\'s Name'),
        'alias': fields.char(size=256, string='Alias', ),
        'comments': fields.text(string='Comments'),
        'appointment_type': fields.selection(
            [('ambulatory', 'Ambulatory'), ('outpatient', 'Outpatient'),
             ('inpatient', 'Inpatient'), ], string='Type'),
        'institution_id': fields.many2one('res.partner',
                                          string='Health Center',
                                          help='Medical Center',
                                          domain="[('is_institution', '=',"
                                                 "True)]"),
        'consultations': fields.many2one('medical.physician.services',
                                         string='Consultation Services',
                                         help='Consultation Services',
                                         domain="[('physician_id', '=',"
                                                "physician_id), ]"),
        'urgency': fields.selection(
            [('a', 'Normal'), ('b', 'Urgent'), ('c', 'Medical Emergency'), ],
            string='Urgency Level'),
        'specialty': fields.many2one('medical.specialty', string='Specialty',
                                     help='Medical Specialty / Sector'),
        'stage_id': fields.many2one('medical.appointment.stage', 'Stage',
                                    track_visibility='onchange'),
        'history_ids': fields.one2many('medical.appointment.history',
                                       'appointment_id_history',
                                       'History lines'),

    }

    _defaults = {
        'name': '/',
        'duration': 30.00,
        'urgency': 'a',
        'stage_id': lambda s, cr, uid, c: s._get_default_stage_id(cr, uid, c),
        'user_id': lambda s, cr, u, c: u,
        'appointment_type': 'outpatient',
    }

    _group_by_full = {'stage_id': _read_group_stage_ids}

    def _get_appointments(self, cr, uid, physician_ids, institution_ids,
                          date_start, date_end, context=None):
        """ Get appointments between given dates, excluding pending review
        and cancelled ones """

        pending_review_id = \
            self.pool.get('ir.model.data').get_object_reference(
                cr, uid, 'medical', 'stage_appointment_in_review')[1]
        cancelled_id = \
            self.pool.get('ir.model.data').get_object_reference(
                cr, uid, 'medical', 'stage_appointment_canceled')[1]
        domain = [('physician_id', 'in', physician_ids),
                  ('date_end', '>', date_start),
                  ('appointment_date', '<', date_end),
                  ('stage_id', 'not in', [pending_review_id, cancelled_id])]
        if institution_ids:
            domain += [('institution_id', 'in', institution_ids)]

        return self.search(cr, uid, domain, context=context)

    def _get_empty_appointments(self, cr, uid, physician_ids, institution_ids,
                                date_start, date_end, context=None):
        """ Get  empty appointments between given dates """

        patient_proxy = self.pool['medical.patient']
        default_patient = patient_proxy._get_default_patient_id(cr, uid,
                                                                context=None)

        domain = [('physician_id', 'in', physician_ids),
                  ('patient_id', '=', default_patient),
                  ('date_end', '>', date_start),
                  ('appointment_date', '<', date_end)]
        if institution_ids:
            domain += [('institution_id', 'in', institution_ids)]

        _logger.warning("get empty appointments domain:  '%s'" % (str(domain)))

        return self.search(cr, uid, domain, context=context)

    def _remove_empty_clashes(self, cr, uid, excluded_ids, physician_ids,
                              institution_ids, date_start, date_end,
                              context=None):
        """ Remove empty appointments that clash with given one """

        # remove from list those ids in excluded_ids
        empty_appointments = set(
            self._get_empty_appointments(cr, uid, physician_ids,
                                         institution_ids, date_start, date_end,
                                         context=context)).difference(
            excluded_ids)

        self.unlink(cr, uid, empty_appointments, context)

    def _set_clashes_state_to_review(self, cr, uid, physician_ids,
                                     institution_ids, date_start, date_end,
                                     context=None):
        dummy, review_stage_id = \
            self.pool[
                'ir.model.data'].get_object_reference(
                    cr, uid, 'medical', 'stage_appointment_in_review')
        if not review_stage_id:
            raise orm.except_orm(_('Error!'),
                                 _('No default stage defined for review'))

        current_appointments = self._get_appointments(cr, uid, physician_ids,
                                                      institution_ids,
                                                      date_start, date_end,
                                                      context=context)
        if current_appointments:
            self.write(cr, uid, current_appointments,
                       {'stage_id': review_stage_id})

    def create(self, cr, uid, vals, context=None):
        date_start = vals['appointment_date']
        duration = int(vals['duration'])
        date_end = (
            datetime.strptime(date_start, "%Y-%m-%d %H:%M:%S") +
            timedelta(minutes=duration)).strftime("%Y-%m-%d %H:%M")
        vals['date_end'] = date_end

        self._remove_empty_clashes(cr, uid, [], [vals['physician_id']], [],
                                   date_start, date_end, context=context)
        current_appointments = self._get_appointments(cr, uid,
                                                      [vals['physician_id']],
                                                      [], date_start, date_end,
                                                      context=context)
        if current_appointments:
            raise orm.except_orm(_('Error!'),
                                 _('Appointment clashes with other'))

        if vals.get('name', '/') == '/':
            vals['name'] = self.pool['ir.sequence'].get(cr, uid,
                                                        'medical.appointment')

        val_history = {}

        val_history['name'] = uid
        val_history['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        val_history['action'] = "----  Created  ----"

        vals['history_ids'] = val_history
        return super(MedicalAppointment, self).create(cr, uid, vals,
                                                      context=context)

    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        else:
            context = context.copy()

        original_values = self.read(cr, uid, ids,
                                    ['physician_id', 'institution_id',
                                     'appointment_date', 'date_end',
                                     'duration'],
                                    context=context)[0]
        date_start = vals.get('appointment_date',
                              original_values['appointment_date'])
        if 'appointment_date' in vals or 'duration' in vals:

            physician_id = vals.get('physician_id',
                                    original_values['physician_id'][0])
            duration = vals.get('duration', original_values['duration'])

            date_end = (
                datetime.strptime(date_start, "%Y-%m-%d %H:%M:%S") +
                timedelta(minutes=duration)).strftime("%Y-%m-%d %H:%M")
            vals['date_end'] = date_end
            self._remove_empty_clashes(cr, uid, ids, [physician_id], [],
                                       date_start, date_end, context=context)
            current_appointments = self._get_appointments(
                cr, uid, [physician_id], [], date_start, date_end,
                context=context).remove(ids[0])
            if current_appointments:
                raise orm.except_orm(_('Error!'),
                                     _('Appointment clashes with other'))

        result = super(MedicalAppointment, self).write(cr, uid, ids, vals,
                                                       context=context)

        # stage change: update date_last_stage_update
        if 'stage_id' in vals:
            ait_obj = self.pool['medical.appointment.history']
            stage_proxy = self.pool['medical.appointment.stage']
            stage_name = stage_proxy.name_get(cr, uid, vals['stage_id'],
                                              context=context)[0][1]
            # ### update history and any other for stage_id.onchange....
            val_history = {
                'action': "----  Changed to {0}  ----".format(stage_name),
                'appointment_id_history': ids[0],
                'name': uid,
                'date': time.strftime('%Y-%m-%d %H:%M:%S'),
            }
            ait_obj.create(cr, uid, val_history)

            user_record = self.pool['res.users'].browse(cr, SUPERUSER_ID, uid)
            lang_id = self.pool['res.lang'].search(cr, SUPERUSER_ID, [
                ('code', '=', user_record.lang)])
            lang_record = self.pool['res.lang'].browse(cr, SUPERUSER_ID,
                                                       lang_id)[0]

            localized_datetime = fields.datetime.context_timestamp(
                cr, uid,
                datetime.strptime(date_start, DEFAULT_SERVER_DATETIME_FORMAT),
                context=context)
            context['appointment_date'] = localized_datetime.strftime(
                lang_record.date_format)
            context['appointment_time'] = localized_datetime.strftime(
                lang_record.time_format)

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
                email_template_proxy = self.pool['email.template']
                template_id = \
                    self.pool.get(
                        'ir.model.data').get_object_reference(
                            cr, uid, 'medical', email_template_name)[1]
                map(lambda t: email_template_proxy.send_mail(
                    cr, uid, template_id, t, True, context=context),
                    ids)

        return result


class MedicalAppointment_history(orm.Model):
    _name = 'medical.appointment.history'

    _columns = {
        'appointment_id_history': fields.many2one('medical.appointment',
                                                  'History',
                                                  ondelete='cascade'),
        'date': fields.datetime(string='Date and Time'),
        'name': fields.many2one('res.users', string='User', help=''),
        'action': fields.text('Action'), }

    _defaults = {}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
