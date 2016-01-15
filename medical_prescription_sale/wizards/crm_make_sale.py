# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
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

from openerp import models, api, fields
import logging


_logger = logging.getLogger(__name__)


class CrmMakeSale(models.TransientModel):
    _inherit = 'crm.make.sale'

    def _compute_default_is_prescription(self, ):
        active_id = self._context.get('active_id', False)
        if not active_id:
            return False
        lead_id = self.env['crm.lead'].get(active_id)
        return lead_id.is_prescription

    is_prescription = fields.Boolean(
        readonly=True,
        default=_compute_default_is_prescription,
    )

    @api.multi
    def makeOrder(self, ):
        """
        This function creates Quotation on given case.
        :return: Dictionary value of created sales order.
        :rtype: dict
        """
        if not self.is_prescription:
            return super(CrmMakeSale)
        raise NotImplementedError(
            'Todo, v9 breaks this so not worth the effort here',
        )
        # model_obj = self.env['ir.model.data']
        # wizard_id = model_obj.xmlid_to_object(
        #     'medical_pharmacy.medical_rx_sale_wizard_form_view',
        # )
        # action_id = model_obj.xmlid_to_object(
        #     'medical_pharmacy.medical_rx_sale_wizard_action',
        # )
        # context = self._context.copy()
        # _logger.info('Created %s', sale_ids)
        # _logger.debug('%s %s %s', form_id, tree_id, action_id)
        # sale_ids = [s.id for s in sale_ids]
        # return {
        #     'name': action_id.name,
        #     'help': action_id.help,
        #     'type': action_id.type,
        #     'view_mode': 'tree',
        #     'view_id': tree_id.id,
        #     'views': [
        #         (tree_id.id, 'tree'), (form_id.id, 'form'),
        #     ],
        #     'target': 'current',
        #     'context': context,
        #     'res_model': action_id.res_model,
        #     'res_ids': sale_ids,
        #     'domain': [('id', 'in', sale_ids)],
        # }
