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

from openerp import fields, models
import logging


class MedicalAppointmentStage(models.Model):
    """ Model for case stages. This models the main stages of an appointment
        management flow. Main CRM objects (leads, opportunities, project
        issues, ...) will now use only stages, instead of state and stages.
        Stages are for example used to display the kanban view of records.
    """
    _name = "medical.appointment.stage"
    _description = "Stage of Appointment"
    _rec_name = 'name'
    _order = "sequence"

    name = fields.Char(
        'Stage Name',
        size=64,
        required=True,
        translate=True,
    )
    sequence = fields.Integer(
        'Sequence',
        help='Used to order stages. Lower is better.',
    )
    requirements = fields.Text(
        'Requirements',
    )
    fold = fields.Boolean(
        'Folded in KanBan view',
        help='This stage is folded in the KanBan view when there are no '
        'records in that stage to display.',
    )
    is_default = fields.Boolean(
        'Default?',
        help='If checked, this stage will be selected when creating new '
        'appointments.',
    )

    _defaults = {'sequence': 1, 'fold': False, }
