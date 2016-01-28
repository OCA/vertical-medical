[![Build Status](https://travis-ci.org/OCA/vertical-medical.svg?branch=9.0)](https://travis-ci.org/OCA/vertical-medical)
[![Coverage Status](https://coveralls.io/repos/OCA/vertical-medical/badge.png?branch=9.0)](https://coveralls.io/r/OCA/vertical-medical?branch=9.0)

What is Odoo Medical
---

**Odoo Medical** is a multi-user, highly scalable, centralized Electronic Medical
Record (EMR) and Hospital Information System for odoo.

**Odoo Medical** provides a free universal Health and Hospital Information System,
so doctors and institutions all over the world, specially in developing
countries will benefit from a centralized, high quality, secure and scalable
system.

Odoo Medical at a glance:
---

- Strong focus in family medicine and Primary Health Care

- Major interest in Socio-economics (housing conditions, substance abuse,
education...)

- Diseases and Medical procedures standards (like ICD-10 / ICD-10-PCS ...)

- Patient Genetic and Hereditary risks : Over 4200 genes related to
diseases (NCBI / Genecards)

- Epidemiological and other statistical reports

- 100% paperless patient examination and history taking

- Patient Administration
(creation, evaluations / consultations, history ... )

- Doctor Administration

- Lab Administration

- Medicine / Drugs information (vadem�cum)

- Medical stock and supply chain management

- Hospital Financial Administration

- Designed with industry standards in mind

- Open Source : Licensed under AGPL


Contributing
---

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

Types of Contributions
---

*Report Bugs*

Report bugs at https://github.com/oca/vertical-medical/issues.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

*Fix Bugs*

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

*Implement Features*

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

*Write Documentation*

Try to comment your code using PEP guidelines, and don�t repeat yourself.
TODO: Link the oca standars here.

*Submit Feedback*

The best way to send feedback is to file an issue at https://github.com/oca/vertical-medical/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Hacking Odoo Medical
---

1. Clone this repository:

    ```bash
    $ git clone git@github.com:oca/vertical-medical.git
    $ cd medical && checkout 9.0
    ```

2. Create your own branch locally.

    ```bash
    $ git checkout -b 9.0-your_new_feature_theme
    ```

3. Push your first change branch to know you start to work on.

    ```bash
    $ git push -u origin 9.0-your_new_feature_theme
    ```

4. Prepare your enviroment to work with this repository and the mandatory ones to have all the enviroment ready.

    ```bash
    $ git clone https://github.com/odoo/odoo.git
    $ git clone https://github.com/oca/vertical-medical.git
    $ cd odoo && checkout 9.0
    $ cd vertical-medical && checkout 9.0
    ```

5. Create a postgres user (only for this work to avoid problems not related to this enviroment).

    ```bash
    $ sudo su postgres
    $ createuser medicaluser -P
    #put your password just (1) for example.
    $ createdb medical -U medicaluser -O medicaluser -T remplate0 -E UTF8
    ```

6. Run the development enviroment.

    ```bash
    $ cd path/to/odoo/odoo
    $ ./openerp-server --addons-path=addons/,../medical -r \
    medicaluser -w 1 --db-filter=medical \
    -i medical -d medical
    ```

7. Do your code, and update it passing -u module -d medical (replacing this paramenter above).

8. Before be sure all is ok, we can delete and create db again with -i
   paramenter to ensure all install correctly.

    ```bash
    $ sudo su postgres
    $ dropbd medical
    $ createdb medical -U medicaluser -O medicaluser -T remplate0 -E UTF8
    $ ./openerp-server --addons-path=addons/,../medical -r \
    medicaluser -w 1 --db-filter=medical \
    -i medical -d medical
    ```

9. If all is ok installing, please test your enviroment running your code with �test-enabled�.

    ```bash
    $ ./openerp-server --addons-path=addons/,../medical -r \
    medicaluser -w 1 --db-filter=medical \
    -i medical -d medical --test-enable
    ```

**Note:**

    This will take a time, just do it before commit your change and make push.

10. Add your changes to have them versioned.

    ```bash
    $ git add .
    ```

11. Commit your changes.

    ```bash
    $ git commit -m "[TAG] module: what you did"
    ```

12. Push your first change branch to know you start to work on.

    ```bash
    $ git push -u origin 9.0-your_new_feature_theme
    ```


[//]: # (addons)
Available addons
----------------
addon | version | summary
--- | --- | ---
[medical](medical/) | 9.0.2.0.0 | Odoo Medical
[medical_base_history](medical_base_history/) | 9.0.2.0.0 | Assists in logging history of abstract records
[medical_physician](medical_physician/) | 9.0.2.0.0 | Adds physician concept
[medical_appointment](medical_appointment/) | 9.0.2.0.0 | Schedule physician appointments
[medical_pathology](medical_pathology/) | 9.0.2.0.0 | Adds a base concept of diseases & categorization
[medical_patient_disease](medical_patient_disease/) | 9.0.2.0.0 | Applies the disease pathologies at the patient level
[medical_patient_disease_allergy](medical_patient_disease_allergy/) | 9.0.2.0.0 | Isolates the allergy concept from diseases
[medical_medicament](medical_medicament/) | 9.0.1.0.0 | Add concept of drugs and medicaments
[medical_medication](medical_medication/) | 9.0.2.0.0 | Adds medicine templates and applies medicament concept to patient
[medical_medication_us](medical_medication_us/) | 9.0.1.1.0 | US Locale for Medications



Unported addons
---------------
addon | version | summary
--- | --- | ---
[medical_insurance](medical_insurance/) | 9.0.1.1.0 | Medical Insurance
[medical_insurance_us](medical_insurance_us/) | 9.0.1.1.0 | US Locale for Insurance concept
[medical_his](medical_his/) | 9.0.1.1.0 | Medical Hospital
[medical_family](medical_family/) | 9.0.1.1.0 | Medical Family
[medical_medicament_attributes](medical_medicament_attributes/) | 9.0.1.1.0 | Adds physical attributes to medicaments
[medical_patient_ethnicity](medical_patient_ethnicity/) | 9.0.1.1.0 | Adds ethnicity concept to patients
[medical_patient_occupation](medical_patient_occupation/) | 9.0.1.1.0 | Adds occupation concept to patients
[medical_pharmacy](medical_pharmacy/) | 9.0.1.1.0 | Isolates pharmacy concept from partners
[medical_pharmacy_us](medical_pharmacy_us/) | 9.0.1.1.0 | Add US Locale to pharmacy concept
[medical_prescription](medical_prescription/) | 9.0.1.1.0 | Add concept of prescription orders applied to medications
[medical_prescription_sale](medical_prescription_sale/) | 9.0.1.0.0 | Provide sale workflow for prescription orders
[medical_prescription_state](medical_prescription_state/) | 9.0.2.0.0 | Add Kanban states to prescription orders
[medical_prescription_state_verify](medical_prescription_state_verify) | 9.0.1.0.0 | Add concept of verified prescription states & provide a hook for actions
[medical_prescription_thread](medical_prescription_thread/) | 9.0.1.1.0 | Add mail.thread capabilities to prescription orders and lines
[oemedical_emr_data](oemedical_emr_data/) | 1.0 (unported) | OeMedical EMR: Module Data
[oemedical_genetics](oemedical_genetics/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_gynecology_and_obstetrics](oemedical_gynecology_and_obstetrics/) | 1.0.1 (unported) | OeMedical : gynecology and obstetrics
[oemedical_icu](oemedical_icu/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_invoice](oemedical_invoice/) | 0.1 (unported) | Medical Invoice
[oemedical_lab](oemedical_lab/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_lifestyle](oemedical_lifestyle/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_pediatrics](oemedical_pediatrics/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_socioeconomics](oemedical_socioeconomics/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_surgery](oemedical_surgery/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[web_doc_oemedical](web_doc_oemedical/) | 0.1 (unported) | OeMedical CMS

[//]: # (end addons)
