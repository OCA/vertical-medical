# -*- coding: utf-8 -*-
# Copyright 2015 ACSONE SA/NV
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Medical Medication",
    "summary": "Introduce medication notion into the medical addons.",
    "version": "9.0.1.0.1",
    "category": "Medical",
    "website": "http://www.acsone.eu",
    "author": "LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical_patient_disease",
        "medical_medicament",
    ],
    "data": [
        "data/product_uom.xml",
        "data/medical_medication_dosage.xml",
        "security/ir.model.access.csv",
        "views/medical_medication_dosage_view.xml",
        "views/medical_medication_template_view.xml",
        "views/medical_patient_medication_view.xml",
        "views/medical_patient_view.xml",
        "views/medical_menu.xml",
    ],
    "demo": [
        "demo/medical_patient_demo.xml",
        "demo/medical_medicament_demo.xml",
        "demo/medical_pathology_demo.xml",
        "demo/medical_patient_medication_demo.xml",
    ],
}
