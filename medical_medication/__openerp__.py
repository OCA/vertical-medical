# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Medication',
    'version': '9.0.1.0.0',
    "author": "LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)",
    "maintainer": "LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)",
    "website": "http://www.acsone.eu",
    'category': 'Medical',
    'depends': [
        'medical',
        'medical_patient_disease',
        'medical_physician',
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
    'demo': [
        'demo/medical_medication_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
