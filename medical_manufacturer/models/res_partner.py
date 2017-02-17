# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_manufacturer = fields.Boolean(
        string='Is Manufacturer',
    )
