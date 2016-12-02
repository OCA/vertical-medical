# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Pathology - ICD-10",
    "summary": "This module provides ICD-10-CM data import for pathologies.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com/",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "medical_pathology",
    ],
    "data": [
        "wizards/medical_pathology_icd10.xml",
        "views/medical_menu.xml",
    ],
    "installable": True,
}
