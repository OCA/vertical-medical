# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical_medication,
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical_medication is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     medical_medication is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with medical_medication.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Medical Medication',
<<<<<<< HEAD
    'version': '8.0.1.0.0',
    'author': 'ACSONE SA/NV, Odoo Community Association (OCA)',
    'maintainer': 'ACSONE SA/NV, Odoo Community Association (OCA)',
    'website': 'http://www.acsone.eu',
    'license': 'AGPL-3',
=======
    'version': '9.0.1.1.0',
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "maintainer": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "http://www.acsone.eu",
>>>>>>> Update active module versions to v9. Leave unported for organization while still in conversion phases
    'category': 'Medical',
    'depends': [
        'medical',
        'medical_disease',
        'medical_medicament',
    ],
    'summary': 'Introduce medication notion into the medical addons',
    'data': [
        'security/ir.model.access.csv',
        'data/product_uom.xml',
        'data/medical_medication_dosage.xml',
        'views/medical_medication_dosage_view.xml',
        'views/medical_medication_template_view.xml',
        'views/medical_patient_medication_view.xml',
        'views/medical_patient_view.xml',
    ],
    'installable': False,
    'auto_install': False,
}
