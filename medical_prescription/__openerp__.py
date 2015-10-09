# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical_prescription,
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical_prescription is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     medical_prescription is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with medical_prescription.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Medical Prescription',
    'version': '8.0.1.0.0',
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "maintainer": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "http://www.acsone.eu",
    'category': 'Medical',
    'depends': [
        'medical',
        'medical_medicament',
        'medical_medication',
    ],
    'summary': 'This module introduce the prescription/prescription line '
    'into the medical addons.',
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/medical_prescription_order_view.xml',
        'views/medical_prescription_order_line_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
