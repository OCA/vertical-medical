# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Medical Website - Insurance Pricelist',
    'description': 'Adds Insurance logic to Website pricelists',
    'version': '9.0.1.0.0',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'website_sale',
        'medical_insurance_pricelist',
    ],
    'data': [
        'views/website_pricelist_view.xml',
    ],
    'website': 'https://laslabs.com',
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
