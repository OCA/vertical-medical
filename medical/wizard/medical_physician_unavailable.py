# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.osv import osv
from openerp.osv import fields


class MedicalPhysicianUnavailableWizard(osv.TransientModel):
    _name = 'medical.physician.unavailable.wizard'
    _description = 'Asistente para la definicion de indisponibilidades'

    _columns = {
        'physician_id': fields.many2one('medical.physician', 'Physician',
                                        required=True),
        'date_start': fields.datetime(string='Start', required=True),
        'date_end': fields.datetime(string='End', required=True),
        'institution_id': fields.many2one('res.partner', 'Medical Center',
                                          select=1,
                                          domain="[('is_institution', '=', "
                                                 "True), ]"),
    }
    _defaults = {
        'date_start': fields.date.today(),
        'date_end': fields.date.today(),
    }

    def action_cancel(self, cr, uid, ids, context=None):
        return {'type': 'ir.actions.act_window_close'}

    def action_set_unavailable(self, cr, uid, ids, context=None):
        if not ids:
            return {}

        appointment_proxy = self.pool['medical.appointment']

        this = self.browse(cr, uid, ids)[0]
        physician_id = this.physician_id.id
        institution_id = this.institution_id.id
        if institution_id:
            institution_ids = [institution_id]
        else:
            institution_ids = []

        date_start = this.date_start
        date_end = this.date_end

        appointment_proxy._remove_empty_clashes(cr, uid, [], [physician_id],
                                                institution_ids, date_start,
                                                date_end, context=context)
        appointment_proxy._set_clashes_state_to_review(cr, uid, [physician_id],
                                                       institution_ids,
                                                       date_start, date_end,
                                                       context=context)

        return {'type': 'ir.actions.act_window_close'}
