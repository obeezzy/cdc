from cdc import SqlDocument, \
                SqliteDatabase, \
                ChordDictionary, \
                Chord

_RECORDS = [
    [1, 'C major', '', 'C', '', 'C', 'C E G', 'major', 'triad', '', '', 'C', '5 3 1', '1 3 5', '1 3 5', 'triad', 'close', 'root position', 0, 0],  # noqa
    [2, 'C major seventh', '', 'Cmaj7', 'CM7', 'C', 'C E G B', 'major', 'seventh', '', '', 'C', '5 3 2 1', '1 2 3 5', '1 3 5 7', 'tetrad', 'close', 'root position', 0, 0],  # noqa
    [3, 'C seventh minus five', 'C seventh flat five', 'C7-5', 'C7b5', 'C', 'C E Gb Bb', 'major', 'seventh', 'Gb', '', 'C', '5 3 2 1', '1 2 3 5', '1 3 b5 b7', 'tetrad', 'close', 'root position', 0, 0] # noqa
]


class DummyChordDictionary(ChordDictionary):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._populate()
        self.save()

    def _populate(self):
        for record in _RECORDS:
            self.add_chord(Chord(record))


class DummySqlDocument(SqlDocument):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._populate()
        self.save()

    def _populate(self):
        self.begin_transaction()
        self.create_table()
        for record in _RECORDS:
            self.append(Chord(record))
        self.commit()
        self.save()


class DummySqliteDatabase(SqliteDatabase):
    pass
