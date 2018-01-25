# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, models, _
from openerp.exceptions import ValidationError


class MedicalAbstractNpi(models.AbstractModel):
    """ Inherit this to provide Npi validation to any model.

    Public attributes and methods will be prefixed with Npi in order
    to avoid name collisions with models that will inherit from this class.
    """

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
        if not num:
            return False
        num = '80840%s' % num
        return self._luhn_is_valid(num)

    @api.multi
    def _npi_constrains_helper(self, col_name, country_col='country_id'):
        """ Provide a mixer for Npi validation via constrains
        Params:
            col_name: :type:``str`` Name of db column to constrain
            country_col: :type:``str`` Name of db country column to verify
        Raises:
            :type:``ValidationError``: If constrain is a failure
            :type:AttributeError``: If country db col is not valid or is null
        """

        for rec_id in self:
            if getattr(rec_id, country_col).code == 'US':
                if self._npi_is_valid(rec_id[col_name]):
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
