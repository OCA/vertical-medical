# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime, timedelta

from openerp.tests.common import TransactionCase
from openerp import fields


class TestMedicalPrescriptionOrder(TransactionCase):

    module = 'medical_prescription_sale_stock'

    def setUp(self, *args, **kwargs):
        super(TestMedicalPrescriptionOrder, self).setUp(*args, **kwargs)
        date_now = datetime.now()
        delta = timedelta(days=1)
        self.date_today = fields.Datetime.to_string(date_now)
        self.date_yesterday = fields.Datetime.to_string(date_now - delta)

    # def _clear_resources(self, ):
        self.order_vals = {}
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
            'duration': 30,
            'duration_uom_id': self.env.ref('product.product_uom_day').id,
            'refill_qty_original': 5,
        }
        self.procurement_vals = {
            'date_planned': fields.Datetime.now(),
            'name': 'Test Dispensing',
            'product_qty': 1,
            'product_uom': 1,
        }

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

    def _new_patient(self, ):
        return self.env['medical.patient'].create(self.patient2_vals)

    def _new_rx_order(self, new_resources=True):
        if new_resources:
            prescription_categ_id = self.env.ref(
                'medical_prescription_sale.product_category_rx'
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

    def _new_procurement(self, order_line_id, date=None):
        vals = order_line_id._prepare_order_line_procurement()
        if date is not None:
            vals['date_planned'] = date
        order_line_id.write({
            'procurement_ids': [(
                0, 0, vals
            )],
        })
        return order_line_id.procurement_ids[-1]

    def test_rx_line_compute_can_dispense_refill(self):
        """ It should allow a dispense due to a refill, but not overfill """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            '2016-01-01 00:00:00',
        ).state = 'done'
        self.assertEqual(
            1, self.rx_line_id.can_dispense_qty,
        )
        self.assertTrue(self.rx_line_id.can_dispense)

    def test_rx_line_compute_dispense_remain_no_fill_days(self):
        """ It should start at zero when no procurements """
        self._new_rx_order()
        self.assertEqual(
            0.0, self.rx_line_id.last_dispense_remain_day,
        )

    def test_rx_line_compute_dispense_remain_no_fill_qty(self):
        """ It should start at zero when no procurements """
        self._new_rx_order()
        self.assertEqual(
            0.0, self.rx_line_id.last_dispense_remain_qty,
        )

    def test_rx_line_compute_dispense_remain_no_fill_percent(self):
        """ It should start at zero when no procurements """
        self._new_rx_order()
        self.assertEqual(
            0.0, self.rx_line_id.last_dispense_remain_percent,
        )

    def test_rx_line_compute_dispense_remain_with_fill_days_today(self):
        """ It should have all days remaining in dispense on dispense day """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_today,
        ).state = 'done'
        self.assertEqual(
            5.0, self.rx_line_id.last_dispense_remain_day,
        )

    def test_rx_line_compute_dispense_remain_with_fill_qty_today(self):
        """ It should have full dispense qty remaining on dispense day """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_today,
        ).state = 'done'
        self.assertEqual(
            1.0, self.rx_line_id.last_dispense_remain_qty,
        )

    def test_rx_line_compute_dispense_remain_with_fill_percent_today(self):
        """ It should have 100% of dispense remaining on dispense day """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_today,
        ).state = 'done'
        self.assertEqual(
            100.0, self.rx_line_id.last_dispense_remain_percent,
        )

    def test_rx_line_compute_dispense_remain_with_fill_days_yestday(self):
        """ It should have -1 day if dispensed yesterday """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_yesterday,
        ).state = 'done'
        self.assertEqual(
            4.0, self.rx_line_id.last_dispense_remain_day,
        )

    def test_rx_line_compute_dispense_remain_with_fill_qty_yestday(self):
        """ It should have -.2 qty remaining if dispensed yesterday """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_yesterday,
        ).state = 'done'
        self.assertEqual(
            0.8, self.rx_line_id.last_dispense_remain_qty,
        )

    def test_rx_line_compute_dispense_remain_with_fill_percent_yestday(self):
        """ It should have -20% remaining if dispensed yesterday """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_yesterday,
        ).state = 'done'
        self.assertEqual(
            80.0, self.rx_line_id.last_dispense_remain_percent,
        )

    def test_compute_qty_remain_total_allowed(self):
        """ It should start with refill count + 1 """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_yesterday,
        ).state = 'done'
        self.assertEqual(
            6.0, self.rx_line_id.total_allowed_qty,
        )

    def test_compute_qty_remain_total_qty_remain(self):
        """ It should decrement remaining qty if dispensed and +1 """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_yesterday,
        ).state = 'done'
        self.assertEqual(
            5.0, self.rx_line_id.total_qty_remain,
        )

    def test_compute_qty_remain_refill_qty_remain(self):
        """ It should decrement remaining qty and represent refills """
        self._new_procurement(
            self._new_rx_order().order_line[0],
            self.date_yesterday,
        ).state = 'done'
        self.assertEqual(
            4.0, self.rx_line_id.refill_qty_remain,
        )
