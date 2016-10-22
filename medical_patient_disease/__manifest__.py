# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Patient Disease',
    'version': '10.0.1.0.0',
    "author": "LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)",
    "maintainer": "LasLabs, ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "http://www.acsone.eu",
    'category': 'Medical',
    'depends': [
        'medical_pathology',
    ],
    'summary': 'Introduce disease notion into the medical category',
    'data': [
        'security/ir.model.access.csv',
        'views/medical_patient_disease_view.xml',
        'views/medical_patient_view.xml',
        'views/medical_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
}
