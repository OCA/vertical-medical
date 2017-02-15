# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api


class MedicalHistoryAbstract(models.AbstractModel):
    """ Inherit this to provide change audit logging capabilities to any model.

    Public attributes and methods will be prefixed with history_entry in order
    to avoid name collisions with models that will inherit from this class.

    Attributes:
        _audit_on: `list` of methods to log. Supports create, write, and delete
            Override this in child classes in order to add/remove attrs
    """

    _name = 'medical.history.abstract'
    _description = 'Provides inheritable model for change history auditing'
    _audit_on = ['create', 'write', 'delete', ]  # @TODO: Read

    history_entry_ids = fields.One2many(
        string='History Entries',
        help='History entries that apply to this record',
        comodel_name='medical.history.entry',
        inverse_name='associated_record_id_int',
        domain=lambda self: [('associated_model_name', '=', self._name)],
        auto_join=True,
    )

    @api.model
    def create(self, vals):
        """ Override create to create history """
        rec_id = super(MedicalHistoryAbstract, self).create(vals)
        if 'create' in self._audit_on:
            rec_id.history_entry_new('CREATE', vals).state_complete()
        return rec_id

    @api.multi
    def write(self, vals):
        """ Override write to create history """
        if 'write' in self._audit_on:
            entry_ids = self.history_entry_new('UPDATE', vals)
        res = super(MedicalHistoryAbstract, self).write(vals)
        try:
            entry_ids.state_complete()
        except NameError:
            pass
        return res

    @api.multi
    def unlink(self):
        """ Override unlink to create history """
        if 'unlink' in self._audit_on:
            entry_ids = self.history_entry_new('DELETE', {})
        res = super(MedicalHistoryAbstract, self).unlink()
        try:
            entry_ids.state_complete()
        except NameError:
            pass
        return res

    @api.multi
    @api.returns('medical.history.entry')
    def history_entry_new(self, code, vals):
        """
        Create a new history entry given values

        Args:
            code (str): representing Entry type code

        Returns:
            Recordset: of the new entries created
        """
        entry_ids = self.env['medical.history.entry']
        entry_type_id = self.env['medical.history.type'].get_by_code(code)
        for rec_id in self:
            entry_ids += entry_ids.new_entry(rec_id, entry_type_id, vals)
        return entry_ids
