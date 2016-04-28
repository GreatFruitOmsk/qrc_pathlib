import unittest

from qrc_pathlib import PureQrcPath


class TestPureQrcPath(unittest.TestCase):
    def test_anchor(self):
        self.assertEqual(PureQrcPath().anchor, '')
        self.assertEqual(PureQrcPath('').anchor, '')
        self.assertEqual(PureQrcPath(':').anchor, ':/')
        self.assertEqual(PureQrcPath(':/').anchor, ':/')
        self.assertEqual(PureQrcPath(':/a/b/c').anchor, ':/')
        self.assertEqual(PureQrcPath('a/b/c').anchor, '')
        self.assertEqual(PureQrcPath('a').anchor, '')

    def test_drive(self):
        self.assertEqual(PureQrcPath().drive, '')
        self.assertEqual(PureQrcPath('').drive, '')
        self.assertEqual(PureQrcPath(':').drive, '')
        self.assertEqual(PureQrcPath(':/').drive, '')
        self.assertEqual(PureQrcPath(':/a/b/c').drive, '')
        self.assertEqual(PureQrcPath('a/b/c').drive, '')
        self.assertEqual(PureQrcPath('a').drive, '')

    def test_root(self):
        self.assertEqual(PureQrcPath().root, '')
        self.assertEqual(PureQrcPath('').root, '')
        self.assertEqual(PureQrcPath(':').root, ':/')
        self.assertEqual(PureQrcPath(':/').root, ':/')
        self.assertEqual(PureQrcPath(':/a/b/c').root, ':/')
        self.assertEqual(PureQrcPath('a/b/c').root, '')
        self.assertEqual(PureQrcPath('a').root, '')

    def test_parents(self):
        self.assertEqual(list(PureQrcPath().parents), [])
        self.assertEqual(list(PureQrcPath('').parents), [])
        self.assertEqual(list(PureQrcPath(':').parents), [])
        self.assertEqual(list(PureQrcPath(':/').parents), [])
        self.assertEqual(list(PureQrcPath(':/a/b/c').parents), [PureQrcPath(':/a/b'), PureQrcPath(':/a'), PureQrcPath(':/')])
        self.assertEqual(list(PureQrcPath('a/b/c').parents), [PureQrcPath('a/b'), PureQrcPath('a'), PureQrcPath('.')])
        self.assertEqual(list(PureQrcPath('a').parents), [PureQrcPath('.')])

    def test_parent(self):
        self.assertEqual(PureQrcPath().parent, PureQrcPath('.'))
        self.assertEqual(PureQrcPath('').parent, PureQrcPath('.'))
        self.assertEqual(PureQrcPath(':').parent, PureQrcPath(':/'))
        self.assertEqual(PureQrcPath(':/').parent, PureQrcPath(':/'))
        self.assertEqual(PureQrcPath(':/a/b/c').parent, PureQrcPath(':/a/b'))
        self.assertEqual(PureQrcPath('a/b/c').parent, PureQrcPath('a/b'))
        self.assertEqual(PureQrcPath('a').parent, PureQrcPath('.'))

    def test_name(self):
        self.assertEqual(PureQrcPath().name, '')
        self.assertEqual(PureQrcPath('').name, '')
        self.assertEqual(PureQrcPath(':').name, '')
        self.assertEqual(PureQrcPath(':/').name, '')
        self.assertEqual(PureQrcPath(':/a/b/c').name, 'c')
        self.assertEqual(PureQrcPath('a/b/c').name, 'c')
        self.assertEqual(PureQrcPath('a').name, 'a')

    def test_suffix(self):
        self.assertEqual(PureQrcPath().suffix, '')
        self.assertEqual(PureQrcPath('').suffix, '')
        self.assertEqual(PureQrcPath(':').suffix, '')
        self.assertEqual(PureQrcPath(':/').suffix, '')
        self.assertEqual(PureQrcPath(':/a/b/c').suffix, '')
        self.assertEqual(PureQrcPath(':/a/b/.c').suffix, '')
        self.assertEqual(PureQrcPath(':/a/b/.c.d').suffix, '.d')
        self.assertEqual(PureQrcPath(':/a/b/.c.d.e').suffix, '.e')
        self.assertEqual(PureQrcPath(':/a/b/c.d').suffix, '.d')
        self.assertEqual(PureQrcPath(':/a/b/c.d.e').suffix, '.e')
        self.assertEqual(PureQrcPath('a/b/c').suffix, '')
        self.assertEqual(PureQrcPath('a/b/.c').suffix, '')
        self.assertEqual(PureQrcPath('a/b/.c').suffix, '')
        self.assertEqual(PureQrcPath('a/b/.c.d').suffix, '.d')
        self.assertEqual(PureQrcPath('a/b/.c.d.e').suffix, '.e')
        self.assertEqual(PureQrcPath('a/b/c.d').suffix, '.d')
        self.assertEqual(PureQrcPath('a/b/c.d.e').suffix, '.e')
        self.assertEqual(PureQrcPath('a').suffix, '')
        self.assertEqual(PureQrcPath('.a').suffix, '')
        self.assertEqual(PureQrcPath('.a.b').suffix, '.b')
        self.assertEqual(PureQrcPath('.a.b.c').suffix, '.c')
        self.assertEqual(PureQrcPath('a.b').suffix, '.b')
        self.assertEqual(PureQrcPath('a.b.c').suffix, '.c')

    def test_suffixes(self):
        self.assertEqual(PureQrcPath().suffixes, [])
        self.assertEqual(PureQrcPath('').suffixes, [])
        self.assertEqual(PureQrcPath(':').suffixes, [])
        self.assertEqual(PureQrcPath(':/').suffixes, [])
        self.assertEqual(PureQrcPath(':/a/b/c').suffixes, [])
        self.assertEqual(PureQrcPath(':/a/b/.c').suffixes, [])
        self.assertEqual(PureQrcPath(':/a/b/.c.d').suffixes, ['.d'])
        self.assertEqual(PureQrcPath(':/a/b/.c.d.e').suffixes, ['.d', '.e'])
        self.assertEqual(PureQrcPath(':/a/b/c.d').suffixes, ['.d'])
        self.assertEqual(PureQrcPath(':/a/b/c.d.e').suffixes, ['.d', '.e'])
        self.assertEqual(PureQrcPath('a/b/c').suffixes, [])
        self.assertEqual(PureQrcPath('a/b/.c').suffixes, [])
        self.assertEqual(PureQrcPath('a/b/.c').suffixes, [])
        self.assertEqual(PureQrcPath('a/b/.c.d').suffixes, ['.d'])
        self.assertEqual(PureQrcPath('a/b/.c.d.e').suffixes, ['.d', '.e'])
        self.assertEqual(PureQrcPath('a/b/c.d').suffixes, ['.d'])
        self.assertEqual(PureQrcPath('a/b/c.d.e').suffixes, ['.d', '.e'])
        self.assertEqual(PureQrcPath('a').suffixes, [])
        self.assertEqual(PureQrcPath('.a').suffixes, [])
        self.assertEqual(PureQrcPath('.a.b').suffixes, ['.b'])
        self.assertEqual(PureQrcPath('.a.b.c').suffixes, ['.b', '.c'])
        self.assertEqual(PureQrcPath('a.b').suffixes, ['.b'])
        self.assertEqual(PureQrcPath('a.b.c').suffixes, ['.b', '.c'])

    def test_stem(self):
        self.assertEqual(PureQrcPath().stem, '')
        self.assertEqual(PureQrcPath('').stem, '')
        self.assertEqual(PureQrcPath(':').stem, '')
        self.assertEqual(PureQrcPath(':/').stem, '')
        self.assertEqual(PureQrcPath(':/a/b/c').stem, 'c')
        self.assertEqual(PureQrcPath(':/a/b/.c').stem, '.c')
        self.assertEqual(PureQrcPath(':/a/b/.c.d').stem, '.c')
        self.assertEqual(PureQrcPath(':/a/b/.c.d.e').stem, '.c.d')
        self.assertEqual(PureQrcPath(':/a/b/c.d').stem, 'c')
        self.assertEqual(PureQrcPath(':/a/b/c.d.e').stem, 'c.d')
        self.assertEqual(PureQrcPath('a/b/c').stem, 'c')
        self.assertEqual(PureQrcPath('a/b/.c').stem, '.c')
        self.assertEqual(PureQrcPath('a/b/.c').stem, '.c')
        self.assertEqual(PureQrcPath('a/b/.c.d').stem, '.c')
        self.assertEqual(PureQrcPath('a/b/.c.d.e').stem, '.c.d')
        self.assertEqual(PureQrcPath('a/b/c.d').stem, 'c')
        self.assertEqual(PureQrcPath('a/b/c.d.e').stem, 'c.d')
        self.assertEqual(PureQrcPath('a').stem, 'a')
        self.assertEqual(PureQrcPath('.a').stem, '.a')
        self.assertEqual(PureQrcPath('.a.b').stem, '.a')
        self.assertEqual(PureQrcPath('.a.b.c').stem, '.a.b')
        self.assertEqual(PureQrcPath('a.b').stem, 'a')
        self.assertEqual(PureQrcPath('a.b.c').stem, 'a.b')

    def test_as_posix(self):
        self.assertEqual(PureQrcPath().as_posix(), '.')
        self.assertEqual(PureQrcPath('').as_posix(), '.')
        self.assertEqual(PureQrcPath(':').as_posix(), ':/')
        self.assertEqual(PureQrcPath(':/').as_posix(), ':/')
        self.assertEqual(PureQrcPath(':/a/b/c').as_posix(), ':/a/b/c')
        self.assertEqual(PureQrcPath('a/b/c').as_posix(), 'a/b/c')
        self.assertEqual(PureQrcPath('a').as_posix(), 'a')

    def test_as_uri(self):
        with self.assertRaises(ValueError):
            PureQrcPath().as_uri()

        with self.assertRaises(ValueError):
            PureQrcPath('').as_uri()

        self.assertEqual(PureQrcPath(':').as_uri(), 'qrc:/')
        self.assertEqual(PureQrcPath(':/').as_uri(), 'qrc:/')
        self.assertEqual(PureQrcPath(':/a/b/c').as_uri(), 'qrc:/a/b/c')

        with self.assertRaises(ValueError):
            PureQrcPath('a/b/c').as_uri()

        with self.assertRaises(ValueError):
            PureQrcPath('a').as_uri()

    def test_is_absolute(self):
        self.assertEqual(PureQrcPath().is_absolute(), False)
        self.assertEqual(PureQrcPath('').is_absolute(), False)
        self.assertEqual(PureQrcPath(':').is_absolute(), True)
        self.assertEqual(PureQrcPath(':/').is_absolute(), True)
        self.assertEqual(PureQrcPath(':/a/b/c').is_absolute(), True)
        self.assertEqual(PureQrcPath('a/b/c').is_absolute(), False)
        self.assertEqual(PureQrcPath('a').is_absolute(), False)

    def test_is_reserved(self):
        self.assertEqual(PureQrcPath().is_reserved(), False)
        self.assertEqual(PureQrcPath('').is_reserved(), False)
        self.assertEqual(PureQrcPath(':').is_reserved(), False)
        self.assertEqual(PureQrcPath(':/').is_reserved(), False)
        self.assertEqual(PureQrcPath(':/a/b/c').is_reserved(), False)
        self.assertEqual(PureQrcPath('a/b/c').is_reserved(), False)
        self.assertEqual(PureQrcPath('a').is_reserved(), False)

    def test_joinpath(self):
        self.assertEqual(PureQrcPath().joinpath('a').joinpath('b').joinpath('c'), PureQrcPath('a/b/c'))
        self.assertEqual(PureQrcPath().joinpath('a', 'b', 'c'), PureQrcPath('a/b/c'))
        self.assertEqual(PureQrcPath('').joinpath('a').joinpath('b').joinpath('c'), PureQrcPath('a/b/c'))
        self.assertEqual(PureQrcPath('').joinpath('a', 'b', 'c'), PureQrcPath('a/b/c'))
        self.assertEqual(PureQrcPath(':').joinpath('a').joinpath('b').joinpath('c'), PureQrcPath(':/a/b/c'))
        self.assertEqual(PureQrcPath(':').joinpath('a', 'b', 'c'), PureQrcPath(':/a/b/c'))
        self.assertEqual(PureQrcPath(':/').joinpath('a').joinpath('b').joinpath('c'), PureQrcPath(':/a/b/c'))
        self.assertEqual(PureQrcPath(':/').joinpath('a', 'b', 'c'), PureQrcPath(':/a/b/c'))
        self.assertEqual(PureQrcPath(':').joinpath(':', ':/'), PureQrcPath(':'))

    def test_match(self):
        self.assertEqual(PureQrcPath().match('*.py'), False)
        self.assertEqual(PureQrcPath('').match('*.py'), False)
        self.assertEqual(PureQrcPath(':').match('*.py'), False)
        self.assertEqual(PureQrcPath(':/').match('*.py'), False)
        self.assertEqual(PureQrcPath(':/a/b/c').match('*.py'), False)
        self.assertEqual(PureQrcPath(':/a/b/c.py').match('*.py'), True)
        self.assertEqual(PureQrcPath('a/b/c').match('*.py'), False)
        self.assertEqual(PureQrcPath('a/b/c.py').match('*.py'), True)
        self.assertEqual(PureQrcPath('a').match('*.py'), False)
        self.assertEqual(PureQrcPath('a.py').match('*.py'), True)

    def test_relative_to(self):
        self.assertEqual(PureQrcPath(':/a/b/c').relative_to(':/'), PureQrcPath('a/b/c'))
        self.assertEqual(PureQrcPath(':/a/b/c').relative_to(':'), PureQrcPath('a/b/c'))
        self.assertEqual(PureQrcPath(':/a/b/c').relative_to(':/a'), PureQrcPath('b/c'))
        self.assertEqual(PureQrcPath(':/a/b/c').relative_to(':a'), PureQrcPath('b/c'))
        self.assertEqual(PureQrcPath(':/a/b/c').relative_to(':/a/b'), PureQrcPath('c'))

        self.assertEqual(PureQrcPath('a/b/c').relative_to('a/b'), PureQrcPath('c'))
        self.assertEqual(PureQrcPath('a/b/c').relative_to('a'), PureQrcPath('b/c'))
        self.assertEqual(PureQrcPath('a/b/c').relative_to('.'), PureQrcPath('a/b/c'))

        with self.assertRaises(ValueError):
            PureQrcPath(':/a/b/c').relative_to('a/b/c')

    def test_with_name(self):
        self.assertEqual(PureQrcPath(':/a/b/c').with_name('d'), PureQrcPath(':/a/b/d'))

        with self.assertRaises(ValueError):
            PureQrcPath(':/').with_name('d')

    def test_with_suffix(self):
        self.assertEqual(PureQrcPath(':/a/b/c').with_suffix('.d'), PureQrcPath(':/a/b/c.d'))
        self.assertEqual(PureQrcPath(':/a/b/c.d').with_suffix('.e'), PureQrcPath(':/a/b/c.e'))

        with self.assertRaises(ValueError):
            PureQrcPath(':/').with_suffix('.a')

    def test_str(self):
        self.assertEqual(str(PureQrcPath(':/a/b/c')), ':/a/b/c')
        self.assertEqual(str(PureQrcPath(':a/b/c')), ':/a/b/c')

    def test_eq(self):
        self.assertEqual(PureQrcPath(':/'), PureQrcPath(':'))
        self.assertEqual(PureQrcPath(':/test'), PureQrcPath(':test'))
        self.assertEqual(PureQrcPath(':test/'), PureQrcPath(':test'))
        self.assertEqual(PureQrcPath(':/test/'), PureQrcPath(':test'))
