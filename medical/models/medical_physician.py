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

from openerp import fields, models
from openerp.addons.medical.medical_constants import days, hours, minutes

import logging

_logger = logging.getLogger(__name__)


class MedicalPhysicianServices(models.Model):
    '''
    Services provided by the Physician on a specific medical center.

    A physician could have "surgeries" on one center but only
    "general consultation" in another center,
    or the same service with different prices for each medical center.
    That's the reason to link this to res.partner instead of medical_physician.
    '''
    _name = 'medical.physician.services'
    _inherits = {'product.product': 'product_id', }
    product_id = fields.Many2one('product.product', 'Related Product',
                                  required=True, ondelete='restrict',
                                  help='Product related information for'
                                       'Appointment Type')
    physician_id = fields.Many2one('medical.physician', 'Physician',
                                    required=True, select=1,
                                    ondelete='cascade')
    service_duration = fields.Selection(minutes, string='Duration')


class MedicalPhysicianScheduleTemplate(models.Model):
    '''
    Available schedule for the Physiscian.

    ie: A physiscian will be able to say, in this schedule on this days.

    The objective is to show the availbles spaces for every physiscian
    '''
    _name = 'medical.physician.schedule.template'
    physician_id = fields.Many2one('medical.physician', 'Physician',
                                    required=True, select=1,
                                    ondelete='cascade')
    day = fields.Selection(days, string='Day', sort=False)
    start_hour = fields.Selection(hours, string='Hour')
    start_minute = fields.Selection(minutes, string='Minute')
    end_hour = fields.Selection(hours, string='Hour')
    end_minute = fields.Selection(minutes, string='Minute')
    duration = fields.Selection(minutes, string='Duration')


class MedicalPhysician(models.Model):
    _name = 'medical.physician'
    _inherits = {'res.partner': 'partner_id', }
    id = fields.Integer('ID', readonly=True)
    partner_id = fields.Many2one(
        'res.partner', 'Related Partner', required=True, ondelete='cascade',
        help='Partner related data of the physician'
    )
    code = fields.Char(size=256, string='ID')
    specialty_id = fields.Many2one(
        'medical.specialty', string='Specialty', required=True,
        help='Specialty Code'
    )
    info = fields.Text(string='Extra info')
    active = fields.Boolean(
        'Active', default=True,
        help='If unchecked, it will allow you to hide the physician without '
             'removing it.'
    )
    schedule_template_ids = fields.One2many(
        'medical.physician.schedule.template', 'physician_id',
        'Related schedules'
    )

    _defaults = {'is_doctor': True, 'supplier': True, 'active': True, }

    def create(self, cr, uid, vals, context=None):
        groups_proxy = self.pool['res.groups']
        group_ids = groups_proxy.search(cr, uid,
                                        [('name', '=', 'Medical Doctor')],
                                        context=context)
        vals['groups_id'] = [(6, 0, group_ids)]
        return super(MedicalPhysician, self).create(cr, uid, vals,
                                                    context=context)
