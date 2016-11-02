# -*- coding: utf-8 -*-
# Copyright 2015 ACSONE SA/NV
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Medicament",
    "summary": "Introduce Medicament notion into the medical product.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "http://acsone.eu",
    "author": "ACSONE SA/NV, LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "medical",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/medical_drug_form.xml",
        "data/medical_drug_route.xml",
        "views/product_product_view.xml",
        "views/medical_medicament_view.xml",
        "views/medical_drug_form_view.xml",
        "views/medical_drug_route_view.xml",
        "views/medical_menu.xml",
    ],
    "demo": [
        "demo/medical_medicament_demo.xml",
    ],
}
