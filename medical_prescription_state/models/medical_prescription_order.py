# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import models


class MedicalPrescriptionOrder(models.Model):
    """ Add Kanban functionality to MedicalPrescriptionOrder """
    _inherit = ['medical.prescription.order', 'base.kanban.abstract']
    _name = 'medical.prescription.order'
