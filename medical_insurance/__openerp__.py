# -*- coding: utf-8 -*-
# Copyright 2015-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Insurance",
    "version": "9.0.1.0.0",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "category": "Medical",
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    "depends": [
        "medical"
    ],
    "data": [
        "views/medical_insurance_company_view.xml",
        "views/medical_insurance_template_view.xml",
        "views/medical_insurance_plan_view.xml",
        "views/medical_patient_view.xml",
        "security/ir.model.access.csv",
        "views/medical_menu.xml",
    ],
    "installable": True,
    "auto_install": False,
}
