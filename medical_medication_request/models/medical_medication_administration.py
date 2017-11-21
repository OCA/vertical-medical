# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools import float_compare


class MedicalMedicationAdministration(models.Model):
    _name = 'medical.medication.administration'
    _inherit = 'medical.event'

    def _default_patient_location(self):
        return self.env.ref('medical_medication_request.location_patient')

    medication_request_id = fields.Many2one(
        comodel_name='medical.medication.request',
    )
    location_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[
            ('is_location', '=', True),
            ('stock_location_id', '!=', False)],
    )
    stock_location_id = fields.Many2one(
        comodel_name='stock.location',
        related='location_id.stock_location_id',
    )
    patient_location_id = fields.Many2one(
        comodel_name='stock.location',
        default=_default_patient_location,
    )
    product_id = fields.Many2one(
        'product.product',
        'Product',
        required=True,
        states={'done': [('readonly', True)]},
    )
    product_uom_id = fields.Many2one(
        'product.uom',
        'Unit of Measure',
        required=True,
        states={'done': [('readonly', True)]},
    )
    tracking = fields.Selection(
        'Product Tracking',
        readonly=True,
        related="product_id.tracking",
    )
    lot_id = fields.Many2one(
        'stock.production.lot',
        'Lot',
        states={'done': [('readonly', True)]},
        domain="[('product_id', '=', product_id)]",
    )
    package_id = fields.Many2one(
        'stock.quant.package',
        'Package',
        states={'done': [('readonly', True)]},
    )
    qty = fields.Float(
        'Quantity',
        default=1.0,
        required=True,
        states={'done': [('readonly', True)]},
    )
    move_id = fields.Many2one(
        'stock.move',
    )

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.product_uom_id = self.product_id.uom_id.id

    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.medication.administration') or '/'

    def _prepare_move_values(self):
        self.ensure_one()
        return {
            'name': self.name or self.internal_identifier,
            'origin': self.internal_identifier,
            'product_id': self.product_id.id,
            'product_uom': self.product_uom_id.id,
            'product_uom_qty': self.qty,
            'location_id': self.stock_location_id.id,
            'location_dest_id': self.patient_location_id.id,
            'move_line_ids': [(0, 0, {
                'product_id': self.product_id.id,
                'product_uom_id': self.product_uom_id.id,
                'qty_done': self.qty,
                'location_id': self.stock_location_id.id,
                'location_dest_id': self.patient_location_id.id,
                'package_id': self.package_id.id,
                'lot_id': self.lot_id.id,
                'medication_administration_id': self.id
            })]
        }

    @api.multi
    def in_progress2completed(self):
        self.ensure_one()
        precision = self.env['decimal.precision'].precision_get(
            'Product Unit of Measure')
        available_qty = sum(self.env['stock.quant']._gather(
            self.product_id,
            self.stock_location_id,
            self.lot_id,
            self.package_id,
            strict=True
        ).mapped('quantity'))
        if self.product_id.type == 'consu' or float_compare(
            available_qty, self.qty, precision_digits=precision
        ) >= 0:
            self.generate_move()
            return super(
                MedicalMedicationAdministration, self).in_progress2completed()
        raise ValidationError(_('Insufficient quantity'))

    @api.multi
    def generate_move(self):
        for event in self:
            if not self.location_id:
                raise ValidationError(_(
                    'Location must be defined in order to complete'))
            move = self.env['stock.move'].create(event._prepare_move_values())
            move._action_done()
            event.write({
                'move_id': move.id,
                'occurrence_date': fields.Datetime.now()
            })

    def action_view_stock_moves(self):
        action = self.env.ref('stock.stock_move_line_action').read([])[0]
        action['domain'] = [('move_id', '=', self.move_id.id)]
        return action
