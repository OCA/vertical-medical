# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalSpecialty(models.Model):
    # FHIR Entity: PractitionerRole
    # (https://www.hl7.org/fhir/practitionerrole.html)
    _name = 'medical.specialty'
    _description = 'Specialty'

    name = fields.Char(
        required=True,
    )
    description = fields.Char(
        required=True,
    )
    active = fields.Boolean(
        default=True,
    )
    sct_code = fields.Many2one(
        comodel_name='medical.sct.concept',
        domain=[('is_specialty', '=', True)],
    )  # FHIR Field: code
