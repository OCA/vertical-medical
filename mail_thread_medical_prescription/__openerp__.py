# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Medical Prescription Thread",
    "summary": "Adds message threads to rx orders and rx order lines.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://laslabs.com/",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical_prescription",
    ],
    "data": [
        "views/medical_prescription_order_view.xml",
        "views/medical_prescription_order_line_view.xml"
    ],
}
