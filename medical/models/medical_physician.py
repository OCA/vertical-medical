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
from openerp.tools.translate import _

from openerp.addons.medical.medical_constants import days, hours, minutes

from datetime import datetime, date, timedelta

import logging

_logger = logging.getLogger(__name__)


class MedicalPhysicianServices(orm.Model):
    '''
    Services provided by the Physician on a specific medical center.

    A physician could have "surgeries" on one center but only
    "general consultation" in another center,
    or the same service with different prices for each medical center.
    That's the reason to link this to res.partner instead of medical_physician.
    '''
    _name = 'medical.physician.services'
    _inherits = {'product.product': 'product_id', }
    _columns = {
        'product_id': fields.many2one('product.product', 'Related Product',
                                      required=True, ondelete='restrict',
                                      help='Product related information for'
                                           'Appointment Type'),
        'physician_id': fields.many2one('medical.physician', 'Physician',
                                        required=True, select=1,
                                        ondelete='cascade'),
        'service_duration': fields.selection(minutes, string='Duration'),
    }


class MedicalPhysicianScheduleTemplate(orm.Model):
    '''
    Available schedule for the Physiscian.

    ie: A physiscian will be able to say, in this schedule on this days.

    The objective is to show the availbles spaces for every physiscian
    '''
    _name = 'medical.physician.schedule.template'
    _columns = {
        'physician_id': fields.many2one('medical.physician', 'Physician',
                                        required=True, select=1,
                                        ondelete='cascade'),
        'day': fields.selection(days, string='Day', sort=False),
        'start_hour': fields.selection(hours, string='Hour'),
        'start_minute': fields.selection(minutes, string='Minute'),
        'end_hour': fields.selection(hours, string='Hour'),
        'end_minute': fields.selection(minutes, string='Minute'),
        'duration': fields.selection(minutes, string='Duration'),
    }


class MedicalPhysician(orm.Model):
    _name = 'medical.physician'
    _inherits = {'res.partner': 'partner_id', }
    _columns = {
        'id': fields.integer('ID', readonly=True),
        'partner_id': fields.many2one('res.partner', 'Related Partner',
                                   required=True, ondelete='cascade',
                                   help='Partner related data '
                                        'of the physician'),
        'code': fields.char(size=256, string='ID'),
        'specialty': fields.many2one('medical.specialty',
                                     string='Specialty',
                                     required=True,
                                     help='Specialty Code'),
        'info': fields.text(string='Extra info'),
        'active': fields.boolean('Active',
                                 help='If unchecked, it will allow you'
                                      ' to hide the physician without '
                                      'removing it.'),
        'schedule_template_ids': fields.one2many(
            'medical.physician.schedule.template', 'physician_id',
            'Related schedules')
    }

    _defaults = {'is_doctor': True, 'supplier': True, 'active': True, }

    def create(self, cr, uid, vals, context=None):
        groups_proxy = self.pool['res.groups']
        group_ids = groups_proxy.search(cr, uid,
                                        [('name', '=', 'Medical Doctor')],
                                        context=context)
        vals['groups_id'] = [(6, 0, group_ids)]
        return super(MedicalPhysician, self).create(cr, uid, vals,
                                                    context=context)

    def action_update_schedule(self, cr, uid, ids, context=None):

        patient_proxy = self.pool['medical.patient']
        default_patient = patient_proxy._get_default_patient_id(cr, uid,
                                                                context=None)

        appointment_proxy = self.pool['medical.appointment']

        ICP = self.pool['ir.config_parameter']
        MaxDays = int(ICP.get_param(cr, uid, 'max.appointment.days'))
        if not MaxDays:
            raise orm.except_orm(_('Error!'),
                                 _('max.appointment.days: Maximun days for '
                                   'future agenda not defined'))

        this = self.browse(cr, uid, ids)[0]
        defined_templates = len(this.schedule_template_ids)

        templates_per_day = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

        # check for overlapping ranges
        for i in range(defined_templates):
            day_1 = this.schedule_template_ids[i].day
            templates_per_day[day_1] += [this.schedule_template_ids[i]]
            start_time_1 = this.schedule_template_ids[i].start_hour * 60 + \
                this.schedule_template_ids[i].start_minute
            end_time_1 = this.schedule_template_ids[i].end_hour * 60 + \
                this.schedule_template_ids[i].end_minute

            for j in range(i + 1, defined_templates):
                day_2 = this.schedule_template_ids[j].day
                start_time_2 = this.schedule_template_ids[j].start_hour * 60 +\
                    this.schedule_template_ids[j].start_minute
                end_time_2 = this.schedule_template_ids[j].end_hour * 60 + \
                    this.schedule_template_ids[j].end_minute
                if day_1 == day_2 and start_time_1 < end_time_2 and \
                   end_time_1 > start_time_2:
                    raise orm.except_orm(_('Error!'),
                                         _('Overlapped ranges for day "%s"'
                                           ) % (days[day_1][1]))

        current_day = date.today()
        current_day_str = current_day.strftime("%Y-%m-%d ")

        last_day = (date.today() + timedelta(MaxDays))
        last_day_str = last_day.strftime("%Y-%m-%d ")

        appointment_proxy._remove_empty_clashes(cr, uid, [], ids, [],
                                                current_day_str, last_day_str,
                                                context=context)
        appointment_proxy._set_clashes_state_to_review(cr, uid, ids, [],
                                                       current_day_str,
                                                       last_day_str,
                                                       context=context)

        appointment_vals = {'user_id': uid, 'patient_id': default_patient,
                            'appointment_type': 'outpatient', 'urgency': 'a', }

        # get timedelta between user timezone and UTC
        utc_time = datetime.now()
        user_time = fields.datetime.context_timestamp(
            cr, uid, utc_time, context=context).replace(tzinfo=None)
        user_timedelta = utc_time - user_time
        one_day = timedelta(1)
        # create appointments
        while current_day < last_day:
            current_day_str = current_day.strftime("%Y-%m-%d ")
            day_of_week = current_day.weekday()
            for slot in templates_per_day[day_of_week]:
                start_time = datetime.strptime(current_day_str +
                                               slot.start_hour + ':' +
                                               slot.start_minute,
                                               "%Y-%m-%d %H:%M") + \
                    user_timedelta
                end_time = datetime.strptime(current_day_str +
                                             slot.end_hour + ':' +
                                             slot.end_minute,
                                             "%Y-%m-%d %H:%M") +\
                    user_timedelta
                one_slot = timedelta(minutes=int(slot.duration))
                while start_time + one_slot <= end_time:
                    appointment_vals['name'] = self.pool[
                        'ir.sequence'].get(cr, uid, 'medical.appointment')
                    # appointment_vals['doctor_med_center'] = \
                    #    slot.institution_id.id
                    appointment_vals['physician_id'] = \
                        slot.physician_id.id
                    appointment_vals['institution_id'] = \
                        slot.physician_id.parent_id.id
                    appointment_vals['appointment_date'] = \
                        start_time.strftime("%Y-%m-%d %H:%M")
                    appointment_vals['duration'] = slot.duration
                    appointment_proxy.create(cr, uid, appointment_vals,
                                             context=context)
                    start_time += one_slot
            current_day += one_day

        return True
