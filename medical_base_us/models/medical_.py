# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class MedicalLuhnAbstract(models.AbstractModel):
    """ Inherit this to provide Luhn validation to any model.

    Public attributes and methods will be prefixed with luhn in order
    to avoid name collisions with models that will inherit from this class.
    """

    _name = 'medical.luhn.abstract'

    @api.model
    def _luhn_is_valid(self, num):
        """ Determine whether num is valid. Meant to be used in constrains
        Params:
            num: ``str`` or ``int`` Number to validate using Luhn's Alg.
        Returns:
            bool
        """
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(num)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        checksum += sum(
            sum(digits_of(d*2)) for d in even_digits
        )
        return (checksum % 10) == 0
