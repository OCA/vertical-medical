# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Ken Mak <kmak@laslabs.com>
#    Copyright: 2014-2016 LasLabs, Inc. [https://laslabs.com]
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

from openerp import fields, models
from openerp.addons.medical.medical_constants import minutes


class MedicalPhysicianService(models.Model):
    '''
    Services provided by the Physician on a specific medical center.

    A physician could have "surgeries" on one center but only
    "general consultation" in another center,
    or the same service with different prices for each medical center.
    That's the reason to link this to res.partner instead of
    medical_physician.
    '''
    _name = 'medical.physician.service'
    _inherits = {'product.product': 'product_id', }
    _description = 'Medical Physicians Services'
    product_id = fields.Many2one(
        string='Related Product',
        help='Product related information for Appointment Type',
        comodel_name='product.product',
        required=True,
        ondelete='restrict',
    )
    physician_id = fields.Many2one(
        string='Physician',
        help='The physician for the appointment',
        comodel_name='medical.physician',
        required=True,
        select=True,
        ondelete='cascade',
    )
    service_duration = fields.Selection(
        minutes, string='Duration',
        help='Duration of the appointment in minutes',
    )
