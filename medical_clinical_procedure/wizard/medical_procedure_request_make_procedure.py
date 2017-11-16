# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import _, api, exceptions, models


class ProcedureRequestMakeProcedure(models.Model):
    _name = "procedure.request.make.procedure"
    _description = "From Procedure Request Make Procedure"

    @api.multi
    def make_procedure(self):
        res = []
        active_ids = self.env.context.get('active_ids', []) or []
        for pr in self.env['medical.procedure.request'].browse(active_ids):
            if pr.procedure_ids:
                raise exceptions.Warning(
                    _('This Procedure Request already has a Procedure.'))
            procedure = pr.generate_event()
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
