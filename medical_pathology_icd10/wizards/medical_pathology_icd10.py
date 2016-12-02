# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import json
import logging

from io import BytesIO
from xml.etree import ElementTree
from urllib2 import urlopen
from zipfile import ZipFile

from openerp import api, fields, models


_logger = logging.getLogger(__name__)


class MedicalPathologyICD10(models.TransientModel):
    """ It provides a model for importing ICD-10-CM codes to Odoo. """

    _name = 'medical.pathology.icd10'
    _description = 'Medical Abstract Icd10'

    zip_uri = fields.Char(
        default='/'.join((
            'ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS',
            'Publications/ICD10CM/2017/ICD10CM_FY2017_Full_XML.zip',
        )),
        help='URI to full Zip file.',
    )
    file_name = fields.Char(
        default='icd10cm_tabular_2017.xml',
        help='Name of file (inside of zip) representing full tabular xml.',
    )
    code_type_id = fields.Many2one(
        string='Code Type',
        comodel_name='medical.pathology.code.type',
        default=lambda s: s.env.ref('medical_pathology.pathology_code_05'),
        help='Defines what code type is being imported. Leave as default if '
             'you do not know what you are doing.',
    )

    @property
    def module_name(self):
        return 'medical_pathology_icd10'

    @api.model
    def create(self, vals):
        """ It begins import process after create """
        record = super(MedicalPathologyICD10, self).create(vals)
        record.parse_xml()
        return record

    @api.multi
    def parse_xml(self):
        """ It parses the remote XML into a relevant data structure.

        Returns:
            (dict)
        """
        for record in self:
            root = ElementTree.fromstring(record.__get_remote_file())
            for chapter in root.iterfind('chapter'):
                record._process_chapter(chapter)

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
    def _process_chapter(self, chapter):
        """ It processes a ``chapter`` XML node """
        self.ensure_one()
        name = chapter.find('name').text.strip()
        desc = chapter.find('desc').text.strip()
        chapter_desc = self.__create_chapter_desc(chapter)
        chapter_name = '%s - %s' % (name, desc)
        chapter_record = self._upsert_pathology_category(
            chapter_name,
            self.code_type_id,
            name,
        )
        for section_index in chapter.iterfind('sectionIndex'):
            self._process_section_index(chapter_record, section_index)
        for section in chapter.iterfind('section'):
            self._process_section(section)

    @api.multi
    def _process_diag(self, diag, category_record, parent_record=None):
        """ It processes a ``diag`` XML node """
        self.ensure_one()
        note = '\n'.join(
            self.__get_el_text_array(diag.find('inclusionTerm')),
        )
        pathology = self._upsert_pathology(
            name=diag.find('desc').text.strip(),
            code=diag.find('name').text.strip(),
            category=category_record,
            code_type=self.code_type_id,
            parent=parent_record,
            note=note,
        )
        for child_diag in diag.iterfind('diag'):
            self._process_diag(child_diag, category_record, pathology)

    @api.multi
    def _process_section(self, section):
        """ It processes a ``section`` XML node """
        self.ensure_one()
        chapter_name = section.get('id')
        try:
            chapter_record = self.env['ir.model.data'].get_object(
                self.module_name,
                self._get_pathology_category_xml_id(chapter_name),
            )
        except ValueError:
            # Ignore sections that were not found, they are description only.
            # Example: C00-C96
            return
        for diag in section.iterfind('diag'):
            self._process_diag(diag, chapter_record)

    @api.multi
    def _process_section_index(self, chapter_record, section_index):
        """ It processes a ``sectionIndex`` XML node """
        self.ensure_one()
        for section_ref in section_index.iterfind('sectionRef'):
            self._upsert_pathology_category(
                name=section_ref.text.strip(),
                code_type=self.code_type_id,
                ref=section_ref.get('id'),
                parent=chapter_record,
            )

    @api.multi
    def _upsert_pathology(
        self, name, code, category, code_type, parent=None, note=None,
    ):
        """ It updates or creates a new Pathology for arguments.

        Args:
            name: (str) Name of pathology to create.
            code: (str) Code for pathology.
            category: (medical.pathology.category) Singleton representing the
                category for the new pathology.
            code_type: (medical.pathology.code.type) Singleton representing
                the code type of the pathology (ICD-10-CM).
            parent: (medical.pathology) Parent pathology.
            note: (str) Pathology notes.
        Returns:
            (medical.pathology) Newly created Pathology.
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
            pathology = self.env['ir.model.data'].get_object(
                self.module_name,
                xml_id,
            )
            pathology.update(vals)
            return pathology
        except ValueError:            
            pathology = self.env['medical.pathology'].create(vals)
            self.__create_ir_model_data(xml_id, pathology)
        return pathology

    @api.multi
    def _upsert_pathology_category(
        self, name, code_type, ref, parent=None, note=None,
    ):
        """ It updates or creates a new Pathology Category for arguments.

        Args:
            name: (str) Name of pathology category to create.
            code_type: (medical.pathology.code.type) Singleton representing
                the code type of the pathology (ICD-10-CM).
            ref: (str) External ID reference.
            parent: (medical.pathology.category) Parent category.
            note: (str) Category notes.
        Returns:
            (medical.pathology.category) Newly created Pathology Category.
        """
        vals = {
            'name': name,
            'code_type_id': code_type.id,
            'parent_id': parent.id if parent else None,
            'notes': note,
        }
        xml_id = self._get_pathology_category_xml_id(ref)
        try:
            category = self.env['ir.model.data'].get_object(
                self.module_name,
                xml_id,
            )
            category.update(vals)
            return category
        except ValueError:
            category = self.env['medical.pathology.category'].create(vals)
            self.__create_ir_model_data(xml_id, category)
        return category

    def __create_chapter_desc(self, chapter):
        use_additional = self.__get_el_text_array(
            chapter.find('useAdditionalCode'),
        )
        excludes_1 = self.__get_el_text_array(
            chapter.find('excludes1'),
        )
        excludes_2 = self.__get_el_text_array(
            chapter.find('excludes2'),
        )
        includes = self.__get_el_text_array(
            chapter.find('includes'),
        )
        notes = self.__get_el_text_array(
            chapter.find('notes'),
        )
        use_additional.insert(0, 'Use Additional:')
        excludes_1.insert(0, 'Type 1 Excludes:')
        excludes_2.insert(0, 'Type 2 Excludes:')
        includes.insert(0, 'Includes:')
        return '\n'.join((
            '\n'.join(use_additional),
            '\n'.join(excludes_1),
            '\n'.join(excludes_2),
            '\n'.join(includes),
        ))

    def __create_ir_model_data(self, name, record):
        vals = {
            'name': name,
            'model': record._model,
            'module': self.module_name,
            'res_id': record.id,
        }
        return self.env['ir.model.data'].create(vals)

    def __get_el_text_array(self, section, node='note'):
        if not section:
            return []
        return [n.text.strip() for n in section.iterfind(node)]

    @api.multi
    def __get_remote_file(self):
        """ It downloads the remote zip, then extracts & returns the file

        Returns:
            (str) Contents of internal file
        """
        self.ensure_one()
        response = urlopen(self.zip_uri)
        with BytesIO(response.read()) as zip_data:
            with ZipFile(zip_data) as files:
                with files.open(self.file_name) as real_file:
                    return real_file.read()
