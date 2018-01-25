# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html)

import logging

from io import BytesIO
from xml.etree import ElementTree
from urllib2 import urlopen
from zipfile import ZipFile

from odoo import api, models

_logger = logging.getLogger(__name__)


class MedicalPathologyImport(models.TransientModel):
    """ It provides a model for importing ICD-10-CM codes to Odoo. """

    _inherit = 'medical.pathology.import'

    ICD10_URI = '/'.join((
        'ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS',
        'Publications/ICD10CM/2017/ICD10CM_FY2017_Full_XML.zip',
    ))
    ICD10_FILE_NAME = 'icd10cm_tabular_2017.xml'
    ICD10_CODE = 'medical_pathology.pathology_code_05'
    ICD10_XML_PREFIX = 'medical_pathology_icd10_test'

    @api.model
    def _get_importer_types(self):
        res = super(MedicalPathologyImport, self)._get_importer_types()
        return res + [('icd10', 'ICD-10-CM')]

    @api.multi
    def _onchange_importer_type_icd10(self):
        self.code_type_id = self.env.ref(self.ICD10_CODE)
        self.file_name = self.ICD10_FILE_NAME
        self.zip_uri = self.ICD10_URI

    @api.multi
    def do_import_icd10(self):
        """ It parses the remote XML into a relevant data structure. """
        for record in self:
            root = ElementTree.fromstring(record.__get_remote_file())
            for chapter in root.iterfind('chapter'):
                record._icd10_process_chapter(chapter)

    @api.multi
    def _icd10_process_chapter(self, chapter):
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
            self.ICD10_XML_PREFIX,
            note=chapter_desc,
        )
        for section_index in chapter.iterfind('sectionIndex'):
            self._icd10_process_section_index(chapter_record, section_index)
        for section in chapter.iterfind('section'):
            self._icd10_process_section(section)

    @api.multi
    def _icd10_process_diag(self, diag, category_record, parent_record=None):
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
            id_pref=self.ICD10_XML_PREFIX,
        )
        for child_diag in diag.iterfind('diag'):
            self._icd10_process_diag(child_diag, category_record, pathology)

    @api.multi
    def _icd10_process_section(self, section):
        """ It processes a ``section`` XML node """
        self.ensure_one()
        chapter_name = section.get('id')
        try:
            chapter_record = self.env['ir.model.data'].get_object(
                self.ICD10_XML_PREFIX,
                self._get_pathology_category_xml_id(chapter_name),
            )
        except ValueError:
            # Ignore sections that were not found, they are description only.
            # Example: C00-C96
            return
        for diag in section.iterfind('diag'):
            self._icd10_process_diag(diag, chapter_record)

    @api.multi
    def _icd10_process_section_index(self, chapter_record, section_index):
        """ It processes a ``sectionIndex`` XML node """
        self.ensure_one()
        for section_ref in section_index.iterfind('sectionRef'):
            self._upsert_pathology_category(
                name=section_ref.text.strip(),
                code_type=self.code_type_id,
                ref=section_ref.get('id'),
                parent=chapter_record,
                id_pref=self.ICD10_XML_PREFIX,
            )

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

        if use_additional:
            use_additional.insert(0, 'Use Additional:')
        if excludes_1:
            excludes_1.insert(0, 'Type 1 Excludes:')
        if excludes_2:
            excludes_2.insert(0, 'Type 2 Excludes:')
        if includes:
            includes.insert(0, 'Includes:')
        if notes:
            notes.insert(0, 'Extra Notes:')

        descriptors = (
            '\n'.join(use_additional),
            '\n'.join(excludes_1),
            '\n'.join(excludes_2),
            '\n'.join(includes),
            '\n'.join(notes),
        )
        return '\n'.join(filter(None, descriptors))

    def __get_el_text_array(self, section, node='note'):
        if section is None:
            return []
        return [n.text.strip() for n in section.iterfind(node)]

    @api.multi
    def __get_remote_file(self):
        """ It downloads the remote zip, then extracts & returns the file

        Returns:
            str: Contents of internal file
        """
        self.ensure_one()
        response = urlopen(self.zip_uri)
        with BytesIO(response.read()) as zip_data:
            with ZipFile(zip_data) as files:
                with files.open(self.file_name) as real_file:
                    return real_file.read()
