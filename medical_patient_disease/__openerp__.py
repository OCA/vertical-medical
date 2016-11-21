# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Patient Disease",
    "summary": "Extend medical patients with the concept of diseases.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical_pathology",
        "medical_physician",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/medical_patient_disease_view.xml",
        "views/medical_patient_view.xml",
        "views/medical_menu.xml",
    ],
    "demo": [
        "demo/medical_pathology_category_demo.xml",
        "demo/medical_patient_demo.xml",
        "demo/medical_patient_disease_demo.xml",
    ]
}
