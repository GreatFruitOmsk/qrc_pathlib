import unittest

from qrc_pathlib import qrc_glob

from test import fixture


class TestQrcGlob(unittest.TestCase):
    def test_iglob_with_files(self):
        self.assertEqual(set(qrc_glob.iglob(':привет.txt')), {':/привет.txt'})
        self.assertEqual(set(qrc_glob.iglob(':привет.txt/')), set())

    def test_iglob_with_dirs(self):
        self.assertEqual(set(qrc_glob.iglob(':dir')), {':/dir'})
        self.assertEqual(set(qrc_glob.iglob(':dir/')), {':/dir'})

    def test_iglob_pattern(self):
        self.assertEqual(set(qrc_glob.iglob(':*.txt')), {':/привет.txt', ':/42.txt'})
        self.assertEqual(set(qrc_glob.iglob(':[0-9][0-9].txt')), {':/42.txt'})

    def test_iglob_dir_pattern(self):
        self.assertEqual(set(qrc_glob.iglob(':/dir/*.txt')), {':/dir/1.txt', ':/dir/2.txt'})

    def test_iglob_recursive_pattern(self):
        self.assertEqual(set(qrc_glob.iglob(':/**/*.txt')), {':/dir/1.txt', ':/dir/2.txt'})
        self.assertEqual(set(qrc_glob.iglob(':/**/*.txt', recursive=True)), {':/dir/1.txt', ':/dir/2.txt', ':/привет.txt', ':/42.txt'})
