# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, exceptions, api, _


class MedicalPrescriptionOrder(models.Model):
    """
    Add State verification functionality to MedicalPrescriptionOrder

    This model will allow you to plug in verification methods to Rx Orders,
    allowing for custom business logic in regards to workflows and auditing.

    Attributes:
        _ALLOWED_CHANGE_KEYS: `list` of keys that are allowed to be changed
            on an RX after it has been verified (without moving to a stage
            that has been defined in `_ALLOWED_CHANGE_STATES`)
        _ALLOWED_CHANGE_STATES: `list` of keys defining status types in which
            an RX can be moved to after being verified
    """

    _inherit = 'medical.prescription.order'

    _ALLOWED_CHANGE_KEYS = ['stage_id', ]
    _ALLOWED_CHANGE_STATES = ['verified', 'cancel', 'exception', ]

    stage_id = fields.Many2one(
        'medical.prescription.order.state',
        'State',
        track_visibility='onchange',
        index=True,
        copy=False,
        help="The state in Kanban view",
        default=lambda self: self.env.ref(
            'medical_prescription_state_verify.state_verification'
        ),
    )

    state_type = fields.Selection(
        related='stage_id.type',
        help="The state type for the order",
    )

    @api.multi
    def write(self, vals, ):
        """
        Overload write & perform audit validations

        Raises:
            ValidationError: When a write is not allowed due to being in a
                protected state
        """
        for rec_id in self:
            if rec_id.state_type == 'verified':

                # Only allow changes for keys in self._ALLOWED_CHANGE_KEYS
                keys = vals.keys()
                for allowed_key in self._ALLOWED_CHANGE_KEYS:
                    try:
                        del keys[keys.index(allowed_key)]
                    except ValueError:
                        pass
                if len(keys) > 0:
                    raise exceptions.ValidationError(_(
                        'You cannot edit this value after an Rx has been'
                        ' verified. Please either cancel it, or mark it as an'
                        ' exception if manual reversals are required. [%s]' %
                        rec_id.name
                    ))

                # Only allow state changes from self._ALLOWED_CHANGE_STATES
                if vals.get('stage_id'):
                    stage_id = self.env['%s.state' % self._name].browse(
                        vals['stage_id']
                    )
                    if stage_id.type not in self._ALLOWED_CHANGE_STATES:
                        raise exceptions.ValidationError(_(
                            'You cannot move an Rx into this state after it'
                            ' has been verified. [%s]' % rec_id.name
                        ))

            return super(MedicalPrescriptionOrder, self).write(vals)
