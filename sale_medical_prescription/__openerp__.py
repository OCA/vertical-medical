# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Prescription Sales",
    "summary": "Create sale orders from prescriptions.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale",
        "stock",
        "medical_prescription",
        "medical_pharmacy",
        "mail_thread_medical_prescription",
    ],
    "data": [
        "data/ir_sequence.xml",
        "data/product_category_data.xml",
        "views/medical_pharmacy_view.xml",
        "views/medical_medicament_view.xml",
        "views/prescription_order_line_view.xml",
        "views/prescription_order_view.xml",
        "views/sale_order_view.xml",
        "views/medical_physician_view.xml",
        "views/medical_patient_view.xml",
        "wizards/medical_sale_wizard_view.xml",
        "wizards/medical_sale_temp_view.xml",
    ],
    "demo": [
        "demo/product_category_demo.xml",
        "demo/medical_patient_demo.xml",
        "demo/medical_medicament_demo.xml",
        "demo/medical_physician_demo.xml",
        "demo/medical_pharmacy_demo.xml",
        "demo/medical_patient_medication_demo.xml",
        "demo/medical_prescription_order_demo.xml",
        "demo/medical_prescription_order_line_demo.xml",
        "demo/sale_order_demo.xml",
        "demo/sale_order_line_demo.xml",
    ],
}
