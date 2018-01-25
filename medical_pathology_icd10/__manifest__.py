# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html)

{
    'name': 'Medical Pathology - ICD-10-CM Import',
    'summary': 'Supports the import of ICD-10-CM pathology data',
    'version': '10.0.1.0.0',
    'category': 'Medical',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'license': 'GPL-3',
    'depends': [
        'medical_pathology_import',
    ],
    'installable': True,
    'data': [
        'demo/medical_pathology_import.xml',
    ],
}
