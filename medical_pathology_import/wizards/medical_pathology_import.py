# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html)

from odoo import api, fields, models


class MedicalPathologyImport(models.TransientModel):
    """ It provides a model for importing ICD-10-CM codes to Odoo. """

    _name = 'medical.pathology.import'
    _description = 'Medical Pathology Import'

    zip_uri = fields.Char(
        help='URI to full ZIP file',
        string='ZIP File URI',
    )
    file_name = fields.Char(
        help='Name of file (inside of ZIP) representing full tabular XML',
        string='XML File Name',
    )
    code_type_id = fields.Many2one(
        string='Code Type',
        comodel_name='medical.pathology.code.type',
        required=True,
        help='Identifies the code type that is being imported. If you are not'
             ' sure what to choose, select an importer first and leave the'
             ' resulting default',
    )
    importer_type = fields.Selection(
        selection=lambda s: s._get_importer_types(),
        required=True,
        string='Importer Type',
    )

    @api.model
    def _get_importer_types(self):
        return []

    @api.multi
    @api.onchange('importer_type')
    def _onchange_importer_type(self):
        """ It calls gets default data by importer type.

        To plug into this interface, importers should implement method
        ``_onchange_importer_type_*``, such as
        ``_onchange_importer_type_icd10``.
        """
        try:
            method = getattr(
                self, '_onchange_importer_type_%s' % self.importer_type,
            )
            method()
        except AttributeError:
            self.zip_uri = False
            self.file_name = False

    @api.model
    def create(self, vals, no_import=False):
        """ It begins import process after creation unless flag is passed """
        record = super(MedicalPathologyImport, self).create(vals)
        if not no_import:
            record.do_import()
        return record

    @api.multi
    def do_import(self):
        """ It calls the import method for the type of importer.

        Import methods should be named ``do_import_*``, such as
        ``do_import_icd10`` or ``do_import_snomed``.
        """
        self.ensure_one()
        method = getattr(self, 'do_import_%s' % self.importer_type)
        method()

    @api.multi
    def _get_pathology_xml_id(self, code):
        """ It returns the XML ID for a pathology code """
        return 'medical_pathology_%s' % code.replace('.', '_')

    @api.multi
    def _get_pathology_category_xml_id(self, name):
        """ IT returns the XML ID for a pathology category by name """
        name = name.replace('.', '_').replace('-', '_')
        return 'medical_pathology_category_%s' % name

    @api.multi
    def _upsert_pathology(
        self, name, code, category, code_type, id_pref, parent=None, note=None,
    ):
        """ It updates or creates a new Pathology for arguments.

        Args:
            name (str): Name of pathology to create.
            code (str): Code for pathology.
            category (MedicalPathologyCategory): Singleton representing the
                category for the new pathology.
            code_type (MedicalPathologyCodeType): Singleton representing
                the code type of the pathology (ICD-10-CM).
            id_pref (str): External ID prefix for pathology
            parent (MedicalPathology): Parent pathology.
            note (str): Pathology notes.
        Returns:
            MedicalPathology: Newly created Pathology.
        """
        vals = {
            'name': name,
            'code': code,
            'category_id': category.id,
            'code_type_id': code_type.id,
            'parent_id': parent.id if parent else None,
            'notes': note,
        }
        xml_id = self._get_pathology_xml_id(code)
        try:
            pathology = self.env['ir.model.data'].get_object(id_pref, xml_id)
            pathology.update(vals)
            return pathology
        except ValueError:
            pathology = self.env['medical.pathology'].create(vals)
            self.__create_ir_model_data(xml_id, id_pref, pathology)
        return pathology

    @api.multi
    def _upsert_pathology_category(
        self, name, code_type, ref, id_pref, parent=None, note=None,
    ):
        """ It updates or creates a new Pathology Category for arguments.

        Args:
            name (str): Name of pathology category to create.
            code_type (MedicalPathologyCodeType): Singleton representing
                the code type of the pathology (ICD-10-CM).
            ref (str): External ID reference.
            id_pref (str): External ID prefix for category
            parent (MedicalPathologyCategory): Parent category.
            note (str): Category notes.
        Returns:
            MedicalPathologyCategory: Newly created Pathology Category.
        """
        vals = {
            'name': name,
            'code_type_id': code_type.id,
            'parent_id': parent.id if parent else None,
            'notes': note,
        }
        xml_id = self._get_pathology_category_xml_id(ref)
        try:
            category = self.env['ir.model.data'].get_object(id_pref, xml_id)
            category.update(vals)
            return category
        except ValueError:
            category = self.env['medical.pathology.category'].create(vals)
            self.__create_ir_model_data(xml_id, id_pref, category)
        return category

    def __create_ir_model_data(self, name, id_pref, record):
        """ It creates an external reference record for the args """
        vals = {
            'name': name,
            'model': record._name,
            'module': id_pref,
            'res_id': record.id,
        }
        return self.env['ir.model.data'].create(vals)
