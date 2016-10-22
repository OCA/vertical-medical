# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):

    def test_medical_patient_ids_none(self):
        partner = self.env['res.partner'].create({'name': 'Test Partner'})
        self.assertEqual(len(partner.medical_patient_ids), 0)

    def test_medical_patient_ids_self(self):
        patient = self.env['medical.patient'].create({'name': 'Test Patient'})
        partner = patient.partner_id
        self.assertEqual(partner.medical_patient_ids, patient)

    def test_medical_patient_ids_self_and_children(self):
        patient = self.env['medical.patient'].create({'name': 'Test Patient'})
        child_patient = self.env['medical.patient'].create({
            'name': 'Child Patient'
        })
        grandchild_patient = self.env['medical.patient'].create({
            'name': 'Grandchild Patient'
        })
        partner = patient.partner_id
        child_patient.parent_id = partner
        grandchild_patient.parent_id = child_patient.partner_id

        self.assertEqual(
            partner.medical_patient_ids,
            patient + child_patient + grandchild_patient,
        )
