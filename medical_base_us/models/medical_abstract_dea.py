# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api
import re


class MedicalAbstractDea(models.AbstractModel):
    """ It provides DEA Number verification method """

    _name = 'medical.abstract.dea'

    @api.model
    def _dea_is_valid(self, dea_num):
        """ Determine whether num is valid. Meant to be used in constrains

        A valid DEA number consists of 2 letters, 6 digits, and 1 check digit.
        * The first letter is a code identifying the type of registrant.
        * The second letter is the first letter of the registrant's last name.

        Verification steps:
        1. Add the first, third, and fifth digits;
        2. Add the second, fourth, and sixth digits;
        3. Multiply the result of Step 2 by two;
        4. Add the result of Step 1 to the result of Step 3;
        5. The last digit of this sum must be the same as the last digit;

        Example: DEA number AP5836727
        1. 5 + 3 + 7 = 15
        2. 8 + 6 + 2 = 16
        3. 16 * 2 = 32
        4. 15 + 32 = 47

        Params:
            dea_num: ``str`` DEA ID to validate
        Returns:
            bool
        """

        if len(dea_num) != 9:
            return False

        def digits_of(n):
            return [int(d) for d in str(n)]

        regex = re.compile(
            r'^(?P<registrant_type>\w)(?P<registrant_identifier>\w)'
            r'(?P<math_digits>\d{6})(?P<control_digit>\d)$'
        )
        for match in regex.finditer(dea_num):
            match = match.groupdict()
            evens = sum(digits_of(match['math_digits'][0:][::2]))
            odds = sum(digits_of(match['math_digits'][1:][::2]))
            res_str = str((odds * 2) + evens)
            return int(res_str[-1]) == int(match['control_digit'])

        return False
