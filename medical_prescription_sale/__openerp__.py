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
        'medical_prescription',
        'medical_pharmacy',
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    "data": [
        'data/ir_sequence.xml',
        'wizards/medical_sale_wizard_view.xml',
        'wizards/medical_sale_temp_view.xml',
        'views/prescription_order_line_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
