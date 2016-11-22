# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class MedicalAbstractNpi(models.AbstractModel):
    """ It provides NPI Validation method """

    _name = 'medical.abstract.npi'
    _description = 'Medical Abstract NPI'
    _inherit = 'medical.abstract.luhn'

    @api.model
    def _npi_is_valid(self, num):
        """ Determine whether num is valid. Meant to be used in constrains
        Params:
            num: :type:``str`` or :type:``int`` Number to validate
                using Npi's Alg.
        Returns:
            :type:``bool``
        """
        num = '80840%s' % num
        return self._luhn_is_valid(num)
