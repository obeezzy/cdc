#!/bin/env python

import argparse
import os
import sqlite3
import sys
from enum import IntEnum
from collections import OrderedDict
import pyexcel_ods3 as py_ods


class ChordTone:
    def __init__(self, name):
        self.name = name.upper()
        self.note = ''

    def sharpen(self, half_steps):
        pass

    def flatten(self, half_steps):
        pass


class ChordField(IntEnum):
    CHORD_ID = 0
    NAME = 1
    NAME_ALT = 2
    SYMBOL = 3
    SYMBOL_ALT = 4
    ROOT_NOTE = 5
    NOTES = 6
    QUALITY = 7
    COMMON_TYPE = 8
    ALTERED_NOTES = 9
    ADDED_NOTES = 10
    BASS_NOTE = 11
    LH_FINGERING = 12
    RH_FINGERING = 13
    SCALE_DEGREES = 14
    MUSIC_SET = 15
    HARMONY = 16
    COMMENTS = 17
    BIMANUAL = 18
    ROOTLESS = 19


class Chord:
    def __init__(self, record):
        self.chord_id = int(record[ChordField.CHORD_ID])
        self.name = record[ChordField.NAME]
        self.name_alt = record[ChordField.NAME_ALT]
        self.symbol = record[ChordField.SYMBOL]
        self.symbol_alt = record[ChordField.SYMBOL_ALT]
        self.root_note = record[ChordField.ROOT_NOTE]
        self.notes = record[ChordField.NOTES]
        self.quality = record[ChordField.QUALITY]
        self.common_type = record[ChordField.COMMON_TYPE]
        self.altered_notes = record[ChordField.ALTERED_NOTES]
        self.added_notes = record[ChordField.ADDED_NOTES]
        self.bass_note = record[ChordField.BASS_NOTE]
        self.lh_fingering = record[ChordField.LH_FINGERING]
        self.rh_fingering = record[ChordField.RH_FINGERING]
        self.scale_degrees = record[ChordField.SCALE_DEGREES]
        self.music_set = record[ChordField.MUSIC_SET]
        self.harmony = record[ChordField.HARMONY]
        self.comments = record[ChordField.COMMENTS]
        self.bimanual = int(record[ChordField.BIMANUAL])
        self.rootless = int(record[ChordField.ROOTLESS])

    @property
    def key(self):
        return self.root_note

    @property
    def root_tone(self):
        return ChordTone(self.root_note)

    def transpose(self, half_steps):
        self.root_tone.sharpen(half_steps)

    def __iter__(self):
        yield self.chord_id
        yield self.name or ''
        yield self.name_alt or ''
        yield self.symbol or ''
        yield self.symbol_alt or ''
        yield self.root_note or ''
        yield self.notes or ''
        yield self.quality or ''
        yield self.common_type or ''
        yield self.altered_notes or ''
        yield self.added_notes or ''
        yield self.bass_note or ''
        yield self.lh_fingering or ''
        yield self.rh_fingering or ''
        yield self.scale_degrees or ''
        yield self.music_set or ''
        yield self.harmony or ''
        yield self.comments or ''
        yield self.bimanual
        yield self.rootless

    def __getitem__(self, key):
        yield 'chord_id', self.chord_id
        yield 'name', self.name
        yield 'name_alt', self.name_alt
        yield 'symbol', self.symbol
        yield 'symbol_alt', self.symbol_alt
        yield 'root_note', self.root_note
        yield 'notes', self.notes
        yield 'quality', self.quality
        yield 'common_type', self.common_type
        yield 'altered_notes', self.altered_notes
        yield 'added_notes', self.added_notes
        yield 'bass_note', self.bass_note
        yield 'lh_fingering', self.lh_fingering
        yield 'rh_fingering', self.rh_fingering
        yield 'scale_degrees', self.scale_degrees
        yield 'music_set', self.music_set
        yield 'harmony', self.harmony
        yield 'comments', self.comments
        yield 'bimanual', self.bimanual
        yield 'rootless', self.rootless

    def __repr__(self):
        return 'Chord(name=\'{}\')'.format(self.name)

    def __str__(self):
        return ('Chord(chord_id={}, '
                'name={}, '
                'name_alt={}, '
                'symbol={}, '
                'symbol_alt={}, '
                'root_note={}, '
                'notes={}, '
                'quality={}, '
                'common_type={}, '
                'altered_notes={}, '
                'added_notes={}, '
                'bass_note={}, '
                'lh_fingering={}, '
                'rh_fingering={}, '
                'scale_degrees={}, '
                'music_set={}, '
                'harmony={}, '
                'comments={}, '
                'bimanual={}, '
                'rootless={})').format(
                self.chord_id,
                self.name,
                self.name_alt,
                self.symbol,
                self.symbol_alt,
                self.root_note,
                self.notes,
                self.quality,
                self.common_type,
                self.altered_notes,
                self.added_notes,
                self.bass_note,
                self.lh_fingering,
                self.rh_fingering,
                self.scale_degrees,
                self.music_set,
                self.harmony,
                self.comments,
                self.bimanual,
                self.rootless)


