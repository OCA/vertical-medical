# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import _, api, models
from odoo.exceptions import ValidationError


class MedicalAbstractLuhn(models.AbstractModel):
    """ Inherit this to provide Luhn validation to any model.

    Public attributes and methods will be prefixed with luhn in order
    to avoid name collisions with models that will inherit from this class.
    """

    _name = 'medical.abstract.luhn'
    _description = 'Medical Abstract Luhn'

    @api.model
    def _luhn_is_valid(self, num):
        """ Determine whether num is valid. Meant to be used in constrains
        Params:
            num (str or int): Number to validate using Luhn's Alg.
        Returns:
            bool
        """

        if not num:
            return False

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

    @api.multi
    def _luhn_constrains_helper(self, col_name, country_col='country_id'):
        """ Provide a mixer for Luhn validation via constrains
        Params:
            col_name: :type:``str`` Name of db column to constrain
            country_col: :type:``str`` Name of db country column to verify
        Raises:
            :type:``ValidationError``: If constrain is a failure
            :type:AttributeError``: If country db col is not valid or is null
        """

        for rec_id in self:
            if getattr(rec_id, country_col).code == 'US':
                if self._luhn_is_valid(rec_id[col_name]):
                    return
                col_obj = self.env['ir.model.fields'].search([
                    ('name', '=', col_name),
                    ('model', '=', rec_id._name),
                ],
                    limit=1,
                )
                raise ValidationError(
                    _('Invalid %s was supplied.') % col_obj.display_name,
                )
