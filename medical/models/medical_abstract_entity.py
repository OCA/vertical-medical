# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import threading

from odoo import _, api, fields, models
from odoo.exceptions import UserError


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

    @api.multi
    @api.depends('id_numbers')
    def _compute_identification(self, field_name, category_code):
        """ It computes a field that indicates a certain ID type.

        Use this on a field that represents a certain ID type. It will compute
        the desired field as that ID(s).

        This ID can be worked with as if it were a Char field, but it will
        be relating back to a ``res.partner.id_number`` instead.

        Example:

            .. code-block:: python

            social_security_id = fields.Char(
                string='Social Security',
                compute=lambda s: s._compute_identification(
                    'social_security_id', 'SSN',
                ),
                inverse=lambda s: s._inverse_identification(
                    'social_security_id', 'SSN',
                ),
            )

        Args:
            field_name: Name of field to set.
            category_code: Category code of the Identification type.
        """
        for record in self:
            id_numbers = record.id_numbers.filtered(
                lambda r: r.category_id.code == category_code
            )
            if not id_numbers:
                continue
            # Singleton cannot be validated, because the record can be
            #   manipulated from underneath the patient. Consider:
            #       * User adds a second driver's license through partner,
            #           but leaves the other active.
            #       * User navigates to partner's associated patient record
            #       UserError(*)
            value = id_numbers[0].name
            setattr(record, field_name, value)

    @api.multi
    def _inverse_identification(self, field_name, category_code):
        """ It provides an inverse for the identification field.

        This method will create a new record, or modify the existing one
        in order to allow for the associated field to work like a Char.

        Example:

            .. code-block:: python

            social_security_id = fields.Char(
                string='Social Security',
                compute=lambda s: s._compute_identification(
                    'social_security_id', 'SSN',
                ),
                inverse=lambda s: s._inverse_identification(
                    'social_security_id', 'SSN',
                ),
            )

        Args:
            field_name: Name of field to set.
            category_code: Category code of the Identification type.
        """
        for record in self:
            id_number = record.id_numbers.filtered(
                lambda r: r.category_id.code == category_code
            )
            record_len = len(id_number)
            if record_len == 0:
                category = self.env['res.partner.id_category'].search([
                    ('code', '=', category_code),
                ])
                self.env['res.partner.id_number'].create({
                    'partner_id': record.partner_id.id,
                    'category_id': category.id,
                    'name': getattr(record, field_name),
                })
            elif record_len == 1:
                value = getattr(record, field_name)
                id_number.name = value
            else:
                raise UserError(_(
                    'This %s has multiple IDs of this type (%s), so a write '
                    'via the %s field is not possible. In order to fix this, '
                    'please use the IDs tab.',
                ) % (
                    record._name, category_code.name, field_name,
                ))

    @api.model
    def _create_vals(self, vals):
        """ Override this in child classes in order to add default values. """
        if self._allow_image_create(vals):
            vals['image'] = self._get_default_image(vals)
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

    @api.model_cr_context
    def _get_default_image(self, vals):
        """ Overload this in child classes in order to add a default image.

        Child classes should only add the image if super returns False/None.
        They should return a base64 encoded image.

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
            bool: False if error.
            NoneType: None if no result.
        """
        return  # pragma: no cover
