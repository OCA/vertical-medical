# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Patient Allergies",
    "summary": "Isolate the allergy concept in medical_disease",
    "version": "10.0.2.0.0",
    "category": "Medical",
    "website": "https://laslabs.com/",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "maintainer": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical_patient_disease",
    ],
    "data": [
        "views/medical_patient_disease_view.xml",
        "views/medical_patient_view.xml",
        'data/medical_pathology_code_type.xml',
    ],
}
