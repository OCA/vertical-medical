# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalPractitioner(models.Model):
    _name = 'medical.practitioner'
    _description = 'Medical Practitioner'
    _inherit = 'medical.abstract.entity'

    role_ids = fields.Many2many(
        string='Roles',
        comodel_name='medical.role',
    )
    practitioner_type = fields.Selection(
        string='Entity Type',
        selection=[('internal', 'Internal Entity'),
                   ('external', 'External Entity')],
        readonly=False,
    )
