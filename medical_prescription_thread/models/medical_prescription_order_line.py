# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class MedicalPrescriptionOrderLine(models.Model):
    _name = 'medical.prescription.order.line'
    _inherit = ['medical.prescription.order.line', 'mail.thread']
