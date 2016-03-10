# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Prescription',
    'version': '9.0.1.0.0',
    "author": "ACSONE SA/NV, LasLabs, Odoo Community Association (OCA)",
    "maintainer": "ACSONE SA/NV, LasLabs, Odoo Community Association (OCA)",
    "website": "http://www.acsone.eu",
    'category': 'Medical',
    'depends': [
        'medical',
        'medical_medicament',
        'medical_medication',
        'medical_physician',
    ],
    'summary': 'This module introduce the prescription/prescription line'
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
