# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api


class MedicalPrescriptionOrder(models.Model):
    _inherit = 'medical.prescription.order'

    receive_method = fields.Selection([
        ('online', 'E-Prescription'),
        ('phone', 'Phoned In'),
        ('fax', 'Fax'),
        ('mail', 'Physical Mail'),
        ('transfer', 'Transferred In'),
    ],
        default='fax',
        string='Receipt Method',
        help='How the Rx was received',
    )
    verify_method = fields.Selection([
        ('none', 'Not Verified'),
        ('doctor_phone', 'Called Doctor'),
    ],
        default='none',
        help='Method of Rx verification',
    )
    receive_date = fields.Datetime(
        default=fields.Datetime.now,
        string='Receipt Date',
        help='When the Rx was received',
    )
    verify_user_id = fields.Many2one(
        string='Verify User',
        comodel_name='res.users',
        store=True,
        compute='_compute_verified',
        help='User that verified the prescription',
    )
    verify_date = fields.Datetime(
        store=True,
        compute='_compute_verified',
        help='When the prescription was verified',
    )
    is_verified = fields.Boolean(
        string='Verified',
        store=True,
        compute="_compute_verified",
        help='If checked, this prescription has been confirmed as valid',
    )
    transfer_pharmacy_id = fields.Many2one(
        string='Transfer Pharmacy',
        comodel_name='medical.pharmacy',
    )
    transfer_direction = fields.Selection([
        ('none', 'None'),
        ('in', 'In'),
        ('out', 'Out'),
    ],
        default='none',
    )
    transfer_ref = fields.Char(
        string='Transfer Reference',
    )

    @api.multi
    @api.depends('verify_method')
    def _compute_verified(self):
        for rec_id in self:
            if rec_id.verify_method != 'none':
                if not rec_id.is_verified:
                    rec_id.is_verified = True
                    rec_id.verify_user_id = self.env.user.id
                    rec_id.verify_date = fields.Datetime.now()
