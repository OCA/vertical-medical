# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def get_pricelist_available(self, show_visible=False):
        pricelist_ids = super(Website, self).get_pricelist_available(
            show_visible
        )
        partner_int = self.env.user.partner_id.id
        # More efficient than any way I could think of in ORM
        self.env.cr.execute(
            """SELECT DISTINCT(insurance_template_id)
                 FROM medical_insurance_plan ins
            LEFT JOIN medical_patient pat
                   ON ins.patient_id = pat.id
            LEFT JOIN res_partner partner
                   ON pat.partner_id = partner.id
                WHERE partner.parent_id = %s
                   OR pat.partner_id = %s""",
            (partner_int, partner_int)
        )
        template_ints = [t[0] for t in self.env.cr.fetchall()]

        def check_pricelist(rec_id):
            try:
                if len(rec_id.insurance_template_ids):
                    temp_ids = rec_id.insurance_template_ids
                    for i in temp_ids:
                        if i.pricelist_id.id in template_ints:
                            return True
                    return False
            except Exception:
                return False
            return True

        return pricelist_ids.filtered(check_pricelist)
