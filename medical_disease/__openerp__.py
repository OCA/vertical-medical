# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical_disease,
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical_disease is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     medical_disease is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with medical_disease.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Medical Disease',
    'version': '9.0.1.1.0',
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "maintainer": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "http://www.acsone.eu",
    'category': 'Medical',
    'depends': [
        'medical',
    ],
    'summary': 'Introduce disease notion into the medical category',
    'data': [
        'security/ir.model.access.csv',
        'views/medical_pathology_view.xml',
        'views/medical_pathology_category_view.xml',
        'views/medical_pathology_group_view.xml',
        'views/medical_patient_disease_view.xml',
        'views/medical_patient_view.xml',
        'views/medical_disease_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
