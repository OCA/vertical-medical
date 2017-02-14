# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": " Sale CRM - Medical Prescription",
    "summary": "Create opportunities from prescriptions.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale_crm",
        "sale_medical_prescription",
    ],
    "data": [
        "wizards/medical_lead_wizard_view.xml",
        "views/crm_lead_view.xml",
    ],
    "demo": [
        "demo/medical_medicament_demo.xml",
        "demo/medical_patient_demo.xml",
        "demo/medical_pharmacy_demo.xml",
        "demo/medical_physician_demo.xml",
        "demo/medical_patient_medication_demo.xml",
        "demo/medical_prescription_order_demo.xml",
        "demo/medical_prescription_order_line_demo.xml",
        "demo/crm_lead_demo.xml",
    ],
}
