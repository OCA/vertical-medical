# Copyright 2025 Invitu
# License AGPL-3.0 or later (https://gnu.org/licenses/agpl).
{
    "name": "Point of Sale - Partner Birthdate Weight Mandatory",
    "summary": "The customer weight is required according" "to their date of birth",
    "version": "17.0.1.0.0",
    "category": "Point Of Sale",
    "website": "https://github.com/OCA/vertical-medical",
    "author": "Invitu, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "pos_partner_birthdate_warning",
        "pos_partner_weight",
    ],
    "data": ["views/res_config_settings.xml"],
}
