# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import models, api
from openerp.models import MAGIC_COLUMNS


class AbstractMedicalMedication(models.AbstractModel):
    _name = 'abstract.medical.medication'
    _description = 'Abstract Medical Medication'

    @api.multi
    @api.onchange('medication_template_id')
    def onchange_template_id(self):
        for rec_id in self:
            if rec_id.medication_template_id:
                values = rec_id.medication_template_id.read()[0]
                for k in values.keys():
                    if k not in MAGIC_COLUMNS:
                        attr = getattr(rec_id.medication_template_id, k)
                        setattr(self, k, attr)
