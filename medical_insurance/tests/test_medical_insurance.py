# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalInsurance(TransactionCase):

    def setUp(self):
        super(TestMedicalInsurance, self).setUp()

        # Models
        self.model_patient = self.env['medical.patient']
        self.model_insurance_company = self.env['medical.insurance.company']
        self.model_product = self.env['product.product']
        self.model_insurance_template = self.env['medical.insurance.template']
        self.model_insurance_plan = self.env['medical.insurance.plan']

        # Patient
        self.patient = self._create_patient()

        # Insurance Company
        self.insurance_company = self._create_insurance_company()

        # Product
        self.product = self._create_product()

        # Insurance Template
        self.insurance_template = \
            self._create_insurance_template(self.product,
                                            self.insurance_company)

        # Insurance Plan
        self.insurance_plan = \
            self._create_insurance_plan(self.patient,  self.insurance_template)

    def _create_patient(self):
        """ Create a patient."""
        return self.model_patient.create({
            'name': 'demo patient',
            'identification_code': 'PA0000000789',
            'gender': 'female',
        })

    def _create_insurance_company(self):
        """ Create an insurance company."""
        return self.model_insurance_company.create({
            'name': 'insurance',
        })

    def _create_product(self):
        """ Create a product."""
        return self.model_product.create({
            'name': 'product',
        })

    def _create_insurance_template(self, product, insurance_company):
        """ Create an insurance template."""
        return self.model_insurance_template.create({
            'code': '00001',
            'description': 'template',
            'product_id': product.id,
            'insurance_company_id': insurance_company.id,
        })

    def _create_insurance_plan(self, patient, plan_template):
        """ Create an insurance plan."""
        return self.model_insurance_plan.create({
            'patient_id': patient.id,
            'insurance_template_id': plan_template.id,
        })

    def test_patient_has_insurance(self):
        """ Check that a user has the insurance plan. """

        self.assertEquals(self.patient.insurance_plan_ids, self.insurance_plan,
                          "The patient must have this insurance plan.")
        self.insurance_plan.active = False
        self.assertEquals(self.patient.insurance_plan_ids[0].active, False,
                          "The insurance plan is no longer active.")

    def test_insurance_provider_has_template(self):
<<<<<<< HEAD
        """ Check that a user has the insurance plan. """
=======
        """ Check that a the insurance provider has an insurance template. """
>>>>>>> 2301f0e8d12ba3ab6c0f3878355f7f5ae3db46a4

        self.assertEquals(self.insurance_company.insurance_template_ids[0],
                          self.insurance_template,
                          "The insurance provider must have this template.")

    def test_patient_has_modified_insurance(self):
<<<<<<< HEAD
        """ Check that a user has the insurance plan. """
=======
        """ Check that when an insurance plan is modified the insurance plan
        of the patient is modified as well. """
>>>>>>> 2301f0e8d12ba3ab6c0f3878355f7f5ae3db46a4

        self.insurance_plan.number = '1234'
        self.assertEquals(self.patient.insurance_plan_ids.number, '1234',
                          "The number of the insurance plan must be 1234.")
