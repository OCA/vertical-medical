# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import Warning


class TestMedicalPatientSpecies(TransactionCase):

    def setUp(self):
        super(TestMedicalPatientSpecies, self).setUp()
        self.human = self.env.ref('medical_patient_species.human')
        self.dog = self.env.ref('medical_patient_species.dog')

    def test_unlink_human(self):
        ''' Test raises Warning if unlinking human '''
        with self.assertRaises(Warning):
            self.human.unlink()
