# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _


class MedicalMedicament(models.Model):
    _name = 'medical.medicament'
    _inherit = ['mail.thread']
    _inherits = {'product.product': 'product_id'}

    product_id = fields.Many2one(
        comodel_name='product.product',
        required=True,
        ondelete="cascade",
    )
    drug_form_id = fields.Many2one(
        comodel_name='medical.drug.form',
        string='Drug Form',
        required=True,
    )
    drug_route_id = fields.Many2one(
        comodel_name='medical.drug.route',
        string='Drug Route',
    )
    active_component = fields.Char()
    indications = fields.Text()
    therapeutic_action = fields.Char()
    pregnancy_category = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('x', 'X'),
        ('n', 'N'),
    ], help=_('** FDA Pregancy Categories ***\n'
              'CATEGORY A :Adequate and well-controlled human studies have'
              'failed to demonstrate a risk to the fetus in the first'
              'trimester of pregnancy (and there is no evidence of risk in '
              'later trimesters).\n\n'
              'CATEGORY B : Animal reproduction studies have failed to '
              'demonstrate a risk to the fetus and there are no adequate '
              'and well-controlled studies in pregnant women OR Animal '
              'studies have shown an adverse effect, but adequate and '
              'well-controlled studies in pregnant women'
              ' have failed to demonstrate a risk to the fetus in any'
              ' trimester.\n\n'
              'CATEGORY C : Animal reproduction studies have shown an '
              'adverse effect on the fetus and there are no adequate and '
              'well-controlled  studies in humans, but potential benefits '
              'may warrant use of the drug in pregnant women despite '
              'potential risks. \n\n '
              'CATEGORY D : There is positive evidence of human fetal '
              'risk based on adverse reaction data from investigational '
              'or marketing experience or studies in humans, but potential '
              'benefits may warrant use of the drug in pregnant women '
              'despite potential risks.\n\n'
              'CATEGORY X : Studies in animals or humans have demonstrated '
              'fetal abnormalities and/or there is positive evidence of '
              'human fetal risk based on adverse reaction data from '
              'investigational or marketing experience, and the risks '
              'involved in use of the drug in pregnant'
              ' women clearly outweigh potential benefits.\n\n'
              'CATEGORY N : Not yet classified'))
    is_pregnancy_warning = fields.Boolean(
        string='Pregnancy Warning',
        help=_('The drug represents risk to pregnancy or lactancy'))
    dosage_instruction = fields.Text(
        string='Dosage Instructions'
    )
    pregnancy = fields.Text(
        string='Pregnancy Notes',
        help=_('Description of potential effects to pregnancy'),
    )
    notes = fields.Text(
        help=_('Additional information that may be useful'),
    )
    overdosage = fields.Text(
        help=_('Steps to perform in the event of overdosage'),
    )
    storage = fields.Text(
        help=('Storage instructions'),
    )
    adverse_reaction = fields.Text(
        help=_('Potential adverse reactions'),
    )
    presentation = fields.Text()
    composition = fields.Text(
        help=_('Components that make up this medicament')
    )

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            name = '%s - %s' % (rec.product_id.name, rec.drug_form_id.name)
            res.append((rec.id, name))
        return res

    @api.multi
    def onchange_type(self, _type):
        return self.product_id.onchange_type(_type)

    @api.multi
    def onchange_uom(self, uom_id, uom_po_id):
        return self.product_id.onchange_uom(uom_id, uom_po_id)

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_medicament'] = True
        return super(MedicalMedicament, self).create(vals)
