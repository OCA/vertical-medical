# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Pathology",
    "summary": "Extends Odoo Medical with pathologies (diseases).",
    "version": "9.0.1.0.1",
    "category": "Medical",
    "website": "https://laslabs.com/",
    "author": "LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical",
    ],
    "data": [
        "views/medical_pathology_category_view.xml",
        "views/medical_pathology_group_view.xml",
        "views/medical_pathology_view.xml",
        "views/medical_menu.xml",
        "data/medical_pathology_code_type.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [
        "demo/medical_pathology_category_demo.xml",
        "demo/medical_pathology_group_demo.xml",
        "demo/medical_pathology_demo.xml",
    ],
}
