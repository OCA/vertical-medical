# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    "name": "Medical Pathology",
    "summary": "Extends Odoo Medical with pathologies (diseases).",
    "version": "10.0.1.0.0",
    "category": "Medical",
    "website": "https://github.com/OCA/vertical-medical",
    "author": "LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)",
    "license": "GPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical",
    ],
    "data": [
        "views/medical_pathology_category_view.xml",
        "views/medical_pathology_view.xml",
        "views/medical_menu.xml",
        "data/medical_pathology_code_type.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [
        "demo/medical_pathology_category_demo.xml",
        "demo/medical_pathology_demo.xml",
    ],
}
