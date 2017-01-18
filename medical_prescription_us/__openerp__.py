# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Prescription - US Locale",
    "summary": "Extension of medical_prescription that provides US Locale",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical_medicament_us",
        "medical_prescription",
    ],
    "data": [
        "views/medical_prescription_order_line_view.xml",
    ],
    "demo": [
        "demo/medical_patient_demo.xml",
        "demo/medical_pharmacy_demo.xml",
        "demo/medical_medicament_demo.xml",
        "demo/medical_physician_demo.xml",
        "demo/medical_patient_medication_demo.xml",
        "demo/medical_prescription_order_demo.xml",
        "demo/medical_prescription_order_line_demo.xml",
    ],
}
