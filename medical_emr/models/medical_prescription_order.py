# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
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
# #############################################################################

from odoo import models, fields


class MedicalPrescriptionOrder(models.Model):
    _inherit = 'medical.prescription.order'

    def print_prescription(self, cr, uid, ids, context=None):
        """
        """
        #        assert len(ids) == 1, 'This option should only be used for '
        #                              'a single id at a time'
        #        wf_service = netsvc.LocalService("workflow")
        #        wf_service.trg_validate(uid, 'medical.prescription.order',
        #                                ids[0], 'prescription_sent', cr)
        datas = {
            'model': 'medical.prescription.order',
            'ids': ids,
            'drug_form_id': self.read(cr, uid, ids[0], context=context),
        }
        return {'type': 'ir.actions.report.xml',
                'report_name': 'prescription.order',
                'datas': datas,
                'nodestroy': True}


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'

    is_printed = fields.Boolean(
        help='Check this box to print this line of the prescription.',
        default=True)
    refills = fields.Integer(string='Refills #')
    review = fields.Datetime()
