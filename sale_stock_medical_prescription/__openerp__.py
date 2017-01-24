# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Prescription Sale Stock",
    "summary": "Provides dispense logic for prescriptions.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "post_init_hook": "_update_medicament_type",
    "depends": [
        "sale_stock",
        "sale_medical_prescription",
    ],
    "data": [
        "data/stock_data.xml",
        "views/stock_warehouse_view.xml",
        "views/prescription_order_view.xml",
        "views/prescription_order_line_view.xml",
    ],
    "demo": [
        "demo/medical_patient_demo.xml",
        "demo/medical_medicament_demo.xml",
        "demo/medical_pharmacy_demo.xml",
        "demo/medical_physician_demo.xml",
        "demo/medical_patient_medication_demo.xml",
        "demo/medical_prescription_order_demo.xml",
        "demo/medical_prescription_order_line_demo.xml",
        "demo/sale_order_demo.xml",
        "demo/sale_order_line_demo.xml",
        "demo/procurement_order_demo.xml",
    ],
}
