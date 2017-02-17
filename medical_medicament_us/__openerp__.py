# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Medical Medicament - US Locale",
    "summary": "Extension of medical_medicament that provides US locale.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical_base_us",
        "medical_manufacturer",
    ],
    "data": [
        "views/medical_medicament_view.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [
        "demo/medical_manufacturer_demo.xml",
        "demo/medical_medicament_gcn_demo.xml",
        "demo/medical_medicament_demo.xml",
        "demo/medical_medicament_ndc_demo.xml",
    ],
}
