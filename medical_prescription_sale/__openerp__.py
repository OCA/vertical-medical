# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Medical Prescription Sales',
    'summary': 'Create Sale Orders from Prescriptions',
    'version': '9.0.0.1.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'sale',
        'stock',
        'medical_prescription',
        'medical_pharmacy',
        'medical_prescription_thread',
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    "data": [
        'data/ir_sequence.xml',
        'data/product_category_data.xml',
        'wizards/medical_sale_wizard_view.xml',
        'wizards/medical_sale_temp_view.xml',
        'views/prescription_order_line_view.xml',
        'views/prescription_order_view.xml',
        'views/sale_order_view.xml',
        'views/medical_physician_view.xml',
        'views/medical_patient_view.xml',
    ],
    'demo': [
        'demo/medical_medicament_demo.xml',
        'demo/medical_medication_demo.xml',
        'demo/medical_prescription_order_demo.xml',
        'demo/medical_prescription_order_line_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
