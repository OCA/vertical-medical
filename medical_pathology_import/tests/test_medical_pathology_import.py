# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import mock
import os

from openerp.tests.common import TransactionCase


MODULE_PATH = '.'.join((
    'openerp.addons.medical_pathology_import',
    'wizards.medical_pathology_import',
))


class TestMedicaPathologyImport(TransactionCase):

    TEST_ZIP = os.path.join(
        os.path.dirname(__file__),
        'test_zip.zip'
    )
    TEST_FILE = 'test.txt'
    TEST_FILE_CONTENT = 'test'

    def setUp(self):
        super(TestMedicaPathologyImport, self).setUp()
        self.Model = self.env['medical.pathology.import']
        self.code_type = self.env.ref(
            'medical_pathology.pathology_code_05',
        )

    @mock.patch('%s.MedicalPathologyImport._get_importer_types' % MODULE_PATH)
    @mock.patch('%s.MedicalPathologyImport.do_import' % MODULE_PATH)
    def create_record(self, do_import, _get_importer_types):
        self._get_importer_types = _get_importer_types
        self.do_import = do_import
        _get_importer_types.return_value = [('test', 'Test Type')]
        return self.Model.create({
            'code_type_id': self.code_type.id,
            'importer_type': 'test',
            'file_name': self.TEST_FILE,
            'zip_uri': self.TEST_ZIP,
        })

    def create_category(self, parent=None):
        return self.env['medical.pathology.category'].create({
            'code_type_id': self.code_type.id,
            'name': 'Category',
            'parent_id': parent.id if parent else None,
            'note': 'Category Notes',
        })

    def _get_pathology_args(self, parent=None, category=None):
        if not category:
            category = self.create_category()
        return {
            'name': 'Name',
            'code': 'Code',
            'category': category,
            'code_type': self.code_type,
            'parent': parent,
            'note': 'Pathology Note',
        }

    def _get_pathology_category_args(self, parent=None):
        return {
            'name': 'Name',
            'code_type': self.code_type,
            'ref': 'Ref',
            'parent': parent,
            'note': 'Category Note',
        }

    def test_module_name(self):
        """ It should return proper base name for modules """
        self.assertEqual(
            self.Model.module_name, 'medical_pathology_'
        )

    def test_get_importer_types(self):
        """ It should return empty list """
        self.assertEqual(
            self.Model._get_importer_types(), [],
        )

    def test_onchange_importer_type_child(self):
        """ It should call child importer onchange """
        record = self.create_record()
        method = mock.MagicMock()
        record._onchange_importer_type_test = method
        record._onchange_importer_type()
        method.assert_called_once_with()

    def test_onchange_importer_type(self):
        """ It should null fields out when no child importer """
        record = self.create_record()
        vals = {
            'zip_uri': 'uri',
            'file_name': 'name',
        }
        record.write(vals)
        record._onchange_importer_type()
        for key in vals.keys():
            self.assertFalse(record[key])

    def test_create_calls_import(self):
        """ It should call do_import on new record """
        self.create_record()
        self.do_import.assert_called_once_with()

    def test_create_returns_record(self):
        """ It should return newly created record """
        record = self.create_record()
        self.assertTrue(record.exists())

    def test_do_import_calls_child(self):
        """ It should call child import method for type """
        record = self.create_record()
        setattr(record, 'do_import_test', mock.MagicMock())
        record.do_import()
        record.do_import_test.assert_called_once_with()

    def test_get_pathology_xml_id(self):
        """ It should return properly formatted XML id """
        record = self.create_record()
        self.assertEqual(
            record._get_pathology_xml_id('A00.01'),
            'medical_pathology_A00_01',
        )

    def test_get_pathology_category_xml_id(self):
        """ It should return properly formatted XML id """
        record = self.create_record()
        self.assertEqual(
            record._get_pathology_category_xml_id('A00-B01'),
            'medical_pathology_category_A00_B01',
        )

    def test_upsert_pathology_inserts(self):
        """ It should create new pathology if not existing """
        record = self.create_record()
        args = self._get_pathology_args()
        pathology = record._upsert_pathology(**args)
        self.assertTrue(pathology.exists())

    def test_upsert_pathology_xml_id(self):
        """ It should create a new ir.model.data record for new pathology """
        record = self.create_record()
        args = self._get_pathology_args()
        pathology = record._upsert_pathology(**args)
        self.assertEqual(
            self.env['ir.model.data'].get_object(
                self.Model.module_name,
                'medical_pathology_Code',
            ),
            pathology,
        )

    def test_upsert_pathology_update(self):
        """ It should update existing pathology if existing """
        record = self.create_record()
        args = self._get_pathology_args()
        pathology = record._upsert_pathology(**args)
        args['name'] = 'New Name'
        record._upsert_pathology(**args)
        self.assertEqual(
            pathology.name, args['name'],
        )

    def test_upsert_pathology_category_inserts(self):
        """ It should create new pathology if not existing """
        record = self.create_record()
        args = self._get_pathology_category_args()
        category = record._upsert_pathology_category(**args)
        self.assertTrue(category.exists())

    def test_upsert_pathology_category_xml_id(self):
        """ It should create a new ir.model.data record for new pathology """
        record = self.create_record()
        args = self._get_pathology_category_args()
        category = record._upsert_pathology_category(**args)
        self.assertEqual(
            self.env['ir.model.data'].get_object(
                self.Model.module_name,
                'medical_pathology_category_Ref',
            ),
            category,
        )

    def test_upsert_pathology_category_update(self):
        """ It should update existing pathology if existing """
        record = self.create_record()
        args = self._get_pathology_category_args()
        category = record._upsert_pathology_category(**args)
        args['name'] = 'New Name'
        record._upsert_pathology_category(**args)
        self.assertEqual(
            category.name, args['name'],
        )

    @mock.patch('%s.urlopen' % MODULE_PATH)
    def test_get_remote_file(self, urlopen):
        """ It should extract and return the correct file. """
        record = self.create_record()
        with open(self.TEST_ZIP) as fh:
            urlopen().read.return_value = fh.read()
        res = record._get_remote_file()
        self.assertEqual(res, self.TEST_FILE_CONTENT)
