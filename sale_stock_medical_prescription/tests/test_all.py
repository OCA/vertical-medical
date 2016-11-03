# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from psycopg2 import IntegrityError
from odoo.tests.common import TransactionCase
from odoo import fields
from odoo.exceptions import ValidationError


class TestAll(TransactionCase):
    """ @TODO: Isolate all of this by model """

    module = 'sale_stock_medical_prescription'

    def setUp(self, *args, **kwargs):
        super(TestAll, self).setUp(*args, **kwargs)
        self.uom_id = self.env.ref('product.product_uom_unit')
        self.order_vals = {}
        self.order_line_vals = {
            'product_uom': self.uom_id.id,
            'product_uom_qty': 1,
        }
        self.patient_vals = {
            'name': 'TestMedicalPatientPrescriptionStock',
        }
        self.patient2_vals = {
            'name': 'TestMedicalPatientPrescriptionStock2',
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
            'is_prescription': False,
        }
        self.rx_line_vals = {
            'date_start_treatment': fields.Datetime.now(),
            'qty': 1,
            'dispense_uom_id': 1,
        }
        self.procurement_vals = {
            'date_planned': fields.Datetime.now(),
            'name': 'Test Dispensing',
            'product_qty': 1,
            'product_uom': self.uom_id.id,
        }
        self.state = 'draft'
        self.prescription_line = True

    def _new_resources(self, clear=True):
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
            'state': self.state,
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
        self.order_line_vals.update({
            'product_id': self.medicament_id.product_id.id,
            'name': self.medicament_id.name,
            'patient_id': self.patient_id.id,
            'price_unit': 1,
            'state': self.state,
        })
        if self.prescription_line:
            self.order_line_vals.update({
                'prescription_order_line_id': self.rx_line_id.id,
            })
        self.order_vals.update({
            'order_line': [(0, 0, self.order_line_vals)],
            'partner_id': self.patient_id.partner_id.id,
            'pharmacy_id': self.pharmacy_id.id,
        })

    def _new_patient(self):
        return self.env['medical.patient'].create(self.patient2_vals)

    def _new_rx_order(self, new_resources=True):
        if new_resources:
            prescription_categ_id = self.env.ref(
                'sale_medical_prescription.product_category_rx'
            )
            self.medicament_vals['categ_id'] = prescription_categ_id.id
            self._new_resources()

        order_id = self.env['sale.order'].create(self.order_vals)
        return order_id

    def _new_order(self, new_resources=True):
        if new_resources:
            self._new_resources()
        order_id = self.env['sale.order'].create(self.order_vals)
        return order_id

    def _new_procurement(self, order_line_id):
        order_line_id.write({
            'procurement_ids': [(
                0, 0, order_line_id._prepare_order_line_procurement()
            )],
        })
        return order_line_id.procurement_ids[-1]

    def test_rx_line_dispense_uom_id_default(self):
        old_rx_line_vals = self.rx_line_vals
        del self.rx_line_vals['dispense_uom_id']
        self._new_rx_order()
        self.rx_line_vals = old_rx_line_vals

        self.assertEqual(
            self.env['product.template']._get_default_uom_id(),
            self.rx_line_id.dispense_uom_id.id,
        )

    def test_rx_line_dispense_uom_id_required(self):
        old_rx_line_vals = self.rx_line_vals
        self.rx_line_vals['dispense_uom_id'] = None

        with self.assertRaises(IntegrityError):
            self._new_rx_order()

        self.rx_line_vals = old_rx_line_vals

    def test_rx_line_compute_dispensings_cancelled(self):
        self._new_procurement(
            self._new_rx_order().order_line[0]
        ).state = 'cancel'
        self.assertEqual(
            1, self.rx_line_id.cancelled_dispense_qty,
        )

    def test_rx_line_compute_dispensings_pending_confirmed(self):
        self._new_procurement(
            self._new_rx_order().order_line[0]
        ).state = 'confirmed'
        self.assertEqual(
            1, self.rx_line_id.pending_dispense_qty,
        )

    def test_rx_line_compute_dispensings_pending_running(self):
        self._new_procurement(
            self._new_rx_order().order_line[0]
        ).state = 'running'
        self.assertEqual(
            1, self.rx_line_id.pending_dispense_qty,
        )

    def test_rx_line_compute_dispensings_done(self):
        self._new_procurement(
            self._new_rx_order().order_line[0]
        ).state = 'done'
        self.assertEqual(
            1, self.rx_line_id.dispensed_qty,
        )

    def test_rx_line_compute_dispensings_except(self):
        self._new_procurement(
            self._new_rx_order().order_line[0]
        ).state = 'exception'
        self.assertEqual(
            1, self.rx_line_id.exception_dispense_qty,
        )

    def test_rx_line_compute_dispensings_unit_conversion(self):
        old_rx_line_vals = self.rx_line_vals
        old_order_line_vals = self.order_line_vals
        self.rx_line_vals['dispense_uom_id'] = self.env.ref(
            'product.product_uom_dozen'
        ).id
        self.order_line_vals['product_uom'] = self.env.ref(
            'product.product_uom_unit'
        ).id
        self.order_line_vals['product_uom_qty'] = 12
        self._new_procurement(
            self._new_rx_order().order_line[0]
        ).state = 'done'
        self.rx_line_vals = old_rx_line_vals
        self.order_line_vals = old_order_line_vals

        self.assertEqual(
            1, self.rx_line_id.active_dispense_qty,
        )

    def test_rx_line_compute_can_dispense_none(self):
        self._new_procurement(
            self._new_rx_order().order_line[0]
        ).state
        self.assertEqual(
            0, self.rx_line_id.can_dispense_qty,
        )
        self.assertFalse(self.rx_line_id.can_dispense)

    def test_rx_line_compute_can_dispense_one(self):
        self._new_rx_order()
        self.assertEqual(
            1, self.rx_line_id.can_dispense_qty,
        )
        self.assertTrue(self.rx_line_id.can_dispense)

    def test_rx_line_compute_can_dispense_active_qty_none(self):
        self._new_rx_order()
        self.assertEqual(
            0, self.rx_line_id.active_dispense_qty,
        )

    def test_rx_line_compute_can_dispense_active_qty_one(self):
        self._new_procurement(
            self._new_rx_order().order_line[0]
        ).state = 'done'
        self.assertEqual(
            1, self.rx_line_id.active_dispense_qty,
        )

    def test_rx_line_compute_can_dispense_draft_no_rx(self):
        """ It should not generate an error """
        self.prescription_line = False
        self._new_rx_order()
        # Assert True because no error
        self.assertTrue(True)

    def test_sale_line_compute_dispense_qty_identical(self):
        order_id = self._new_rx_order()
        self.assertEqual(
            1, order_id.order_line[0].dispense_qty,
        )

    def test_sale_line_check_product(self):
        order_id = self._new_rx_order()
        order_line = order_id.order_line[0]
        product = self.env['product.product'].search([
            ('id', '!=', order_line.product_id.id)
        ], limit=1)
        with self.assertRaises(ValidationError):
            order_line.product_id = product.id

    def test_prepare_order_line_procurement_otc(self):
        """ It should not throw an error and should assign OTC route """
        order_id = self._new_order()
        res = order_id.order_line[0]._prepare_order_line_procurement()
        expect = self.env.ref(
            '%s.route_warehouse0_otc' % self.module
        )
        res = res['route_ids'][0][2]
        self.assertEquals(
            [expect.id], res,
            'Did not correctly assign route. Expect %s, Got %s' % (
                [expect.id], res
            )
        )

    def test_prepare_order_line_procurement_prescription(self):
        """ It should not throw an error and should assign RX route """
        order_id = self._new_rx_order()
        res = order_id.order_line[0]._prepare_order_line_procurement()
        expect = self.env.ref(
            '%s.route_warehouse0_prescription' % self.module
        )
        res = res['route_ids'][0][2]
        self.assertEquals(
            [expect.id], res,
            'Did not correctly assign route. Expect %s, Got %s' % (
                [expect.id], res
            )
        )
