# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class MedicalPrescriptionOrder(models.Model):
    _name = 'medical.prescription.order'
    _inherit = ['medical.prescription.order', 'mail.thread']
