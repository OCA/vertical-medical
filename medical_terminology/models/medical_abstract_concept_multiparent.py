# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalAbstractConceptMultiparent(models.AbstractModel):
    # Medical Code system concept
    # (https://www.hl7.org/fhir/codesystem.html)
    _name = 'medical.abstract.concept.multiparent'
    _inherit = 'medical.abstract.concept'

    parent_ids = fields.Many2many(
        comodel_name='medical.abstract.concept',
        relation='medical_abstract_concept_is_a',
        column1='parent',
        column2='child',
    )
    child_ids = fields.Many2many(
        comodel_name='medical.abstract.concept',
        compute='_compute_child_ids'
    )  # FHIR Field: concept/concept
    full_parent_ids = fields.Many2many(
        comodel_name='medical.abstract.concept',
        compute='_compute_child_ids'
    )
    full_child_ids = fields.Many2many(
        comodel_name='medical.abstract.concept',
        compute='_compute_full_child_ids'
    )

    def _get_childs(self):
        res = self.child_ids.ids or []
        for child in self.child_ids:
            res += child._get_childs()
        return res

    @api.multi
    @api.depends('parent_ids')
    def _compute_full_child_ids(self):
        for record in self:
            record.full_child_ids = record.browse(record._get_childs())

    @api.multi
    @api.depends('parent_ids')
    def _compute_child_ids(self):
        for record in self:
            record.child_ids = self.search([('parent_ids', '=', record.id)])
            full_parents = record.parent_ids.ids or []
            for parent in record.parent_ids:
                full_parents += parent.full_parent_ids.ids
            record.full_parent_ids = record.browse(full_parents)