class ChordDictionaryIterator:
    def __init__(self, chord_dictionary):
        self._chord_dictionary = chord_dictionary
        self._current = 0

    def __next__(self):
        if self._current < len(self._chord_dictionary.chords):
            current = self._current
            self._current += 1
            return self._chord_dictionary.chords[current]
        else:
            self._current = 0
            raise StopIteration()


class ChordDictionary:
    def __init__(self, filename=''):
        self._chords = []
        self.filename = (os.path.abspath(filename)
                         if filename and filename != ''
                         else '')

    def __iter__(self):
        return ChordDictionaryIterator(self)

    @property
    def chords(self):
        return self._chords

    def add_chord(self, chord):
        if not isinstance(chord, Chord):
            raise TypeError('Not a Chord.')
        self._chords.append(chord)

    def save(self):
        if not self.filename or self.filename == '':
            raise RuntimeError(('No file name specified for ODS document. '
                                'Unable to save ODS document.'))
        if not self.filename.endswith('.ods'):
            raise RuntimeError('Not an ODS file: {}'
                               .format(self.filename))
        records = [tuple(chord) for chord in self._chords]
        data = OrderedDict()
        data.update({'Chords': records})
        py_ods.save_data(self.filename, data)

    def load(self):
        if os.path.isfile(os.path.abspath(self.filename)):
            data = py_ods.get_data(self.filename)
            sheet_name = list(data.keys())[0]
            chord_table = data[sheet_name]
            chord_table.pop(0)  # Remove table header
            for chord_row in chord_table:
                self.add_chord(Chord(chord_row))
        elif isinstance(self.filename, str) \
                and self.filename.endswith('.ods'):
            raise RuntimeError('ODS file does not exist.')
        else:
            raise RuntimeError('ODS file does not exist.')

    def __repr__(self):
        return 'ChordDictionary({})'.format(self._chords)


class SqlDocumentIterator:
    def __init__(self, sql_document):
        self._sql_document = sql_document
        self._current = 0

    def __next__(self):
        if self._current < len(self._sql_document.statements):
            current = self._current
            self._current += 1
            return self._sql_document.statements[current]
        else:
            self._current = 0
            raise StopIteration()


