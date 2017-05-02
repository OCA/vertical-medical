# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models


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
