# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    "name": "Medical Physician",
    "summary": "Adds physicians to Odoo Medical.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "GPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical",
        "product",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "data/medical_specialties.xml",
        "security/ir.model.access.csv",
        "views/medical_physician_view.xml",
        "views/medical_specialty_view.xml",
        "views/medical_menu.xml",
    ],
    "demo": [
        "demo/medical_physician_demo.xml",
    ],
}
