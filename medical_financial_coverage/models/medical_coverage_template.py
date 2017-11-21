# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalCoverageTemplate(models.Model):
    _name = 'medical.coverage.template'
    _description = 'Medical Coverage Template'
    _inherit = ['medical.abstract', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Name',
    )
    payor_id = fields.Many2one(
        string='Payor',
        comodel_name='res.partner',
        domain=[('is_payor', '=', True)],
        required=True,
        index=True,
        help='Payer name',
    )
    coverage_ids = fields.One2many(
        string='Coverage',
        comodel_name='medical.coverage',
        inverse_name='coverage_template_id',
    )
    state = fields.Selection(
        string="Coverage Status",
        required="True",
        selection=[
            ("draft", "Draft"),
            ("active", "Active"),
            ("cancelled", "Cancelled"),
            ("entered-in-error", "Entered In Error")],
        default="draft",
        help="Current state of the coverage.",
    )
    is_editable = fields.Boolean(
        compute='_compute_is_editable',
    )

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.coverage') or '/'

    @api.multi
    @api.depends('name', 'internal_identifier')
    def name_get(self):
        result = []
        for record in self:
            name = '[%s]' % record.internal_identifier
            if record.name:
                name = '%s %s' % (name, record.name)
            result.append((record.id, name))
        return result

    @api.multi
    @api.depends('state')
    def _compute_is_editable(self):
        for rec in self:
            if rec.state in \
                    ('active', 'cancelled', 'entered-in-error'):
                rec.is_editable = False
            else:
                rec.is_editable = True

    def draft2active(self):
        self.write({'state': 'active'})

    def draft2cancelled(self):
        self.write({'state': 'cancelled'})

    def draft2enteredinerror(self):
        self.write({'state': 'entered-in-error'})

    def active2cancelled(self):
        self.write({'state': 'cancelled'})

    def active2enteredinerror(self):
        self.write({'state': 'entered-in-error'})

    def cancelled2enteredinerror(self):
        self.write({'state': 'entered-in-error'})

    def active2draft(self):
        self.write({'state': 'draft'})

    def cancelled2draft(self):
        self.write({'state': 'draft'})

    def cancelled2active(self):
        self.write({'state': 'active'})
