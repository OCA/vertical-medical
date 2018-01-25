# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html)

from copy import deepcopy
from mock import patch
from tempfile import TemporaryFile
from xml.etree import ElementTree
from zipfile import ZipFile
from odoo.tests.common import TransactionCase

S_PATH = 'odoo.addons.medical_pathology_icd10.wizards'
P_PATH = 'odoo.addons.medical_pathology_import.wizards'
IMPORT_PATH = S_PATH + '.medical_pathology_import.MedicalPathologyImport'
P_IMPORT_PATH = P_PATH + '.medical_pathology_import.MedicalPathologyImport'


class TestMedicalPathologyImport(TransactionCase):

    def setUp(self):
        super(TestMedicalPathologyImport, self).setUp()

        self.test_wizard = self.env['medical.pathology.import'].new({
            'importer_type': 'icd10',
        })

        self.test_xml = 'Test XML'
        with TemporaryFile() as test_file:
            with ZipFile(test_file, 'w') as test_zip:
                file_name = self.test_wizard.ICD10_FILE_NAME
                test_zip.writestr(file_name, self.test_xml)

            test_file.seek(0)
            self.test_response = test_file.read()

        self.test_chapter = ElementTree.fromstring(
            '<chapter>'
            '<name>Test Name</name>'
            '<desc>Test Description</desc>'
            '<useAdditionalCode>'
            '<note>Test Additional</note>'
            '</useAdditionalCode>'
            '<excludes1><note>Test Exclude 1</note></excludes1>'
            '<excludes2><note>Test Exclude 2</note></excludes2>'
            '<includes><note>Test Include</note></includes>'
            '<notes><note>Test Note</note></notes>'
            '<sectionIndex id="test_1"></sectionIndex>'
            '<sectionIndex id="test_2"></sectionIndex>'
            '<section id="test_1"></section>'
            '<section id="test_2"></section>'
            '</chapter>'
        )
        self.test_section_index = ElementTree.fromstring(
            '<sectionIndex>'
            '<sectionRef id="test_1">Test Name</sectionRef>'
            '<sectionRef id="test_2">Test Name 2</sectionRef>'
            '</sectionIndex>'
        )
        self.test_section = ElementTree.fromstring(
            '<section id="test_1">'
            '<diag id="test_1"></diag>'
            '<diag id="test_2"></diag>'
            '</section>'
        )
        self.test_diag = ElementTree.fromstring(
            '<diag>'
            '<name>Test Name</name>'
            '<desc>Test Description</desc>'
            '<inclusionTerm>'
            '<note>Test Note</note>'
            '</inclusionTerm>'
            '</diag>'
        )

    def test_get_importer_types_correct(self):
        """It should add correct ICD-10 entry to list of types"""
        resulting_types = self.test_wizard._get_importer_types()
        self.assertIn(('icd10', 'ICD-10-CM'), resulting_types)

    def test_onchange_importer_type_icd10_correct(self):
        """It should correctly update fields with ICD-10 values"""
        self.test_wizard._onchange_importer_type_icd10()

        expected_type = self.env.ref(self.test_wizard.ICD10_CODE)
        expected_file = self.test_wizard.ICD10_FILE_NAME
        expected_uri = self.test_wizard.ICD10_URI
        self.assertEqual(self.test_wizard.code_type_id, expected_type)
        self.assertEqual(self.test_wizard.file_name, expected_file)
        self.assertEqual(self.test_wizard.zip_uri, expected_uri)

    @patch(IMPORT_PATH + '._icd10_process_chapter')
    @patch(IMPORT_PATH + '._MedicalPathologyImport__get_remote_file')
    def test_do_import_icd10_helper_calls(self, file_mock, chapter_mock):
        """It should call helper once per <chapter> in XML file"""
        file_mock.return_value = ''.join((
            '<test>',
            '<chapter id="1"></chapter>',
            '<dud></dud>',
            '<chapter id="2"></chapter>',
            '</test>',
        ))
        chapter_mock.reset_mock()
        self.test_wizard.do_import_icd10()

        resulting_calls = chapter_mock.mock_calls
        first_call_args = resulting_calls[0][1]
        second_call_args = resulting_calls[1][1]
        self.assertEqual(len(resulting_calls), 2)
        self.assertEqual(first_call_args[0].tag, 'chapter')
        self.assertEqual(first_call_args[0].get('id'), '1')
        self.assertEqual(second_call_args[0].tag, 'chapter')
        self.assertEqual(second_call_args[0].get('id'), '2')

    def test_icd10_process_chapter_ensure_singleton(self):
        """It should raise an exception when called with multiple records"""
        test_wizard_2 = self.env['medical.pathology.import'].new()
        test_wizard_set = self.test_wizard + test_wizard_2

        with self.assertRaises(ValueError):
            test_wizard_set._icd10_process_chapter(None)

    @patch(P_IMPORT_PATH + '._upsert_pathology_category')
    @patch(IMPORT_PATH + '._MedicalPathologyImport__create_chapter_desc')
    def test_icd10_process_chapter_upsert_call(self, desc_mock, upsert_mock):
        """It should call category upsert, passing in correct values"""
        self.test_wizard._onchange_importer_type_icd10()
        test_long_desc = 'Test Long Description'
        desc_mock.return_value = test_long_desc
        upsert_mock.reset_mock()
        self.test_wizard._icd10_process_chapter(self.test_chapter)

        upsert_mock.assert_called_once_with(
            'Test Name - Test Description',
            self.test_wizard.code_type_id,
            'Test Name',
            self.test_wizard.ICD10_XML_PREFIX,
            note=test_long_desc,
        )

    @patch(IMPORT_PATH + '._icd10_process_section_index')
    @patch(P_IMPORT_PATH + '._upsert_pathology_category')
    def test_icd10_process_chapter_sect_index(self, upsert_mock, index_mock):
        """It should call correct helper once per <sectionIndex> in chapter"""
        test_path_category = 'Totally A Record'
        upsert_mock.return_value = test_path_category
        index_mock.reset_mock()
        self.test_wizard._icd10_process_chapter(self.test_chapter)

        resulting_calls = index_mock.mock_calls
        first_call_args = resulting_calls[0][1]
        second_call_args = resulting_calls[1][1]
        self.assertEqual(len(resulting_calls), 2)
        self.assertEqual(first_call_args[0], test_path_category)
        self.assertEqual(first_call_args[1].tag, 'sectionIndex')
        self.assertEqual(first_call_args[1].get('id'), 'test_1')
        self.assertEqual(second_call_args[0], test_path_category)
        self.assertEqual(second_call_args[1].tag, 'sectionIndex')
        self.assertEqual(second_call_args[1].get('id'), 'test_2')

    @patch(IMPORT_PATH + '._icd10_process_section')
    def test_icd10_process_chapter_section(self, section_mock):
        """It should call correct helper once per <section> in chapter"""
        section_mock.reset_mock()
        self.test_wizard._icd10_process_chapter(self.test_chapter)

        resulting_calls = section_mock.mock_calls
        first_call_args = resulting_calls[0][1]
        second_call_args = resulting_calls[1][1]
        self.assertEqual(len(resulting_calls), 2)
        self.assertEqual(first_call_args[0].tag, 'section')
        self.assertEqual(first_call_args[0].get('id'), 'test_1')
        self.assertEqual(second_call_args[0].tag, 'section')
        self.assertEqual(second_call_args[0].get('id'), 'test_2')

    def test_icd10_process_diag_ensure_singleton(self):
        """It should raise an exception when called with multiple records"""
        test_wizard_2 = self.env['medical.pathology.import'].new()
        test_wizard_set = self.test_wizard + test_wizard_2

        with self.assertRaises(ValueError):
            test_wizard_set._icd10_process_diag(None, None)

    @patch(P_IMPORT_PATH + '._upsert_pathology')
    def test_icd10_process_diag_upsert_call(self, upsert_mock):
        """It should call pathology upsert, passing in correct values"""
        self.test_wizard._onchange_importer_type_icd10()
        upsert_mock.reset_mock()
        self.test_wizard._icd10_process_diag(self.test_diag, 'Category Record')

        upsert_mock.assert_called_once_with(
            name='Test Description',
            code='Test Name',
            category='Category Record',
            code_type=self.test_wizard.code_type_id,
            parent=None,
            note='Test Note',
            id_pref=self.test_wizard.ICD10_XML_PREFIX,
        )

    @patch(P_IMPORT_PATH + '._upsert_pathology')
    def test_icd10_process_diag_child_diag_upsert_call(self, upsert_mock):
        """It should correctly call pathology upsert on each child <diag>"""
        self.test_wizard._onchange_importer_type_icd10()
        self.test_diag_2 = deepcopy(self.test_diag)
        self.test_diag_2.find('name').text += ' 2'
        self.test_diag.append(self.test_diag_2)
        test_parent = 'Test Parent'
        upsert_mock.return_value = test_parent
        upsert_mock.reset_mock()
        self.test_wizard._icd10_process_diag(self.test_diag, 'Category Record')

        self.assertEqual(len(upsert_mock.mock_calls), 2)
        upsert_mock.assert_any_call(
            name='Test Description',
            code='Test Name',
            category='Category Record',
            code_type=self.test_wizard.code_type_id,
            parent=None,
            note='Test Note',
            id_pref=self.test_wizard.ICD10_XML_PREFIX,
        )
        upsert_mock.assert_called_with(
            name='Test Description',
            code='Test Name 2',
            category='Category Record',
            code_type=self.test_wizard.code_type_id,
            parent=test_parent,
            note='Test Note',
            id_pref=self.test_wizard.ICD10_XML_PREFIX,
        )

    def test_icd10_process_section_ensure_singleton(self):
        """It should raise an exception when called with multiple records"""
        test_wizard_2 = self.env['medical.pathology.import'].new()
        test_wizard_set = self.test_wizard + test_wizard_2

        with self.assertRaises(ValueError):
            test_wizard_set._icd10_process_section(None)

    @patch(IMPORT_PATH + '._icd10_process_diag')
    def test_icd10_process_section_no_matching_category(self, diag_mock):
        """It should not call helper when no category with matching XML ID"""
        diag_mock.reset_mock()
        self.test_wizard._icd10_process_section(self.test_section)

        diag_mock.assert_not_called()

    @patch(IMPORT_PATH + '._icd10_process_diag')
    def test_icd10_process_section_matching_category(self, diag_mock):
        """It should call helper on each <diag> if category XML ID match"""
        test_category = self.env['medical.pathology.category'].create({
            'name': 'Test Category',
        })
        self.env['ir.model.data'].create({
            'name': 'medical_pathology_category_test_1',
            'model': 'medical.pathology.category',
            'module': self.test_wizard.ICD10_XML_PREFIX,
            'res_id': test_category.id,
        })
        diag_mock.reset_mock()
        self.test_wizard._icd10_process_section(self.test_section)

        resulting_calls = diag_mock.mock_calls
        first_call_args = resulting_calls[0][1]
        second_call_args = resulting_calls[1][1]
        self.assertEqual(len(resulting_calls), 2)
        self.assertEqual(first_call_args[0].tag, 'diag')
        self.assertEqual(first_call_args[0].get('id'), 'test_1')
        self.assertEqual(first_call_args[1], test_category)
        self.assertEqual(second_call_args[0].tag, 'diag')
        self.assertEqual(second_call_args[0].get('id'), 'test_2')
        self.assertEqual(second_call_args[1], test_category)

    def test_icd10_process_section_index_ensure_singleton(self):
        """It should raise an exception when called with multiple records"""
        test_wizard_2 = self.env['medical.pathology.import'].new()
        test_wizard_set = self.test_wizard + test_wizard_2

        with self.assertRaises(ValueError):
            test_wizard_set._icd10_process_section_index(None, None)

    @patch(P_IMPORT_PATH + '._upsert_pathology_category')
    def test_icd10_process_section_index_upsert_call(self, upsert_mock):
        """It should correctly call category upsert once per <sectionRef>"""
        self.test_wizard._onchange_importer_type_icd10()
        test_chapter = 'Totally A Real Category'
        upsert_mock.reset_mock()
        self.test_wizard._icd10_process_section_index(
            test_chapter,
            self.test_section_index,
        )

        self.assertEqual(len(upsert_mock.mock_calls), 2)
        upsert_mock.assert_any_call(
            name='Test Name',
            code_type=self.test_wizard.code_type_id,
            ref='test_1',
            parent=test_chapter,
            id_pref=self.test_wizard.ICD10_XML_PREFIX,
        )
        upsert_mock.assert_called_with(
            name='Test Name 2',
            code_type=self.test_wizard.code_type_id,
            ref='test_2',
            parent=test_chapter,
            id_pref=self.test_wizard.ICD10_XML_PREFIX,
        )

    def test__create_chapter_desc_correct_output(self):
        """It should correctly process subnodes and create description"""
        test_result = self.test_wizard\
            ._MedicalPathologyImport__create_chapter_desc(self.test_chapter)

        expected_result = (
            'Use Additional:\nTest Additional\n'
            'Type 1 Excludes:\nTest Exclude 1\n'
            'Type 2 Excludes:\nTest Exclude 2\n'
            'Includes:\nTest Include\n'
            'Extra Notes:\nTest Note'
        )
        self.assertEqual(test_result, expected_result)

    def test__create_chapter_desc_no_heading_for_missing(self):
        """It should not include headings for missing subnodes"""
        includes_subnode = self.test_chapter.find('includes')
        self.test_chapter.remove(includes_subnode)
        test_result = self.test_wizard\
            ._MedicalPathologyImport__create_chapter_desc(self.test_chapter)

        expected_result = (
            'Use Additional:\nTest Additional\n'
            'Type 1 Excludes:\nTest Exclude 1\n'
            'Type 2 Excludes:\nTest Exclude 2\n'
            'Extra Notes:\nTest Note'
        )
        self.assertEqual(test_result, expected_result)

    def test__get_el_text_array_no_element(self):
        """It should return empty list if no element passed in"""
        test_result = self.test_wizard\
            ._MedicalPathologyImport__get_el_text_array(None)

        self.assertEqual(test_result, [])

    def test__get_el_text_array_no_specified_subelements(self):
        """It should return empty list if no specified subelements"""
        test_result = self.test_wizard\
            ._MedicalPathologyImport__get_el_text_array(
                self.test_chapter,
                'missing_element',
            )

        self.assertEqual(test_result, [])

    def test__get_el_text_array_correct_output(self):
        """It should return correct list if specified subelements present"""
        test_element = ElementTree.fromstring(
            '<element>'
            '<subelement>Test Note</subelement>'
            '<subelement>Test Note 2</subelement>'
            '</element>'
        )
        test_result = self.test_wizard\
            ._MedicalPathologyImport__get_el_text_array(
                test_element,
                'subelement',
            )

        self.assertEqual(test_result, ['Test Note', 'Test Note 2'])

    def test__get_remote_file_ensure_singleton(self):
        """It should raise an exception when called with multiple records"""
        test_wizard_2 = self.env['medical.pathology.import'].new()
        test_wizard_set = self.test_wizard + test_wizard_2

        with self.assertRaises(ValueError):
            test_wizard_set._MedicalPathologyImport__get_remote_file()

    @patch(S_PATH + '.medical_pathology_import.urlopen')
    def test__get_remote_file_url_helper_call(self, url_mock):
        """It should call urlopen helper with correct URI"""
        self.test_wizard._onchange_importer_type_icd10()
        url_mock().read.return_value = self.test_response
        url_mock.reset_mock()
        self.test_wizard._MedicalPathologyImport__get_remote_file()

        url_mock.assert_called_once_with(self.test_wizard.zip_uri)

    @patch(S_PATH + '.medical_pathology_import.urlopen')
    def test__get_remote_file_correct_output(self, url_mock):
        """It should correctly process response from urlopen"""
        self.test_wizard._onchange_importer_type_icd10()
        url_mock().read.return_value = self.test_response
        test_result = self.test_wizard\
            ._MedicalPathologyImport__get_remote_file()

        self.assertEqual(test_result, self.test_xml)
