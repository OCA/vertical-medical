# -*- coding: utf-8 -*-
# © 2004 Tech-Receptives
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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
    That's the reason to link this to res.partner instead of
    medical_physician.
    '''
    _name = 'medical.physician.services'
    _inherits = {'product.product': 'product_id', }
    product_id = fields.Many2one(
        'product.product', 'Related Product', required=True,
        ondelete='restrict',
        help='Product related information for Appointment Type'
    )
    physician_id = fields.Many2one(
        'medical.physician', 'Physician', required=True, select=1,
        ondelete='cascade'
    )
    service_duration = fields.Selection(minutes, string='Duration')


class MedicalPhysicianScheduleTemplate(models.Model):
    '''
    Available schedule for the Physiscian.

    ie: A physiscian will be able to say, in this schedule on this days.

    The objective is to show the availbles spaces for every physiscian
    '''
    _name = 'medical.physician.schedule.template'
    physician_id = fields.Many2one(
        'medical.physician', 'Physician', required=True, select=1,
        ondelete='cascade'
    )
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
