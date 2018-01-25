# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html)

{
    'name': 'Medical Practitioner - US Locale',
    'summary': 'Adds several US IDs to medical practitioners',
    'version': '10.0.1.0.0',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'GPL-3',
    'category': 'Medical',
    'depends': [
        'medical_base_us',
        'medical_practitioner',
    ],
    'data': [
        'data/res_partner_id_category.xml',
        'views/medical_practitioner.xml',
    ],
    'application': False,
    'installable': True,
}
