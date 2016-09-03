# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class MedicalPrescriptionOrder(models.Model):
    """ Add Kanban functionality to MedicalPrescriptionOrder """
    _inherit = ['medical.prescription.order', 'medical.base.kanban']
    _name = 'medical.prescription.order'
