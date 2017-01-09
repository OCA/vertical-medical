# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Physician',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical',
        'medical_center',
        'product',
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    "data": [
        'views/medical_physician_view.xml',
        'views/medical_specialty_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
        'wizard/medical_physician_unavailable_view.xml',
        'data/ir_sequence_data.xml',
        'data/medical_specialties.xml',
    ],
    'demo': [
        'demo/medical_physician.xml',
    ],
    "application": False,
    'installable': True,
}
