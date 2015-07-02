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

    'name': 'OeMedical : Free Health and Hospital Information System',
    'version': '1.0',
    'author': "OeMEdical Team,Odoo Community Association (OCA)",
    'category': 'Generic Modules/Others',
    'depends': ['base', 'sale', 'purchase', 'account', 'product'],
    'application': True,
    'description': """

About OeMedical
---------------

OeMedical is a multi-user, highly scalable, centralized Electronic
Medical Record (EMR) and Hospital Information System for openERP.

OeMedical provides a free universal Health and Hospital Information System,
so doctors and institutions all over the world,
specially in developing countries will benefit from a centralized,
high quality, secure and scalable system.

OeMedical at a glance:

    * Strong focus in family medicine and Primary Health Care

    * Major interest in Socio-economics (housing conditions, substance abuse,
    education...)

    * Diseases and Medical procedures standards (like ICD-10 / ICD-10-PCS ...)

    * Patient Genetic and Hereditary risks : Over 4200 genes related to
    diseases (NCBI / Genecards)

    * Epidemiological and other statistical reports

    * 100% paperless patient examination and history taking

    * Patient Administration
    (creation, evaluations / consultations, history ... )

    * Doctor Administration

    * Lab Administration

    * Medicine / Drugs information (vademécum)

    * Medical stock and supply chain management

    * Hospital Financial Administration

    * Designed with industry standards in mind

    * Open Source : Licensed under AGPL

""",
    "website": "http://launchpad.net/oemedical",
    "licence": "AGPL v3",
    "data": [
        'sequence/oemedical_sequence.xml',
        'views/oemedical_secondary_condition_view.xml',
        'views/oemedical_pathology_category_view.xml',
        'views/oemedical_signs_and_symptoms_view.xml',
        'views/product_product_view.xml',
        'views/oemedical_physician_view.xml',
        'views/oemedical_directions_view.xml',
        'views/oemedical_insurance_view.xml',
        'views/res_partner_view.xml',
        'views/oemedical_pathology_view.xml',
        'views/oemedical_operational_area_view.xml',
        'views/oemedical_ethnicity_view.xml',
        'views/oemedical_operational_sector_view.xml',
        'views/oemedical_prescription_order_view.xml',
        'views/oemedical_medicament_category_view.xml',
        'views/oemedical_insurance_plan_view.xml',
        'views/oemedical_diagnostic_hypothesis_view.xml',
        'views/oemedical_procedure_view.xml',
        'views/oemedical_medication_template_view.xml',
        'views/oemedical_vaccination_view.xml',
        'views/oemedical_medication_dosage_view.xml',
        'views/oemedical_family_member_view.xml',
        'views/oemedical_hospital_ward_view.xml',
        'views/oemedical_hospital_or_view.xml',
        'views/oemedical_drug_form_view.xml',
        'views/oemedical_patient_medication_view.xml',
        'views/oemedical_patient_evaluation_view.xml',
        'views/oemedical_hospital_building_view.xml',
        'views/oemedical_patient_view.xml',
        'views/oemedical_prescription_line_view.xml',
        'views/oemedical_patient_disease_view.xml',
        'views/oemedical_drug_route_view.xml',
        'views/oemedical_hospital_unit_view.xml',
        'views/oemedical_appointment_view.xml',
        'views/oemedical_specialty_view.xml',
        'views/oemedical_family_view.xml',
        'views/oemedical_hospital_bed_view.xml',
        'views/oemedical_occupation_view.xml',
        'views/oemedical_disease_group_members_view.xml',
        'views/oemedical_medicament_view.xml',
        'views/oemedical_pathology_group_view.xml',
        #'views/oemedical_gynecology_and_obstetrics_view.xml',   # view has errors, please correct before enabling....
        #'views/oemedical_lifestyle_view.xml',
        'views/data/recreational_drugs.xml',
        #'views/oemedical_disease_gene_view.xml',  # view has errors, please correct before enabling....
        'views/data/disease_genes.xml',
        #'views/oemedical_socioeconomics_view.xml', # view has errors, please correct before enabling....
        #'views/oemedical_lab_view.xml',  # view has errors, please correct before enabling....
        'security/oemedical_security.xml',
        'security/ir.model.access.csv',
        'oemedical_menu.xml',
    ],
    "demo": [

    ],
    'test': [
        'test/physician.yml',
        'test/patient.yml',
        'test/partners.yml',
        'test/insurance_plan.yml',
        'test/insurance.yml',
        'test/physician_speciality.yml'
    ],
    'css': [

    ],
    'js': [

    ],
    'qweb': [

    ],
    "active": False,
    "installable": False,
}

