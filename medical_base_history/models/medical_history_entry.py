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

from openerp import fields, models, api, _
from openerp.exceptions import ValidationError


try:
    import cPickle as pickle
except ImportError:
    import pickle


class MedicalHistoryEntry(models.Model):
    '''
    Provides an abstract change log entry object to record changes on models
    '''

    _name = 'medical.history.entry'
    _description = 'Medical History Historying Entries'

    user_id = fields.Many2one(
        string='User',
        help='User that logged history record',
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
    old_record_dict = fields.Binary(
        help='Copy of old record for history auditing',
        readonly=True,
        store=True,
        select=False,
        compute='_compute_old_record_dict',
        inverse='_write_old_record_dict',
    )
    new_record_dict = fields.Binary(
        help='Copy of new record for history auditing',
        readonly=True,
        store=True,
        select=False,
        compute='_compute_old_record_dict',
        inverse='_write_old_record_dict',
    )
    associated_model_id = fields.Many2one(
        string='Associated To Type',
        help='Type of data record that this history entry is associated with',
        comodel_name='ir.model',
        readonly=True,
        required=True,
    )
    associated_model_name = fields.Char(
        string='Associated Record Type',
        related='associated_model_id.name',
        store=True,
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
    def _compute_old_record_dict(self, ):
        ''' Unpickle the old record for usage '''
        for rec_id in self:
            rec_id.old_record_dict = pickle.loads(rec_id.old_record_dict)

    @api.multi
    def _write_old_record_dict(self, ):
        ''' Pickle the old record for storage '''
        for rec_id in self:
            rec_id.old_record_dict = pickle.dumps(rec_id.old_record_dict)

    @api.multi
    def _compute_new_record_dict(self, ):
        ''' Unpickle the new record for usage '''
        for rec_id in self:
            rec_id.new_record_dict = pickle.loads(rec_id.new_record_dict)

    @api.multi
    def _write_new_record_dict(self, ):
        ''' Pickle the new record for storage '''
        for rec_id in self:
            rec_id.new_record_dict = pickle.dumps(rec_id.new_record_dict)

    @api.multi
    def _compute_associated_record_details(self, ):
        ''' Compute the record name and other details for abstract context '''
        for rec_id in self:
            associated_id = self.get_associated_record_id()
            rec_id.associated_record_name = associated_id.name

    @api.multi
    def write(self, vals, ):
        ''' Overload write & disable if state is complete '''
        for rec_id in self:
            if rec_id.state == 'complete':
                raise ValidationError(_(
                    'In order to preserve a compliant timeline, this history '
                    'record cannot be edited once completed. [%s]' % self,
                ))

    @api.multi
    def unlink(self, ):
        ''' Overload unlink & disable '''
        raise ValidationError(_(
            'In order to preserve a compliant timeline, this history '
            'record cannot be destroyed once created. [%s]' % self,
        ))

    @api.multi
    def get_associated_record_id(self, ):
        '''
        Returns the Data Record that this History Record is associated with

        Raises:
            AssertionError: When a Singleton Recordset is not supplied

        Returns:
            `Recordset` - Singleton associated with input record -unknown Model
        '''
        self.ensure_one()
        model_obj = self.env[self.associated_model_id.model]
        return model_obj.browse(self.associated_record_id_int)

    @api.multi
    def get_changed_cols(self, record_obj, new_vals, ):
        '''
        Returns a dictionary of the old values that are about to be changed

        Args:
            new_vals: Dict of new values to check against current record

        Returns:
            `dict` or `None` - Old values that are about to be changed
        '''
        changed = {}
        for key, val in new_vals.items():
            current_val = self.get(key, None)
            if current_val.get and current_val.get('id'):
                current_val = current_val.id
            if val != current_val:
                changed[key] = current_val
        return len(changed) and changed or None

    @api.model
    def _do_history_actions(self, record_id, new_vals, ):
        '''
        Perform history actions for record_id

        Hooks into new_entry to add history actions as defined by the entry
            type. Overload this method in order to provide custom history
            auditing features

        Args:
            new_vals: Dict of new values to check against current record
            record_id: Recordset that the entry is being created for

        Returns:
            `dict` - Values for the new history record
        '''
        entry_type_id = new_vals['entry_type_id']
        changed_cols = record_id.get_changed_cols(new_vals)

        # Old col saving
        if entry_type_id.cols_to_save == 'changed':
            new_vals['old_record_dict'] = changed_cols
        elif entry_type_id.cols_to_save == 'all':
            new_vals['old_record_dict'] = record_id.read()

        # New col saving
        if entry_type_id.new_cols_to_save == 'changed':
            new_vals['new_record_dict'] = new_vals
        elif entry_type_id.new_cols_to_save == 'all':
            new_vals['new_record_dict'] = record_id.read()
            new_vals['new_record_dict'].update(new_vals)

        return new_vals

    @api.model
    @api.returns('self')
    def new_entry(self, record_id, entry_type_id, new_vals, ):
        '''
        Create a new entry from the record and proposed new vals for it

        Args:
            record_id: Recordset Singleton that the entry is being created for
            entry_type_id: Recordset Singleton of `medical.history.type` to
                create
            new_vals: Dict of new values to check against current record

        Returns:
            `Recordset` - Singleton of new history entry
        '''
        entry_vals = {
            'user_id': self.env.user,
            'entry_type_id': entry_type_id.id,
            'associated_model_id': record_id.model.id,
            'associated_record_id_int': record_id.id,
        }
        entry_vals.update(
            self._do_history_actions(record_id, new_vals)
        )
        return self.create(entry_vals)

    @api.multi
    def state_complete(self, ):
        ''' Complete the history entry, indicating a valid record '''
        return self.write({'state': 'complete'})