class SqlDocument:
    def __init__(self, filename='', *, sql=None):
        self.filename = filename
        self._sql = (sql
                     if sql
                     else self._load(filename))

    def __iter__(self):
        return SqlDocumentIterator(self)

    def __enter__(self):
        if not self._sql or self._sql == '':
            self.begin_transaction()
            self.create_table()

    def __exit__(self, *args, **kwargs):
        self.commit()
        if self.filename and self.filename != '':
            self.save()

    @property
    def statements(self):
        return self._sql.split('\n')

    @property
    def sql(self):
        return self._sql

    def append(self, chord):
        if not isinstance(chord, Chord):
            raise TypeError('Not a Chord.')

        chord_id = chord.chord_id
        name = "'{}'".format(chord.name)
        name_alt = ("'{}'".format(chord.name_alt)
                    if chord
                    else 'NULL')
        symbol = "'{}'".format(chord.symbol)
        symbol_alt = ("'{}'".format(chord.symbol_alt)
                      if chord.symbol_alt
                      else 'NULL')
        notes = "'{}'".format(chord.notes)
        root_note = "'{}'".format(chord.root_note)
        quality = "'{}'".format(chord.quality)
        common_type = "'{}'".format(chord.common_type)
        altered_notes = "'{}'".format(chord.altered_notes)
        added_notes = "'{}'".format(chord.added_notes)
        bass_note = "'{}'".format(chord.bass_note)
        lh_fingering = "'{}'".format(chord.lh_fingering)
        rh_fingering = "'{}'".format(chord.rh_fingering)
        scale_degrees = "'{}'".format(chord.scale_degrees)
        music_set = "'{}'".format(chord.music_set)
        harmony = "'{}'".format(chord.harmony)
        comments = "'{}'".format(chord.comments)
        rootless = chord.rootless
        bimanual = chord.bimanual

        self._sql += (f'INSERT INTO "chord_dictionary" VALUES ('
                      f'{chord_id}, '
                      f'{name}, '
                      f'{name_alt}, '
                      f'{symbol}, '
                      f'{symbol_alt}, '
                      f'{root_note}, '
                      f'{notes}, '
                      f'{quality}, '
                      f'{common_type}, '
                      f'{altered_notes}, '
                      f'{added_notes}, '
                      f'{bass_note}, '
                      f'{lh_fingering}, '
                      f'{rh_fingering}, '
                      f'{scale_degrees}, '
                      f'{music_set}, '
                      f'{harmony}, '
                      f'{comments}, '
                      f'{bimanual}, '
                      f'{rootless}'
                      f');\n')

    def save(self):
        if not self.filename or self.filename == '':
            raise RuntimeError('No file name specified for SQL document. '
                               'Unable to save SQL document.')
        if not self.filename.endswith('.sql'):
            raise RuntimeError('SQL files must end with .sql')

        with open(self.filename, 'w') as f:
            f.write(self._sql)

    def commit(self):
        self._sql += 'COMMIT;\n'

    def begin_transaction(self):
        self._sql = 'BEGIN TRANSACTION;\n'

    def create_table(self):
        self._sql += ('CREATE TABLE IF NOT EXISTS "chord_dictionary" ('
                      '"id" INTEGER, '
                      '"name" TEXT NOT NULL, '
                      '"name_alt" TEXT NOT NULL, '
                      '"symbol" TEXT NOT NULL UNIQUE, '
                      '"symbol_alt" TEXT UNIQUE, '
                      '"notes" TEXT NOT NULL, '
                      '"root_note" TEXT NOT NULL, '
                      '"quality" TEXT NOT NULL, '
                      '"common_type" TEXT NOT NULL, '
                      '"altered_notes" TEXT, '
                      '"added_notes" TEXT, '
                      '"bass_note" TEXT NOT NULL, '
                      '"lh_fingering" TEXT NOT NULL, '
                      '"rh_fingering" TEXT NOT NULL, '
                      '"scale_degrees" TEXT NOT NULL, '
                      '"music_set" TEXT NOT NULL, '
                      '"harmony" TEXT NOT NULL, '
                      '"comments" TEXT NOT NULL, '
                      '"rootless" INTEGER NOT NULL DEFAULT 0, '
                      '"bimanual" INTEGER NOT NULL DEFAULT 0, '
                      'PRIMARY KEY("id" AUTOINCREMENT));\n')

    def _load(self, filename):
        if os.path.isfile(os.path.abspath(filename)):
            with open(os.path.abspath(filename)) as f:
                return f.read()
        return ''


class SqliteDatabaseIterator:
    def __init__(self, sqlite_database):
        self._sqlite_database = sqlite_database
        self._current = 0

    def __next__(self):
        if self._current < len(self._sqlite_database.records):
            current = self._current
            self._current += 1
            return self._sqlite_database.records[current]
        else:
            self._current = 0
            raise StopIteration()


class SqliteDatabase:
    def __init__(self, filename):
        filename = os.path.abspath(filename)
        self.open(filename)

    def __iter__(self):
        return SqliteDatabaseIterator(self)

    def __enter__(self):
        pass

    def __exit__(self, *args, **kwargs):
        self.close()

    @property
    def records(self):
        fetched_records = []
        if self._conn:
            for row in self._conn.execute('SELECT id AS chord_id, '
                                          'name, '
                                          'name_alt, '
                                          'symbol, '
                                          'symbol_alt, '
                                          'root_note, '
                                          'notes, '
                                          'quality, '
                                          'common_type, '
                                          'altered_notes, '
                                          'added_notes, '
                                          'bass_note, '
                                          'lh_fingering, '
                                          'rh_fingering, '
                                          'scale_degrees, '
                                          'music_set, '
                                          'harmony, '
                                          'comments, '
                                          'bimanual, '
                                          'rootless '
                                          'FROM chord_dictionary'):
                fetched_records.append(tuple(row))
        return fetched_records

    def build(self, sql_document):
        if not isinstance(sql_document, SqlDocument):
            raise TypeError('Not a SqlDocument.')
        for statement in sql_document:
            self._execute(statement.strip())

    def close(self):
        self._conn.commit()
        self._conn.close()

    def dump(self):
        sql = ''
        for line in self._conn.iterdump():
            sql += line
        return sql

    def open(self, filename):
        self._conn = sqlite3.connect(filename)
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()

    def _execute(self, statement):
        self._cursor.execute(statement)


