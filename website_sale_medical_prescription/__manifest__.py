# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Sale Medical Prescription',
    'summary': 'Adds prescription information to website checkout process',
    'version': '10.0.1.0.0',
    'category': 'Website',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'medical_prescription_sale',
        'website_sale',
        'website_medical_prescription_order_line',
        'website_sale_medical_medicament',
        'website_field_autocomplete_related',
    ],
    'data': [
        'views/medical_prescription_order_template.xml',
        'views/assets.xml',
        'security/ir.model.access.csv',
        'security/medical_patient_security.xml',
        'security/medical_physician_security.xml',
        'security/medical_pharmacy_security.xml',
        'security/res_partner_security.xml',
        'security/medical_patient_medication_security.xml',
        'security/medical_prescription_order_security.xml',
        'security/ir_sequence_security.xml',
    ],
}
