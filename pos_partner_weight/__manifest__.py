# Copyright 2025 INVITU
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Point of Sale - Partner contact weight",
    "summary": "Adds the partner weight in the customer screen of POS",
    "version": "17.0.1.0.0",
    "development_status": "Beta",
    "category": "Point of sale",
    "website": "https://github.com/OCA/vertical-medical",
    "author": "INVITU, Odoo Community Association (OCA)",
    "maintainers": ["invitu"],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "point_of_sale",
        "partner_contact_weight",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_partner_weight/static/src/xml/screens.xml",
            "pos_partner_weight/static/src/js/ClientDetailsEdit.esm.js",
        ]
    },
}