def build_chord_dictionary(*, output_file, sql_document=None,
                           sqlite_database=None):
    if not sql_document and not sqlite_database:
        raise RuntimeError('Either SQL file or SQLite database '
                           'must be specified to build ODS document.')

    chord_dictionary = ChordDictionary(output_file)
    TEMP_DB = '/tmp/chord_dictionary.db'
    if sql_document:
        if os.path.isfile(TEMP_DB):
            os.remove(TEMP_DB)
        sqlite_database = SqliteDatabase(TEMP_DB)
        with sqlite_database:
            sqlite_database.build(sql_document)
            for record in sqlite_database:
                chord_dictionary.add_chord(Chord(record))
    elif sqlite_database:
        with sqlite_database:
            for record in sqlite_database:
                chord_dictionary.add_chord(Chord(record))

    chord_dictionary.save()


def build_sql_document(*, output_file, chord_dictionary=None,
                       sqlite_database=None):
    if not chord_dictionary and not sqlite_database:
        raise RuntimeError('Either ODS file or SQLite database '
                           'must be specified to build SQL file.')

    sql_document = SqlDocument(output_file)
    if chord_dictionary:
        chord_dictionary.load()
        with sql_document:
            for chord in chord_dictionary:
                sql_document.append(chord)
    elif sqlite_database:
        with sqlite_database:
            sql = sqlite_database.dump()
            sql_document = SqlDocument(output_file, sql=sql)

    sql_document.save()


def build_sqlite_database(*, output_file, chord_dictionary=None,
                          sql_document=None):
    if not chord_dictionary and not sql_document:
        raise RuntimeError('Either ODS file or SQL file '
                           'must be specified to build SQLite database.')

    sqlite_database = SqliteDatabase(output_file)
    with sqlite_database:
        if chord_dictionary:
            chord_dictionary.load()
            sql_document = SqlDocument()
            with sql_document:
                for chord in chord_dictionary:
                    sql_document.append(chord)

        sqlite_database.build(sql_document)


# FIXME: Too complex?
def main():  # noqa
    parser = argparse.ArgumentParser(description='Chord Dictionary Creator')
    parser.add_argument('-i', '--input', type=str, required=True,
                        help='Input file (ODS, SQL, SQLITE)')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='Output file (ODS, SQL, SQLITE)')

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()

    try:
        input_file = args.input
        output_file = args.output

        if not input_file:
            raise ValueError('No input file specified.')
        if not output_file:
            raise ValueError('No output file specified.')

        chord_dictionary = (ChordDictionary(input_file)
                            if input_file.endswith('.ods')
                            else None)
        sql_document = (SqlDocument(input_file)
                        if input_file.endswith('.sql')
                        else None)
        sqlite_database = (SqliteDatabase(input_file)
                           if input_file.endswith('.db')
                           else None)

        if output_file.endswith('.ods'):
            build_chord_dictionary(sql_document=sql_document,
                                   sqlite_database=sqlite_database,
                                   output_file=output_file)
        elif output_file.endswith('.sql'):
            build_sql_document(chord_dictionary=chord_dictionary,
                               sqlite_database=sqlite_database,
                               output_file=output_file)
        elif output_file.endswith('.db'):
            build_sqlite_database(sql_document=sql_document,
                                  chord_dictionary=chord_dictionary,
                                  output_file=output_file)
        elif not chord_dictionary and not sql_document \
                and not sqlite_database:
            raise ValueError('Invalid input format. '
                             'Valid formats: .ods, .sql, .db')
        else:
            raise ValueError('Invalid output format. '
                             'Valid formats: .ods, .sql, .db')
    except ValueError as e:
        print('ERROR: {}'.format(e), file=sys.stderr)
        parser.print_help()
        raise
    except RuntimeError as e:
        print(e, file=sys.stderr)
        raise


if __name__ == '__main__':
    main()
