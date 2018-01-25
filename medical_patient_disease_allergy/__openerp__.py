# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    "name": "Medical Patient Allergies",
    "summary": "Isolates allergies from diseases.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com/",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "GPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical_patient_disease",
    ],
    "data": [
        "data/medical_pathology_code_type.xml",
        "views/medical_patient_disease_view.xml",
        "views/medical_patient_view.xml",
    ],
    "demo": [
        "demo/medical_pathology_demo.xml",
        "demo/medical_patient_demo.xml",
        "demo/medical_patient_disease_demo.xml",
    ],
}
