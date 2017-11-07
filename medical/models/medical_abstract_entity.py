# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import threading
import base64

from odoo import api, fields, models


class MedicalAbstractEntity(models.AbstractModel):
    _name = 'medical.abstract.entity'
    _description = 'Medical Abstract Entity'
    _inherits = {'res.partner': 'partner_id'}
    _inherit = ['mail.thread']

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
    def toggle_active(self):
        """ It toggles patient and partner activation. """
        for record in self:
            super(MedicalAbstractEntity, self).toggle_active()
            if record.active:
                record.partner_id.active = True
            else:
                entities = record.env[record._name].search([
                    ('partner_id', 'child_of', record.partner_id.id),
                    ('parent_id', 'child_of', record.partner_id.id),
                    ('active', '=', True),
                ])
                if not entities:
                    record.partner_id.active = False

    @api.model
    def _create_vals(self, vals):
        """ Override this in child classes in order to add default values. """
        if self._allow_image_create(vals):
            vals['image'] = self._get_default_image_encoded(vals)
        return vals

    @api.model_cr_context
    def _allow_image_create(self, vals):
        """ It determines if conditions are present that should stop image gen.

        This is implemented so that tests aren't wildly creating images left
         and right for no reason. Child classes could also inherit this to
         provide custom rules for image generation.

        Note that this method explicitly allows image generation if
         ``__image_create_allow`` is a ``True`` value in the context. Any
         child that chooses to provide custom rules shall also adhere to this
         context, unless there is a documented reason to not do so.
        """
        if vals.get('image'):
            return False
        if any((getattr(threading.currentThread(), 'testing', False),
                self._context.get('install_mode'))):
            if not self.env.context.get('__image_create_allow'):
                return False
        return True

    def _get_default_image_encoded(self, vals):
        """ It returns the base64 encoded image string for the default avatar.

        Args:
            vals (dict): Values dict as passed to create.

        Returns:
            str: A base64 encoded image.
            NoneType: None if no result.
        """
        image_path = self._get_default_image_path(vals)
        import logging
        logging.info(image_path)
        if not image_path:
            return False
        with open(image_path, 'rb') as image:
            return base64.b64encode(image.read())

    @api.model_cr_context
    def _get_default_image_path(self, vals):
        """ Overload this in child classes in order to add a default image.

        Example:

            .. code-block:: python
            @api.model
            def _get_default_image_path(self, vals):
                res = super(MedicalPatient, self)._get_default_image_path(vals)
                if res:
                    return res
                image_path = odoo.modules.get_module_resource(
                    'base', 'static/src/img', 'patient-avatar.png',
                )
                return image_path

        Args:
            vals (dict): Values dict as passed to create.

        Returns:
            str: A file path to the image on disk.
            bool: False if error.
            NoneType: None if no result.
        """
        return False  # pragma: no cover

    def toggle(self, attr):
        if getattr(self, attr) is True:
            self.write({attr: False})
        elif getattr(self, attr) is False:
            self.write({attr: True})
