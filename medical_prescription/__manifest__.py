# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Prescription",
    "summary": "Introduces prescription orders and prescription order lines.",
    "version": "10.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "ACSONE SA/NV, LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical_medication",
        "medical_pharmacy",
    ],
    "data": [
        "data/ir_sequence.xml",
        "security/ir.model.access.csv",
        "views/medical_prescription_order_view.xml",
        "views/medical_prescription_order_line_view.xml",
        "views/medical_menu.xml",
    ],
    "demo": [
        "demo/medical_patient_demo.xml",
        "demo/medical_pharmacy_demo.xml",
        "demo/medical_physician_demo.xml",
        "demo/medical_prescription_order_demo.xml",
        "demo/medical_prescription_order_line_demo.xml",
    ],
}
