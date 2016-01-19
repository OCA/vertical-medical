# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields


class MedicalHistoryExample(models.Model):
    '''
    This is an example of how to use the MedicalHistoryAbstract

    @TODO: Example of custom logging method

    Examples:
        _audit_on: This is being declared in order to override the default
            change logging columns (`create`, `write`, `delete` - but could be
            more/less by other inherits) Example only audits on `create`.
    '''
    _inherit = 'medical.history.abstract'
    _name = 'medical.history.example'
    _description = 'Example of a model with audit logging'
    _audit_on = ['create', ]
    example_col = fields.Char()
