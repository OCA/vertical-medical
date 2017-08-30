# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import _, api, exceptions, fields, models


class ProcedureRequestMakeProcedure(models.Model):
    _name = "procedure.request.make.procedure"
    _description = "From Procedure Request Make Procedure"

    @api.model
    def _prepare_procedure(self, pr):
        data = {
            'subject_id': pr.subject_id.id,
            'performer_id': pr.performer_id.id,
            'priority': pr.priority,
            'procedure_request_id': pr.id,
            'title': pr.title,
            'service_id': pr.service_id.id,
            'center_id': pr.center_id.id,
             }
        return data

    @api.multi
    def make_procedure(self):
        res = []
        active_ids = self.env.context.get('active_ids', []) or []
        procedure_obj = self.env['medical.procedure']
        for pr in self.env['medical.procedure.request'].browse(active_ids):
            if pr.procedure_ids:
                raise exceptions.Warning(_('This Procedure Request '
                                           'already has a Procedure.'))
            proc_data = self._prepare_procedure(pr)
            procedure = procedure_obj.create(proc_data)
            res.append(procedure.id)
        return {
            'domain': "[('id','in', [" + ','.join(map(str, res)) + "])]",
            'name': _('Procedure'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'medical.procedure',
            'view_id': False,
            'context': False,
            'type': 'ir.actions.act_window'
            }
