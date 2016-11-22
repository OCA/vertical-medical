# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class MedicalAbstractLuhn(models.AbstractModel):
    """ It provides Luhn verification method """

    _name = 'medical.abstract.luhn'
    _description = 'Medical Abstract Luhn'

    @api.model
    def _luhn_is_valid(self, num):
        """ Determine whether num is valid. Meant to be used in constrains
        Params:
            num: :type:``str`` or :type:``int`` Number to validate
                using Luhn's Alg.
        Returns:
            :type:``bool``
        """

        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(num)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        checksum += sum(
            sum(digits_of(d * 2)) for d in even_digits
        )
        return (checksum % 10) == 0
