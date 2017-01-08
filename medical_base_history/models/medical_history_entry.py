# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, api, fields, models
from openerp.exceptions import ValidationError


class MedicalHistoryEntry(models.Model):
    """ Provides an abstract change log entry object to record changes. """

    _name = 'medical.history.entry'
    _description = 'Medical History History Entries'

    user_id = fields.Many2one(
        string='Responsible User',
        help='User responsible for this history entry',
        comodel_name='res.users',
        required=True,
    )
    entry_type_id = fields.Many2one(
        string='Entry Type',
        help='Action type that was performed on the record',
        comodel_name='medical.history.type',
        required=True,
    )
    name = fields.Char(
        related='entry_type_id.name',
        help='Humanized name of entry type',
    )
    code = fields.Char(
        related='entry_type_id.code',
        help='Entry type code designation',
    )
    display_name = fields.Char(
        related='entry_type_id.display_name',
    )
    old_record_dict = fields.Serialized(
        help='Copy of old record for history auditing',
        readonly=True,
        store=True,
        select=False,
    )
    new_record_dict = fields.Serialized(
        help='Copy of new record for history auditing',
        readonly=True,
        store=True,
        select=False,
    )
    associated_model_name = fields.Char(
        string='Associated Record Type',
        required=True,
        select=True,
    )
    associated_record_id_int = fields.Integer(
        string='Associated Record ID',
        help='Integer ID of the data record association',
        readonly=True,
        required=True,
    )
    associated_record_name = fields.Char(
        compute='_compute_associated_record_details',
    )
    state = fields.Selection([
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ],
        default='incomplete'
    )

    @api.multi
    def _compute_associated_record_details(self):
        """ Compute the record name and other details for abstract context """
        for record in self:
            associated_id = record.get_associated_record_id()
            record.associated_record_name = associated_id.get_name()

    @api.multi
    def write(self, vals):
        """ Override write & disable if state is complete """
        for record in self:
            if record.state == 'complete':
                raise ValidationError(_(
                    'In order to preserve a compliant timeline, this history '
                    'record cannot be edited once completed. [%s]',
                ) % (
                    record,
                ))

    @api.multi
    def unlink(self):
        """ Override unlink & disable """
        raise ValidationError(_(
            'In order to preserve a compliant timeline, this history '
            'record cannot be edited once completed. [%s]',
        ) % (
            self,
        ))

    @api.multi
    def get_associated_record_id(self):
        """ Returns the Data Record that the History Record is associated with

        Raises:
            AssertionError: When a Singleton Recordset is not supplied

        Returns:
            Recordset: Singleton associated with input record -unknown Model
        """
        self.ensure_one()
        model_obj = self.env[self.associated_model_name]
        return model_obj.browse(self.associated_record_id_int)

    @api.model
    def get_changed_cols(self, record_id, new_vals):
        """ Returns a dictionary of the old values that are about to be changed

        Note that this method should be called *before* the record is updated;
        except in the instances of create, which is called after to circumvent
        known issue with col saving and no record existing.

        Args:
            record_id (Recordset): that is being evaluated for changed cols
            new_vals (dict): of new values to check against current record

        Returns:
            dict: Old values that are about to be changed
        """
        changed = {}
        for key, val in new_vals.items():
            current_val = getattr(record_id, key, None)
            try:  # Handle Recordsets
                current_val = current_val.id
            except AttributeError:
                pass
            if val != current_val:
                changed[key] = current_val
        return len(changed) and changed or {}

    @api.model
    def _do_history_actions(self, record_id, entry_type_id, new_vals):
        """ Perform history actions for record_id

        Hooks into new_entry to add history actions as defined by the entry
            type. Override this method in order to provide custom history
            auditing features

        Args:
            record_id (Recordset): that the entry is being created for
            new_vals (dict): of new values to check against current record

        Returns:
            dict: of values for the new history record
        """

        vals = {}

        # Old col saving
        if entry_type_id.old_cols_to_save == 'changed':
            changed_cols = self.get_changed_cols(record_id, new_vals)
            vals['old_record_dict'] = changed_cols
        elif entry_type_id.old_cols_to_save == 'all':
            vals['old_record_dict'] = record_id.read()[0]

        # New col saving
        if entry_type_id.new_cols_to_save == 'changed':
            vals['new_record_dict'] = new_vals
        elif entry_type_id.new_cols_to_save == 'all':
            vals['new_record_dict'] = record_id.read()[0]
            vals['new_record_dict'].update(new_vals)

        return vals

    @api.model
    @api.returns('self')
    def new_entry(self, record_id, entry_type_id, new_vals):
        """ Create a new entry from the record and proposed new vals for it

        Args:
            record_id: `Recordset` Singleton that the entry is being created
                for
            entry_type_id: `Recordset` Singleton of `medical.history.type` to
                create
            new_vals: `dict` of new values to check against current record

        Returns:
            `Recordset` Singleton of new history entry
        """
        entry_vals = {
            'user_id': self.env.user.id,
            'entry_type_id': entry_type_id.id,
            'associated_model_name': record_id._name,
            'associated_record_id_int': record_id.id,
        }
        entry_vals.update(
            self._do_history_actions(
                record_id, entry_type_id, new_vals
            )
        )
        return self.create(entry_vals)

    @api.multi
    def state_complete(self):
        """ Complete the history entry, indicating a valid record """
        return self.write({'state': 'complete'})
