# -*- coding: utf-8 -*-
# #############################################################################
#
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
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
# #############################################################################

from openerp import models, api
from openerp.models import MAGIC_COLUMNS


class AbstractMedicalMedication(models.AbstractModel):
    _name = 'abstract.medical.medication'
    _description = 'Abstract Medical Medication'

    @api.one
    @api.onchange('medication_template_id')
    def onchange_template_id(self):
        if self.medication_template_id:
            values = self.medication_template_id.read()[0]
            for k in values.keys():
                if k not in MAGIC_COLUMNS:
                    setattr(self, k, getattr(self.medication_template_id, k))
