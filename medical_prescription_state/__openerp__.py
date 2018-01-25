# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    'name': 'Medical Prescription Order States',
    'version': '9.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'website': 'https://laslabs.com',
    'license': 'GPL-3',
    'depends': [
        'base_kanban_stage',
        'medical_prescription',
    ],
    'data': [
        'views/medical_prescription_order.xml',
        'views/medical_prescription_order_line.xml',
    ],
    'installable': True,
    'auto_install': False,
}
