# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical, an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical is free software:
#     you can redistribute it and/or
#     modify it under the terms of the GNU Affero General Public License
#     as published by the Free Software Foundation, either version 3 of
#     the License, or (at your option) any later version.
#
#     medical is distributed in the hope that it will
#     be useful but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the
#     GNU Affero General Public License
#     along with medical.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.tests.common import TransactionCase
from openerp import fields


class TestMedicalMedication(TransactionCase):

    _module_ns = 'medical_medication'

    def setUp(self):
        super(TestMedicalMedication, self).setUp()
        self.medical_medication = self.env['medical.patient.medication']
        self.medical_medication_template =\
            self.env['medical.medication.template']
        self.medical_medicament = self.env['medical.medicament']
        self.medical_physician = self.env['medical.physician']
        self.medical_patient = self.env['medical.patient']
        self.medical_speciality = self.env['medical.specialty']

    def test_onchange_template_id(self):
        vals = {
            'name': 'headache',
            'drug_form_id': self.env.ref('medical_medicament.AEM').id,
        }
        medicament_id = self.medical_medicament.create(vals)
        temp_vals = {
            'medicament_id': medicament_id.id,
            'quantity': 1,
            'dose_unit_id': self.env.ref(
                '%s.product_uom_ml' % self._module_ns).id,
            'frequency': 1,
            'frequency_unit': 'wr',
            'frequency_prn': True,
            'duration': 1,
            'duration_period': 'indefinite',
            'medication_dosage_id': self.env.ref(
                '%s.229797004' % self._module_ns).id,
            'suggested_administration_hours': 8,
        }
        medication_template_id =\
            self.medical_medication_template.create(temp_vals)
        vals = {
            'name': 'patient',
        }
        patient_id = self.medical_patient.create(vals)
        vals = {
            'name': 'generic',
        }
        speciality_id = self.medical_speciality.create(vals)
        vals = {
            'name': 'physician',
            'specialty': speciality_id.id,
        }
        physician_id = self.medical_physician.create(vals)
        vals = {
            'medicament_id': medicament_id.id,
            'medication_template_id': medication_template_id.id,
            'date_start_treatment': fields.Datetime.now(),
            'physician_id': physician_id.id,
            'patient_id': patient_id.id,
        }
        medication_id = self.medical_medication.create(vals)
        medication_id.onchange_template_id()
        for k in temp_vals.keys():
            t_value = getattr(medication_template_id, k)
            m_value = getattr(medication_id, k)
            self.assertEqual(t_value, m_value, '%s Should be the same' % k)
