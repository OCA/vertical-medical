# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class MedicalBaseKanbanTest(models.Model):
    """ It provides a model for testing. Need to figure out a way to only
    load while testing, instead of all the time
    """
    _name = 'medical.base.kanban.test'
    _inherit = 'medical.base.kanban'
