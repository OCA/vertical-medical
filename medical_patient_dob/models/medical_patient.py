# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: James Foster <jfoster@laslabs.com>
#    Copyright: 2016-TODAY LasLabs, Inc. [https://laslabs.com]
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

from datetime import datetime
from openerp import api, models


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    @api.multi
    def format_dob(self, ):
        return datetime.strptime(self.dob, '%Y-%m-%d').strftime('%m/%d/%Y')

    @api.multi
    def name_get(self, ):
        res = []
        for rec_id in self:
            if rec_id.dob:
                name = '%s %s' % (rec_id.name, rec_id.format_dob())
            else:
                name = rec_id.name
            res.append((rec_id.id, name))
        return res
