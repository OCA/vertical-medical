# -*- coding: utf-8 -*-
# Copyright 2015 ACSONE SA/NV
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp.tests.common import TransactionCase


class TestAbstractMedicalMedication(TransactionCase):

    def setUp(self):
        super(TestAbstractMedicalMedication, self).setUp()
        self.medication_6 = self.env.ref(
            'medical_medication.medical_patient_medication_medication_6'
        )
        self.medication_template_6 = self.env.ref(
            'medical_medication.medical_medication_template_template_6'
        )

    def test_onchange_template_id(self):
        """ Test template vals and medication vals are set the same """
        comparison_keys = [
            'medicament_id',
            'quantity',
            'dose_uom_id',
            'frequency',
            'frequency_uom_id',
            'frequency_prn',
            'duration',
            'duration_uom_id',
            'medication_dosage_id',
            'suggested_administration_hours',
        ]
        self.medication_6.onchange_template_id()
        for k in comparison_keys:
            t_value = getattr(self.medication_6, k)
            m_value = getattr(self.medication_template_6, k)
            self.assertEqual(
                t_value, m_value,
                '%s not the same.\rMedication: %s\rTemplate: %s' % (
                    k, t_value, m_value
                )
            )
