# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Prescription Order State Verification',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Medical Team, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_prescription_state',
    ],
    'website': "https://laslabs.com",
    'licence': "AGPL-3",
    'data': [
        'views/medical_prescription_order_state_view.xml',
        'data/medical_prescription_order_state_data.xml',
    ],
    'installable': False,
    'auto_install': False,
}
