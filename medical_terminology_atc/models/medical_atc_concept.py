# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalATCConcept(models.Model):
    """
        Medical ATC concept
        (https://www.hl7.org/fhir/terminologies-systems.html)
        It has been defined following the code system entity with the following
        information:
        - url: http://www.whocc.no/atc
        - identifier: urn:oid:2.16.840.1.113883.6.73
        - name: ATC/DDD
        - publisher: WHO
    """
    _name = 'medical.atc.concept'
    _inherit = 'medical.abstract.concept.uniparent'
    _parent_order = False

    code = fields.Char(
        compute='_compute_code',
        store=True,
        required=False,
    )
    level_code = fields.Char(
        required=True,
    )
    parent_id = fields.Many2one(
        comodel_name='medical.atc.concept',
    )
    child_ids = fields.One2many(
        comodel_name='medical.atc.concept',
    )

    @api.depends('level_code', 'parent_id')
    def _compute_code(self):
        for record in self:
            record.code = record.level_code
            if record.parent_id:
                record.code = record.parent_id.code + record.code
