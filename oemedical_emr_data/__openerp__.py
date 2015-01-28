##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    OeMedical, HMS Opensource Solution
##############################################################################
#    Collaborators of this module:
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Coded by: Parthiv Patel <parthiv@techreceptives.com>
#    Coded by: Ruchir Shukla <ruchir@techreceptives.com>
#    Planifyied by: Parthiv Patel <parthiv@techreceptives.com>
#    Planifyied by: Nhomar Hernandéz <nhomar@vauxoo.com>
#
##############################################################################
#    This project is mantained by OeMEdical Team:
#    https://launchpad.net/oemedical
#
##############################################################################
#    It is a collaborative effort between several companies that want to join
#    efforts in have a proposal solid and strong in the Health Care environment
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{

    'name': 'OeMedical EMR: Module Data',
    'version': '1.0',
    'author': "OeMEdical Team",
    'category': 'Generic Modules/Others',
    'depends': ['oemedical_emr'],
    'application': True,
    'description': """

About OeMedical Data
---------------------

Core Data for oemedical, is kept as a separate module to overcome need of
localizing core data.


""",
    "website": "http://launchpad.net/oemedical",
    "licence": "AGPL v3",
    "data": [
        'data/medicament_categories.xml',
        'data/WHO_products.xml',
        'data/WHO_list_of_essential_medicines.xml',
        'data/health_specialties.xml',
        'data/ethnic_groups.xml',
        'data/occupations.xml',
        'data/dose_units.xml',
        'data/drug_routes.xml',
        'data/medicament_form.xml',
        'data/medication_frequencies.xml',
        'data/disease_categories.xml',
        'data/diseases.xml',
    ],
    "demo": [

    ],
    'test': [

    ],
    'css': [

    ],
    'js': [

    ],
    'qweb': [

    ],
    "active": False
}
