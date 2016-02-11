# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp import fields


class TestPrescriptionSaleOrder(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestPrescriptionSaleOrder, self).setUp(*args, **kwargs)
        self.order_vals = {}
        self.patient_vals = {
            'name': 'TestMedicalPatient',
        }
        self.pharmacy_vals = {
            'name': 'TestMedicalPharmacy',
        }
        vals = {
            'name': 'nothing',
        }
        speciality_id = self.env['medical.specialty'].create(vals)
        self.physician_vals = {
            'name': 'physician',
            'specialty_id': speciality_id.id,
        }
        self.rx_vals = {}
        self.medicament_vals = {
            'name': 'simvastatin',
            'drug_form_id': self.env.ref('medical_medicament.AEM').id,
        }
        self.rx_line_vals = {
            'date_start_treatment': fields.Datetime.now(),
        }

    def _new_sale(self):
        self.patient_id = self.env['medical.patient'].create(
            self.patient_vals
        )
        self.pharmacy_id = self.env['medical.pharmacy'].create(
            self.pharmacy_vals
        )
        self.physician_id = self.env['medical.physician'].create(
            self.physician_vals
        )
        self.medicament_id = self.env['medical.medicament'].create(
            self.medicament_vals
        )
        self.order_vals.update({
            'partner_id': self.patient_id.partner_id.id,
            'pharmacy_id': self.pharmacy_id.id,
        })
        self.rx_line_vals.update({
            'medicament_id': self.medicament_id.id,
            'physician_id': self.physician_id.id,
            'patient_id': self.patient_id.id,
        })
        self.rx_vals.update({
            'patient_id': self.patient_id.id,
            'physician_id': self.physician_id.id,
            'prescription_order_line_ids': [(0, 0, self.rx_line_vals)],
        })
        self.rx_id = self.env['medical.prescription.order'].create(
            self.rx_vals
        )
        self.rx_line_id = self.rx_id.prescription_order_line_ids[0]
        self.order_vals.update({
            'order_line': [(0, 0, {
                'product_id': self.medicament_id.product_id.id,
                'name': self.medicament_id.name,
                'patient_id': self.patient_id.id,
                'price_unit': 1,
                'product_uom': 1,
                'product_uom_qty': 1,
                'prescription_order_line_id': self.rx_line_id.id,
            })],
            'partner_id': self.patient_id.partner_id.id,
            'pharmacy_id': self.pharmacy_id.id,
        })
        order_id = self.env['sale.order'].create(self.order_vals)
        return order_id

    def test_sale_order_compute_patient_ids_gets_correct(self):
        order_id = self._new_sale()
        self.assertIn(
            self.patient_id, order_id.patient_ids,
            'Did not compute correct patient. Expected %s Got %s' % (
                self.patient_id, order_id.patient_ids
            )
        )
        self.assertEqual(
            1, len(order_id.patient_ids),
        )

    def test_sale_order_compute_prescription_ids_gets_correct(self):
        order_id = self._new_sale()
        self.assertIn(
            self.rx_id, order_id.prescription_order_ids,
            'Did not compute correct rx. Expected %s Got %s' % (
                self.rx_id, order_id.prescription_order_ids
            )
        )
        self.assertEqual(
            1, len(order_id.prescription_order_ids),
        )

    def test_prescription_line_compute_orders_gets_correct(self):
        order_id = self._new_sale()
        self.assertIn(
            order_id, self.rx_line_id.sale_order_ids,
            'Did not compute correct order. Expected %s Got %s' % (
                order_id, self.rx_line_id.sale_order_ids,
            )
        )
        self.assertEqual(
            1, len(self.rx_line_id.sale_order_ids),
        )

    def test_prescription_line_default_name(self):
        self._new_sale()
        self.assertTrue(
            self.rx_line_id.name,
            'Expected Rx Line name to be set',
        )

    def test_medicament_is_prescription_direct_descendant(self):
        prescription_categ_id = self.env.ref(
            'medical_prescription_sale.product_category_rx'
        )
        self.medicament_vals['categ_id'] = prescription_categ_id.id
        medicament_id = self.env['medical.medicament'].create(
            self.medicament_vals
        )
        self.assertTrue(
            medicament_id.is_prescription,
            'Is prescription is not set to True when in Rx categ_id'
        )

    def test_medicament_is_prescription_indirect_descendant(self):
        prescription_categ_id = self.env.ref(
            'medical_prescription_sale.product_category_rx'
        )
        prescription_categ_id = self.env['product.category'].create({
            'name': 'Category',
            'parent_id': prescription_categ_id.id,
        })
        self.medicament_vals['categ_id'] = prescription_categ_id.id
        medicament_id = self.env['medical.medicament'].create(
            self.medicament_vals
        )
        self.assertTrue(
            medicament_id.is_prescription,
            'Is prescription is not set to True when in Rx categ descendant'
        )
