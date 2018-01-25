# -*- coding: utf-8 -*-
# Copyright 2004-2009 Tiny SPRL
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    "name": "Odoo Medical",
    "summary": "Extends Odoo with medical patients and centers.",
    "version": "9.0.1.0.0",
    "category": "Medical",
    "website": "https://odoo-community.org/",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "GPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
        "product",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "security/medical_security.xml",
        "security/ir.model.access.csv",
        "views/medical_patient_view.xml",
        "views/res_partner_view.xml",
        "views/medical_menu.xml",
    ],
    "demo": [
        "demo/medical_patient_demo.xml",
    ],
}
