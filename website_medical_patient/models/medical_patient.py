# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api


class MedicalPatient(models.Model):

    _name = 'medical.patient'
    _inherit = ['medical.patient', 'website.published.mixin', 'mail.thread']

    @api.multi
    def action_invalidate(self):
        return self.write({'active': False})

    @api.multi
    def _website_url(self, field_name, arg):
        res = super(MedicalPatient, self)._website_url(field_name, arg)
        for rec_id in self:
            res[rec_id.id] = "/medical/patients/%s" % rec_id.id
        return res
