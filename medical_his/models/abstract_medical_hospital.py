# -*- coding: utf-8 -*-
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class AbstractHospital(models.AbstractModel):
    _name = 'abstract.medical.hospital'
    _description = 'Abstract Medical Hospital'

    @api.one
    @api.depends('active')
    def _compute_expire_date(self):
        if self.active:
            self.expire_date = False
        else:
            self.expire_date = fields.datetime.now()

    active = fields.Boolean(string='Active', default=1)
    expire_date = fields.Datetime(string='Expire Date')

    @api.one
    def action_invalidate(self):
        self.active = False
        self.expire_date = fields.datetime.now()

    @api.one
    def action_revalidate(self):
        self.active = True
