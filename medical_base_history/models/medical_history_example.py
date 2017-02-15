# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MedicalHistoryExample(models.Model):
    """ This is an example of how to use the MedicalHistoryAbstract

    @TODO: Example of custom logging method

    Examples:
        _audit_on: This is being declared in order to override the default
            change logging columns (`create`, `write`, `delete` - but could be
            more/less by other inherits) Example only audits on `create`.
    """

    # Standard private model methods
    _inherit = 'medical.history.abstract'
    _name = 'medical.history.example'
    _description = 'Example of a model with audit logging'

    # By overriding `_audit_on` and only providing `create`, we are removing
    # the default operation of logging on `write`, and `unlink` methods in
    # favor of only logging `create` (defaults - `create`, `write`, `delete`)
    _audit_on = ['create', ]

    # These are columns for your actual database. The prefix `history_entry_`
    # is reserved by the superclass for its public methods.
    example_col = fields.Char()
