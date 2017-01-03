# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import threading

from openerp import api, fields, models


class MedicalAbstractEntity(models.AbstractModel):
    _name = 'medical.abstract.entity'
    _description = 'Medical Abstract Entity'
    _inherits = {'res.partner': 'partner_id'}

    # Redefine ``active`` so that it is managed independently from partner.
    active = fields.Boolean(
        default=True,
    )
    partner_id = fields.Many2one(
        string='Related Partner',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
        index=True,
    )
    type = fields.Selection(
        default=lambda s: s._name,
        related='partner_id.type',
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals = self._create_vals(vals)
        return super(MedicalAbstractEntity, self).create(vals)

    @api.multi
    def action_invalidate(self):
        """ It deactivates a patient, and their partner if no active entities.
        """
        for record in self:
            record.active = False
            entities = self.env[self._name].search([
                ('partner_id', 'child_of', record.partner_id.id),
                ('parent_id', 'child_of', record.partner_id.id),
                ('active', '=', True),
            ])
            if not entities:
                record.partner_id.active = False

    @api.model
    def _create_vals(self, vals):
        """ Overload this in child classes in order to add values. """
        if not vals.get('image'):
            vals['image'] = self._get_default_image(vals)
        return vals

    @api.model
    def _get_default_image(self, vals):
        """ Overload this in child classes in order to add a default image.

        Child classes should only add the image if super returns True. They
        should return a base64 encoded image.

        Example:

            .. code-block:: python

            @api.model
            def _get_default_image(self, vals):
                res = super(MedicalPatient, self)._get_default_image(vals)
                if not res:
                    return res
                img_path = odoo.modules.get_module_resource(
                    'base', 'static/src/img', 'patient-avatar.png',
                )
                with open(img_path, 'r') as image:
                    base64_image = image.read().encode('base64')
                    return odoo.tools.image_resize_image_big(base64_image)

        Args:
            vals (dict): Values dict as passed to create.

        Returns:
            str: Base64 encoded image if there was one.
            bool: False in the event that an image should/could not be
                generated.
        """
        if any((getattr(threading.currentThread(), 'testing', False),
                self._context.get('install_mode'))):
            return False
        return True
