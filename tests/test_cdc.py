#!/bin/env python

import os
import unittest
import subprocess
import shutil
from cdc import SqlDocument, SqliteDatabase, ChordDictionary
from tests.dummy_cdc import DummySqlDocument, \
                            DummySqliteDatabase, \
                            DummyChordDictionary


class TestCdc(unittest.TestCase):
    def setUp(self):
        self.input_ods = 'tests/resources/chord_dictionary.ods'
        self.input_sql = 'tests/resources/chord_dictionary.sql'
        self.input_sqlite = 'tests/resources/chord_dictionary.db'
        self.output_ods = 'tests/artifacts/chord_dictionary.ods'
        self.output_sql = 'tests/artifacts/chord_dictionary.sql'
        self.output_sqlite = 'tests/artifacts/chord_dictionary.db'
        self.resource_dir = os.path.abspath('tests/resources')
        self.artifact_dir = os.path.abspath('tests/artifacts')

        if not os.path.isdir(self.resource_dir):
            os.makedirs(self.resource_dir)

        self.dummy_chord_dictionary = DummyChordDictionary(self.input_ods)
        self.dummy_sql_document = DummySqlDocument(self.input_sql)
        self.dummy_sqlite_database = DummySqliteDatabase(self.input_sqlite)
        with self.dummy_sqlite_database:
            self.dummy_sqlite_database.build(self.dummy_sql_document)

        if not os.path.isdir(self.artifact_dir):
            os.makedirs(self.artifact_dir)

    def tearDown(self):
        if os.path.isdir(self.resource_dir):
            shutil.rmtree(self.resource_dir)
        if os.path.isdir(self.artifact_dir):
            shutil.rmtree(self.artifact_dir)

    def test_ods_to_sql(self):
        completed_process = subprocess.run(['./cdc.py',
                                            '-i', self.input_ods,
                                            '-o', self.output_sql])
        self.assertEqual(completed_process.returncode, 0,
                         'Failed to convert ODS to SQL.')
        self.assertTrue(os.path.isfile(self.output_sql),
                        'Failed to create SQL file.')
        sql_document = SqlDocument(self.output_sql)
        sqlite_database = SqliteDatabase(self.output_sqlite)
        with sqlite_database:
            sqlite_database.build(sql_document)
            records_exist = (True
                             if len(sqlite_database.records)
                             else False)
            self.assertTrue(records_exist, 'Failed to populate SQLite database.')  # noqa

    def test_ods_to_sqlite(self):
        completed_process = subprocess.run(['./cdc.py',
                                            '-i', self.input_ods,
                                            '-o', self.output_sqlite])
        self.assertEqual(completed_process.returncode, 0,
                         'Failed to convert ODS to SQL.')
        self.assertTrue(os.path.isfile(self.output_sqlite),
                        'Failed to create SQL file.')
        sqlite_database = SqliteDatabase(self.output_sqlite)
        with sqlite_database:
            records_exist = (True
                             if len(sqlite_database.records)
                             else False)
            self.assertTrue(records_exist, 'Failed to populate SQLite database.')  # noqa

    def test_sql_to_ods(self):
        completed_process = subprocess.run(['./cdc.py',
                                            '-i', self.input_sql,
                                            '-o', self.output_ods])
        self.assertEqual(completed_process.returncode, 0,
                         'Failed to convert ODS to SQL.')
        self.assertTrue(os.path.isfile(self.output_ods),
                        'Failed to create ODS file.')
        sql_document = SqlDocument(self.input_sql)
        sqlite_database = SqliteDatabase(self.output_sqlite)
        with sqlite_database:
            sqlite_database.build(sql_document)
            records_exist = (True
                             if len(sqlite_database.records)
                             else False)
            self.assertTrue(records_exist, 'No records in SQLite database.')

    def test_sql_to_sqlite(self):
        completed_process = subprocess.run(['./cdc.py',
                                            '-i', self.input_sql,
                                            '-o', self.output_sqlite])
        self.assertEqual(completed_process.returncode, 0,
                         'Failed to convert ODS to SQLite database.')
        self.assertTrue(os.path.isfile(self.output_sqlite),
                        'Failed to create SQLite database.')
        sql_document = SqlDocument(self.output_sql)
        sqlite_database = SqliteDatabase(self.output_sqlite)
        with sqlite_database:
            sqlite_database.build(sql_document)
            records_exist = (True
                             if len(sqlite_database.records)
                             else False)
            self.assertTrue(records_exist, 'No records in SQLite database.')

    def test_sqlite_to_ods(self):
        completed_process = subprocess.run(['./cdc.py',
                                            '-i', self.input_sqlite,
                                            '-o', self.output_ods])
        self.assertEqual(completed_process.returncode, 0,
                         'Failed to convert SQLite database to ODS.')
        self.assertTrue(os.path.isfile(self.output_ods),
                        'Failed to create ODS file.')
        chord_dictionary = ChordDictionary(self.output_ods)
        chord_dictionary.load()
        records_exist = (True
                         if len(chord_dictionary.chords)
                         else False)
        self.assertTrue(records_exist, 'No records in ODS file.')

    def test_sqlite_to_sql(self):
        completed_process = subprocess.run(['./cdc.py',
                                            '-i', self.input_sqlite,
                                            '-o', self.output_sql])
        self.assertEqual(completed_process.returncode, 0,
                         'Failed to convert SQLite database to SQL.')
        self.assertTrue(os.path.isfile(self.output_sql),
                        'Failed to create SQL file.')
        sql_document = SqlDocument(self.output_sql)
        records_exist = (True
                         if len(sql_document.statements)
                         else False)
        self.assertTrue(records_exist, 'No records in SQL file.')


if __name__ == '__main__':
    unittest.main()
