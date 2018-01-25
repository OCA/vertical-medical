# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, fields, models


class MedicalPharmacy(models.Model):
    _inherit = 'medical.pharmacy'

    is_verified = fields.Boolean(
        string='Verified',
        help='Check this to indicate that this pharmacy is a verified entity',
    )
    verified_by_id = fields.Many2one(
        string='Verified By',
        comodel_name='res.users',
        store=True,
        compute='_compute_verified_by_id_and_date',
    )
    verified_date = fields.Datetime(
        string='Verified Date',
        store=True,
        compute='_compute_verified_by_id_and_date',
    )

    @api.multi
    @api.depends('is_verified')
    def _compute_verified_by_id_and_date(self):
        for record in self:
            if record.is_verified and not record.verified_date:
                record.verified_by_id = self.env.user.id
                record.verified_date = fields.Datetime.now()
