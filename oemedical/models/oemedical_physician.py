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

from openerp.osv import fields, orm
from openerp.tools.translate import _

from openerp.addons.oemedical.oemedical_constants import days, hours, minutes


class oemedical_physician_schedule_template(orm.Model):
    _name = 'oemedical.physician.schedule.template'
    _columns = {
        'physician_id': fields.many2one('oemedical.physician', 'Physician', required=True, select=1, ondelete='cascade'),
        'day': fields.selection(days,
                                string='Day', sort=False),
        'start_hour': fields.selection(hours,
            string='Hour'),
        'start_minute': fields.selection(minutes,
            string='Minute'),
        'end_hour': fields.selection(hours,
            string='Hour'),
        'end_minute': fields.selection(minutes,
            string='Minute'),
        'duration': fields.selection(minutes,
            string='Duration'),
    }


class OeMedicalPhysician(orm.Model):
    _name = 'oemedical.physician'
    _inherits = {
        'res.users': 'user_id',
    }
    _columns = {
        'id': fields.integer('ID', readonly=True),
        'user_id': fields.many2one(
            'res.users', 'Related User', required=True,
            ondelete='cascade', help='User-related data of the physician'),
        'code': fields.char(size=256, string='ID'),
        'specialty': fields.many2one('oemedical.specialty', string='Specialty', required=True, help='Specialty Code'),
        'info': fields.text(string='Extra info'),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the physician without removing it."),
        'schedule_template_ids': fields.one2many('oemedical.physician.schedule.template', 'physician_id', 'Related schedules'),
    }

    def create(self, cr, uid, vals, context=None):
        vals['is_doctor'] = True
        vals['supplier'] = True
        return super(OeMedicalPhysician, self).create(cr, uid, vals, context=context)

    def action_update_schedule(self, cr, uid, ids, context=None):

        schedule_template_proxy = self.pool.get('oemedical.physician.schedule.template')

        this = self.browse(cr, uid, ids)[0]
        defined_templates = len(this.schedule_template_ids)

        #check for overlapping ranges
        for i in range(defined_templates):
            day_1 = this.schedule_template_ids[i].day
            start_time_1 = this.schedule_template_ids[i].start_hour * 60 + this.schedule_template_ids[i].start_minute
            end_time_1 = this.schedule_template_ids[i].end_hour * 60 + this.schedule_template_ids[i].end_minute

            for j in range(i + 1, defined_templates):
                day_2 = this.schedule_template_ids[j].day
                start_time_2 = this.schedule_template_ids[j].start_hour * 60 + this.schedule_template_ids[j].start_minute
                end_time_2 = this.schedule_template_ids[j].end_hour * 60 + this.schedule_template_ids[j].end_minute
                if day_1 == day_2 and \
                    start_time_1 < end_time_2 and \
                    end_time_1 > start_time_2:
                    # overlaped ranges
                    raise orm.except_orm(_('Error!'), _('Overlapped ranges for day "%s" ') % (days[day_1][1]))
        #create

        return True

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
