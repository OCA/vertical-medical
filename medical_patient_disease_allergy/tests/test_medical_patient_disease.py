# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from .common import CommonTestBase


class TestMedicalPatientDisease(CommonTestBase):

    def test_compute_is_allergy(self):
        """ It should be identified as an allergy """
        self.assertTrue(
            self.disease_id.is_allergy,
        )
