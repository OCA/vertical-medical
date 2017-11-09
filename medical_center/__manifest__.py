# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Medical Centers",
    "summary": "Adds a concept of Medical Centers to Patients.",
    "version": "11.0.1.0.0",
    "category": "Medical",
    "website": "https://github.com/OCA/vertical-medical",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "medical",
    ],
    "data": [
        "views/medical_center.xml",
        "views/medical_patient.xml",
        "views/medical_menu.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [
        "demo/medical_center.xml",
    ],
}
