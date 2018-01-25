# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical_medicament,
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical_medicament is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     medical_medicament is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with medical_medicament.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Medical Medicament',
    'version': '8.0.1.0.0',
    'author': 'ACSONE SA/NV, Odoo Community Association (OCA)',
    'maintainer': 'ACSONE SA/NV, Odoo Community Association (OCA)',
    'website': 'http://www.acsone.eu',
    'license': 'GPL-3',
    'category': 'Medical',
    'depends': [
        'medical',
        'product',
    ],
    'summary': 'Introduce Medicament notion into the medical product',
    'data': [
        'security/ir.model.access.csv',
        'data/medical_drug_form.xml',
        'data/medical_drug_route.xml',
        'views/product_product_view.xml',
        'views/medical_medicament_view.xml',
        'views/medical_drug_form_view.xml',
        'views/medical_drug_route_view.xml',
    ],
    'installable': False,
    'auto_install': False,
}
