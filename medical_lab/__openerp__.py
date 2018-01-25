# -*- coding: utf-8 -*-
# Copyright 2004-2009 Tiny SPRL
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    "name": "Medical Lab",
    "version": "9.0.1.0.0",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "category": "Medical",
    "website": "https://github.com/OCA/vertical-medical",
    "license": "GPL-3",
    "installable": True,
    "depends": [
        "medical_pathology",
        "medical_physician",
    ],
    "data": [
        "views/medical_lab.xml",
        "views/medical_lab_patient.xml",
        "views/medical_lab_test_type.xml",
        "views/medical_patient.xml",
        "views/medical_menu.xml",
        "security/medical_security.xml",
        "security/ir.model.access.csv",
    ],
}
