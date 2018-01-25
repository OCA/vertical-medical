# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import fields, models, api


class MedicalMedicationTemplate(models.Model):
    _name = 'medical.medication.template'
    _description = 'Medical Medication Template'
    _rec_name = 'pathology_id'

    medicament_id = fields.Many2one(
        string='Medicament',
        comodel_name='medical.medicament',
        required=True,
    )
    pathology_id = fields.Many2one(
        string='Pathology',
        comodel_name='medical.pathology',
        help='Choose a disease for this medicament from the disease list.'
             ' It can be an existing disease of the patient or a'
             ' prophylactic.',
    )
    duration = fields.Integer(
        help='Period that the patient must take the medication',
    )
    duration_uom_id = fields.Many2one(
        string='Duration UoM',
        comodel_name='product.uom',
        domain=[('category_id.name', '=', 'Time')],
        help='Measurement unit for medication duration',
    )
    frequency = fields.Integer(
        help='Time in between doses the patient must wait (ie, for 1 pill '
             'each 8 hours, put here 8 and select "hours\" in the unit field',
    )
    frequency_uom_id = fields.Many2one(
        string='Frequency UoM',
        comodel_name='product.uom',
        domain=[('category_id.name', '=', 'Time')],
        help='Measurement unit for medication frequency',
    )
    frequency_prn = fields.Boolean(
        help='Use medication as needed (pro re nata)',
    )
    medication_dosage_id = fields.Many2one(
        string='Common Dose',
        comodel_name='medical.medication.dosage',
        help='Common / standard dosage frequency for this medicament',
    )
    suggested_administration_hours = fields.Char(
        help='Time that medication should typically be administered',
    )
    quantity = fields.Float(
        string='Dose Quantity',
        help='Quantity of units (eg, 2 capsules) of the medicament',
    )
    dose_uom_id = fields.Many2one(
        string='Dose Unit',
        comodel_name='product.uom',
        help='Measurement unit for dosage quantity',
    )

    @api.multi
    def name_get(self):
        res = []
        for rec_id in self:
            if rec_id.medication_dosage_id:
                name = rec_id.medication_dosage_id.name
            elif rec_id.frequency and rec_id.frequency_uom_id:
                name = '%s / %s' % (
                    rec_id.frequency, rec_id.frequency_uom_id.name
                )
            elif rec_id.pathology_id:
                name = rec_id.pathology_id.name
            else:
                name = rec_id.medicament_id.name
            res.append((rec_id.id, name))
        return res
