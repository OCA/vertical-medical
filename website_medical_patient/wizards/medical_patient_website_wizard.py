# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class MedicalPatientWebsiteWizard(models.TransientModel):
    _inherit = 'medical.patient'
    _name = 'medical.patient.website.wizard'
