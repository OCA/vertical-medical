# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalAbstractConceptUniparent(models.AbstractModel):
    # Medical Code system concept
    # (https://www.hl7.org/fhir/codesystem.html)
    _name = 'medical.abstract.concept.uniparent'
    _inherit = 'medical.abstract.concept'
    _parent_name = 'parent_id'
    _parent_store = True
    _parent_order = 'code'

    parent_id = fields.Many2one(
        comodel_name='medical.abstract.concept.uniparent',
        ondelete='restrict'
    )  # SNOMED_CT Field: parent
    child_ids = fields.One2many(
        comodel_name='medical.abstract.concept.uniparent',
        inverse_name='parent_id'
    )  # SNOMED_CT Field: parent
    parent_left = fields.Integer(
        'Left Parent',
        index=True,
    )
    parent_right = fields.Integer(
        'Right Parent',
        index=True,
    )
