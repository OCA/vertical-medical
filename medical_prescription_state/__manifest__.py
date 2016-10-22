# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Prescription Order States',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_base_kanban',
        'medical_prescription',
    ],
    'website': 'http://github.com/oca/vertical-medical',
    'license': 'AGPL-3',
    'data': [
        'views/medical_prescription_order.xml',
        'views/medical_prescription_order_line.xml',
    ],
    'installable': True,
    'auto_install': False,
}
