# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Medicament Physical Attributes',
    'summary': 'Add abstract physical attributes to medical medicaments.',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_medicament',
    ],
    "website": "http://github.com/oca/vertical-medical",
    "license": "AGPL-3",
    "data": [
        'views/medical_medicament_view.xml',
        'views/medical_medicament_attribute_view.xml',
        'views/medical_medicament_attribute_type_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
