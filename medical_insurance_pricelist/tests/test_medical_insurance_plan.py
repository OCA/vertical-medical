# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalInsurancePlan(TransactionCase):

    def setUp(self):
        super(TestMedicalInsurancePlan, self).setUp()
        self.patient_vals = {
            'name': 'Test Patient',
        }
        self.product_vals = {
            'name': 'Test Product',
            'type': 'service',
        }
        self.pricelist_vals = {
            'name': 'Test Pricelist',
        }
        self.template_vals = {
            'plan_number': '69105',
        }
        self.vals = {
            'number': '42',
        }

    def _new_record(self):
        self.patient_id = self.env['medical.patient'].create(
            self.patient_vals,
        )
        self.product_id = self.env['product.product'].create(
            self.product_vals,
        )
        self.pricelist_id = self.env['product.pricelist'].create(
            self.pricelist_vals,
        )
        self.template_vals.update({
            'product_id': self.product_id.id,
            'pricelist_id': self.pricelist_id.id,
        })
        self.template_id = self.env['medical.insurance.template'].create(
            self.template_vals,
        )
        self.vals.update({
            'patient_id': self.patient_id.id,
            'insurance_template_id': self.template_id.id,
        })
        return self.env['medical.insurance.plan'].create(
            self.vals,
        )

    def test_pricelist_saved_on_patient_on_create(self):
        rec_id = self._new_record()
        self.assertEqual(
            rec_id.pricelist_id, self.patient_id.pricelist_id,
            'Pricelist did not save on patient. Expected %s got %s' % (
                rec_id.pricelist_id, self.patient_id.pricelist_id
            )
        )

    def test_pricelist_saved_on_patient_on_write(self):
        rec_id = self._new_record()
        new_patient_id = self.env['medical.patient'].create({
            'name': 'New Patient'
        })
        rec_id.write({'patient_id': new_patient_id.id})
        self.assertEqual(
            rec_id.pricelist_id, new_patient_id.pricelist_id,
            'Pricelist did not save on patient. Expected %s got %s' % (
                rec_id.pricelist_id, new_patient_id.pricelist_id
            )
        )

    def test_current_plan_active(self):
        rec_id = self._new_record()
        self.assertEqual(
            True, rec_id.active,
            'Did not flag plan as active. Expected %s got %s' % (
                True, rec_id.active
            )
        )

    def test_old_plan_inactive_on_create(self):
        old_rec_id = self._new_record()
        self.env['medical.insurance.plan'].create({
            'number': '43',
            'patient_id': self.patient_id.id,
            'insurance_template_id': self.template_id.id,
        })
        self.assertEqual(
            False, old_rec_id.active,
            'Did not invalidate previous plan. Expected %s got %s' % (
                False, old_rec_id.active
            )
        )

    def test_old_plan_inactive_on_write(self):
        old_rec_id = self._new_record()
        new_rec_id = self.env['medical.insurance.plan'].create({
            'number': '43',
            'insurance_template_id': self.template_id.id,
        })
        new_rec_id.write({'patient_id': self.patient_id.id})
        self.assertEqual(
            False, old_rec_id.active,
            'Did not invalidate previous plan. Expected %s got %s' % (
                False, old_rec_id.active
            )
        )
