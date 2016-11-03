# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Prescription Sale Stock',
    'summary': 'Provides Dispense Logic for Prescriptions',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'sale_stock',
        'sale_medical_prescription',
    ],
    'data': [
        'data/stock_data.xml',
        'views/stock_warehouse_view.xml',
        'views/prescription_order_view.xml',
        'views/prescription_order_line_view.xml',
    ],
    'demo': [
        'demo/medical_prescription_order_line_demo.xml',
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    'installable': True,
    'auto_install': False,
    'post_init_hook': 'post_init_hook_for_new_medicament_type',
}
