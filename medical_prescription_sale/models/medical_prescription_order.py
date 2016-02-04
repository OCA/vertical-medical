# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


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
