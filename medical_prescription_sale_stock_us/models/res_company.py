# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api, _
from openerp.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    medical_prescription_refill_threshold = fields.Float(
        string='Refill Threshold',
        default=0.80,
        help='Amount of fill that must be used before allowing a refill. '
             'This should be a decimal, such as .75 for 75%.',
    )

    @api.multi
    @api.constrains('medical_prescription_refill_threshold')
    def _check_medical_prescription_refill_threshold(self):
        for rec_id in self:
            if rec_id.medical_prescription_refill_threshold > 1:
                ValidationError(_(
                    'Refill threshold should not be greater than 1, which '
                    'indicates 100%.',
                ))
            if rec_id.medical_prescription_refill_threshold < 0:
                ValidationError(_(
                    'Refill threshold should not be less than 0, which '
                    'indicates no threshold.',
                ))
