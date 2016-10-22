# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api
from odoo.exceptions import ValidationError
import re


class MedicalAbstractDea(models.AbstractModel):
    """ Inherit this to provide DEA validation to any model.

    Public attributes and methods will be prefixed with dea in order
    to avoid name collisions with models that will inherit from this class.
    """

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

    @api.multi
    def _dea_constrains_helper(self, col_name, country_col='country_id'):
        """ Provide a helper for dea validation via constrain
        Params:
            col_name: ``str`` Name of db column to constrain
            country_col: ``str`` Name of db country column to verify
        Raises:
            ValidationError: If constrain is a failure
            AttributeError: If country column is not valid or is null in db
        """

        for rec_id in self:
            if getattr(rec_id, country_col).code == 'US':
                if not self._dea_is_valid(
                    getattr(rec_id, col_name, 0)
                ):
                    col_obj = self.env['ir.model.fields'].search([
                        ('name', '=', col_name),
                        ('model', '=', rec_id._name),
                    ],
                        limit=1,
                    )
                    raise ValidationError(
                        'Invalid %s was supplied.' % col_obj.display_name
                    )
