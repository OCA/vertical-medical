# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Medical Prescription Disease State',
    'summary': 'Adds state and more prescription context to disease concept',
    'version': '9.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_prescription_disease',
    ],
    'data': [
        'views/medical_patient_disease_view.xml',
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    'installable': True,
    'auto_install': False,
}
