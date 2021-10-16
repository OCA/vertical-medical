import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-vertical-medical",
    description="Meta package for oca-vertical-medical Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-medical',
        'odoo10-addon-medical_agpl',
        'odoo10-addon-medical_base_us',
        'odoo10-addon-medical_center',
        'odoo10-addon-medical_insurance',
        'odoo10-addon-medical_pathology',
        'odoo10-addon-medical_pathology_icd10',
        'odoo10-addon-medical_pathology_import',
        'odoo10-addon-medical_practitioner',
        'odoo10-addon-medical_practitioner_us',
        'odoo10-addon-medical_procedure',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)
