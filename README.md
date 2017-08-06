[![Runbot Status](https://runbot.odoo-community.org/runbot/badge/flat/159/9.0.svg)](https://runbot.odoo-community.org/runbot/repo/github-com-oca-vertical-medical-159)
[![Build Status](https://travis-ci.org/OCA/vertical-medical.svg?branch=9.0)](https://travis-ci.org/OCA/vertical-medical)
[![codecov](https://codecov.io/gh/OCA/vertical-medical/branch/9.0/graph/badge.svg)](https://codecov.io/gh/OCA/vertical-medical)

# Vertical Medical

Vertical Medical provides a Free and Open Source solution for storing and processing medical
records in Odoo.

Many of the workflows were built in alignment with existing Odoo processes to allow for
seamless operation with other record types.

This project is moving towards organization and data models inspired by [HL7 FHIR v3](
https://www.hl7.org/fhir/overview.html).

[//]: # (addons)

Available addons
----------------
addon | version | summary
--- | --- | ---
[mail_thread_medical_prescription](mail_thread_medical_prescription/) | 9.0.1.0.0 | Adds message threads to rx orders and rx order lines.
[medical](medical/) | 9.0.1.0.0 | Extends Odoo with medical patients and centers.
[medical_base_us](medical_base_us/) | 9.0.1.0.0 | Provides some helper mixins for US locale.
[medical_lab](medical_lab/) | 9.0.1.0.0 | Medical Lab
[medical_manufacturer](medical_manufacturer/) | 9.0.1.0.0 | Extension of medical with concept of medical manufacturers.
[medical_medicament](medical_medicament/) | 9.0.1.0.0 | Introduce Medicament notion into the medical product.
[medical_medicament_component](medical_medicament_component/) | 9.0.1.0.0 | Medical Medicament Components
[medical_medicament_us](medical_medicament_us/) | 9.0.1.0.0 | Extension of medical_medicament that provides US locale.
[medical_medication](medical_medication/) | 9.0.1.0.1 | Introduce medication notion into the medical addons.
[medical_pathology](medical_pathology/) | 9.0.1.0.1 | Extends Odoo Medical with pathologies (diseases).
[medical_patient_disease](medical_patient_disease/) | 9.0.1.0.0 | Extend medical patients with the concept of diseases.
[medical_patient_disease_allergy](medical_patient_disease_allergy/) | 9.0.1.0.0 | Isolates allergies from diseases.
[medical_patient_dob](medical_patient_dob/) | 9.0.1.0.0 | Show date of birth when searching patients.
[medical_pharmacy](medical_pharmacy/) | 9.0.1.0.0 | Adds pharmacy namespace on partners.
[medical_pharmacy_us](medical_pharmacy_us/) | 9.0.1.0.0 | Medical Pharmacy - US Locale
[medical_physician](medical_physician/) | 9.0.1.0.0 | Adds physicians to Odoo Medical.
[medical_prescription](medical_prescription/) | 9.0.2.0.0 | Introduces prescription orders and prescription order lines.
[medical_prescription_state](medical_prescription_state/) | 9.0.1.0.0 | Medical Prescription Order States
[medical_prescription_us](medical_prescription_us/) | 9.0.1.0.0 | Extension of medical_prescription that provides US Locale
[sale_crm_medical_prescription](sale_crm_medical_prescription/) | 9.0.1.0.0 | Create opportunities from prescriptions.
[sale_medical_prescription](sale_medical_prescription/) | 9.0.2.0.0 | Create sale orders from prescriptions.
[sale_stock_medical_prescription](sale_stock_medical_prescription/) | 9.0.1.0.0 | Provides dispense logic for prescriptions.


Unported addons
---------------
addon | version | summary
--- | --- | ---
[medical_insurance](medical_insurance/) | 8.0.1.1.0 (unported) | Medical Insurance
[medical_insurance_us](medical_insurance_us/) | 8.0.1.1.0 (unported) | Medical Insurance - US
[medical_medicament_attributes](medical_medicament_attributes/) | 8.0.1.0.0 (unported) | Medical Medicament Physical Attributes

[//]: # (end addons)

Translation Status
------------------
[![Transifex Status](https://www.transifex.com/projects/p/OCA-vertical-medical-9.0/chart/image_png)](https://www.transifex.com/projects/p/OCA-vertical-medical-9.0)

----

OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.
