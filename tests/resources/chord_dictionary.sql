BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "chord_dictionary" ("id" INTEGER, "name" TEXT NOT NULL, "name_alt" TEXT NOT NULL, "symbol" TEXT NOT NULL UNIQUE, "symbol_alt" TEXT UNIQUE, "notes" TEXT NOT NULL, "root_note" TEXT NOT NULL, "quality" TEXT NOT NULL, "common_type" TEXT NOT NULL, "altered_notes" TEXT, "added_notes" TEXT, "bass_note" TEXT NOT NULL, "lh_fingering" TEXT NOT NULL, "rh_fingering" TEXT NOT NULL, "scale_degrees" TEXT NOT NULL, "music_set" TEXT NOT NULL, "harmony" TEXT NOT NULL, "comments" TEXT NOT NULL, "rootless" INTEGER NOT NULL DEFAULT 0, "bimanual" INTEGER NOT NULL DEFAULT 0, PRIMARY KEY("id" AUTOINCREMENT));
INSERT INTO "chord_dictionary" VALUES (1, 'C major', '', 'C', NULL, 'C', 'C E G', 'major', 'triad', '', '', 'C', '5 3 1', '1 3 5', '1 3 5', 'triad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (2, 'C major seventh', '', 'Cmaj7', 'CM7', 'C', 'C E G B', 'major', 'seventh', '', '', 'C', '5 3 2 1', '1 2 3 5', '1 3 5 7', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (3, 'C sixth', '', 'C6', NULL, 'C', 'C E G A', 'major', 'added note', '', 'A', 'C', '5 3 2 1', '1 2 3 5', '1 3 5 6', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (4, 'C major sixth/ninth', 'C major sixth added ninth', 'C6/9', NULL, 'C', 'C E G A D', 'major', 'added note', '', 'A D', 'C', '5 4 3 2 1', '1 2 3 4 5', '1 3 5 6 9', 'pentad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (5, 'C major ninth', '', 'Cmaj9', 'CM9', 'C', 'C E G B D', 'major', 'extended', '', '', 'C', '5 4 3 2 1', '1 2 3 4 5', '1 3 5 7 9', 'pentad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (6, 'C minor', '', 'Cmin', 'Cm', 'C', 'C Eb G', 'minor', 'triad', '', '', 'C', '5 3 1', '1 3 5', '1 b3 5', 'triad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (7, 'C minor seventh', '', 'Cmin7', 'Cm7', 'C', 'C Eb G Bb', 'minor', 'seventh', '', '', 'C', '5 3 2 1', '1 2 3 5', '1 b3 5 b7', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (8, 'C minor sixth', '', 'Cmin6', 'Cm6', 'C', 'C Eb G A', 'minor', 'added note', '', 'A', 'C', '5 3 2 1', '1 2 3 5', '1 b3 5 6', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (9, 'C minor sixth/ninth', 'C minor sixth added ninth', 'Cmin6/9', 'Cm6/9', 'C', 'C Eb G A D', 'minor', 'added note', '', 'A D', 'C', '5 4 3 2 1', '1 2 3 4 5', '1 b3 5 6 9', 'pentad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (10, 'C minor ninth', '', 'Cmin9', 'Cm9', 'C', 'C Eb G Bb D', 'minor', 'extended', '', '', 'C', '5 4 3 2 1', '1 2 3 4 5', '1 b3 5 b7 9', 'pentad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (11, 'C minor eleventh', '', 'Cmin11', 'Cm11', 'C', 'C Eb G Bb D F', 'minor', 'extended', '', '', 'C', '5 3 2 1', '1 3', '1 b3 5 b7 9 11', 'hexad', 'close', 'root position', 1, 0);
INSERT INTO "chord_dictionary" VALUES (12, 'C minor major seventh', '', 'CminM7', 'CmM7', 'C', 'C Eb G B', 'minor', 'seventh', '', '', 'C', '5 3 2 1', '1 2 3 5', '1 b3 5 7', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (13, 'C seventh', 'C dominant seventh', 'C7', NULL, 'C', 'C E G Bb', 'major', 'seventh', '', '', 'C', '5 3 2 1', '1 2 3 5', '1 3 5 b7', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (14, 'C ninth', 'C dominant ninth', 'C9', NULL, 'C', 'C E G Bb D', 'major', 'extended', '', '', 'C', '5 4 3 2 1', '1 2 3 4 5', '1 3 5 b7 9', 'pentad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (15, 'C eleventh', 'C dominant eleventh', 'C11', NULL, 'C', 'C E G Bb D F', 'major', 'extended', '', '', 'C', '5 3 2 1', '1 3', '1 3 5 b7 9 11', 'hexad', 'close', 'root position', 1, 0);
INSERT INTO "chord_dictionary" VALUES (16, 'C diminished', '', 'Cdim', NULL, 'C', 'C Eb Gb', 'diminished', 'triad', '', '', 'C', '5 3 2', '1 2 3', '1 b3 b5', 'triad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (17, 'C diminished seventh', '', 'Cdim7', NULL, 'C', 'C Eb Gb A', 'diminished', 'seventh', '', '', 'C', '5 3 2 1', '1 2 3 5', '1 b3 b5 6', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (18, 'C half diminished ', 'C minor seventh flat five', 'Cm7b5', NULL, 'C', 'C Eb Gb Bb', 'diminished', 'seventh', '', '', 'C', '5 3 2 1', '1 2 3 5', '1 b3 b5 b7', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (19, 'C augmented', '', 'Caug', NULL, 'C', 'C E G#', 'augmented', 'triad', '', '', 'C', '5 3 1', '1 3 5', '1 3 #5', 'triad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (20, 'C augmented seventh', '', 'Caug7', NULL, 'C', 'C E G# Bb', 'augmented', 'seventh', '', '', 'C', '5 3 2 1', '1 2 3 5', '1 3 #5 b7', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (21, 'C seventh minus five', 'C seventh flat five', 'C7-5', 'C7b5', 'C', 'C E Gb Bb', 'seventh', 'seventh', 'Gb', '', 'C', '5 3 2 1', '1 2 3 5', '1 3 b5 b7', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (22, 'C seventh plus five', 'C seventh sharp five', 'C7+5', 'C7#5', 'C', 'C E G# Bb', 'seventh', 'seventh', 'G#', '', 'C', '5 3 2 1', '1 2 3 5', '1 3 #5 b7', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (23, 'C seventh minus nine', 'C seventh flat nine', 'C7-9', 'C7b9', 'C', 'C E G Bb Db', 'seventh', 'seventh', 'Db', '', 'C', '5 3 2 1', '2', '1 3 5 b7 b9', 'pentad', 'close', 'root position', 1, 0);
INSERT INTO "chord_dictionary" VALUES (24, 'C seventh plus nine', 'C seventh sharp nine', 'C7+9', 'C7#9', 'C', 'C E G Bb D#', 'seventh', 'seventh', 'D#', '', 'C', '5 3 2 1', '2', '1 3 5 b7 #9', 'pentad', 'close', 'root position', 1, 0);
INSERT INTO "chord_dictionary" VALUES (25, 'C seventh sharp eleventh', '', 'C7#11', NULL, 'C', 'C E G Bb F#', 'seventh', 'added tone', '', 'F#', 'C', '5 3 2 1', '2', '1 3 5 b7 #11', 'pentad', 'close', 'root position', 1, 0);
INSERT INTO "chord_dictionary" VALUES (26, 'C five', '', 'C5', 'Cno3', 'C', 'C G', 'perfect fifth', 'power', '', '', 'C', '5 1', '1 5', '1 5', 'dyad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (27, 'C add nine', '', 'Cadd9', 'Cadd', 'C', 'C E G D', 'major', 'added note', '', 'D', 'C', '5 3 2 1', '1 2 3 5', '1 3 5 9', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (28, 'C add second', '', 'Cadd2', NULL, 'C', 'C D E G', 'major', 'added note', '', 'D', 'C', '5 3 2 1', '1 2 3 5', '1 2 3 5', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (29, 'C add eleven', '', 'Cadd11', NULL, 'C', 'C E G F', 'major', 'added note', '', 'F', 'C', '5 3 1', '1', '1 3 5 11', 'tetrad', 'close', 'root position', 1, 0);
INSERT INTO "chord_dictionary" VALUES (30, 'C add four', '', 'Cadd4', NULL, 'C', 'C E F G', 'major', 'added note', '', 'F', 'C', '5 3 2 1', '1 2 3 5', '1 3 4 5', 'tetrad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (31, 'C suspended fourth', '', 'Csus4', NULL, 'C', 'C F G', 'major', 'suspended', '', '', 'C', '5 2 1', '1 2 3', '1 4 5', 'triad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (32, 'C suspended second', '', 'Csus2', NULL, 'C', 'C D G', 'major', 'suspended', '', '', 'C', '5 4 1', '1 2 5', '1 2 5', 'triad', 'close', 'root position', 0, 0);
INSERT INTO "chord_dictionary" VALUES (33, 'C major thirteenth', '', 'Cmaj13', 'CM13', 'C', 'C E G B D A', 'seventh', 'extended', '', '', 'C', '5 3 2 1', '1 5', '1 3 5 7 9 13', 'hexad', 'close', 'root position', 1, 0);
INSERT INTO "chord_dictionary" VALUES (34, 'C thirteenth', 'C dominant thirteeth', 'C13', NULL, 'C', 'C E G Bb D A', 'seventh', 'extended', '', '', 'C', '5 3 2 1', '1 5', '1 3 5 b7 9 13', 'hexad', 'close', 'root position', 1, 0);
COMMIT;