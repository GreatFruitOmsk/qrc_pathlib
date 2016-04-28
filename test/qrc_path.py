import fnmatch
import unittest

from qrc_pathlib import QrcPath

from test import fixture


class TestQrcPath(unittest.TestCase):
    def test_cwd(self):
        with self.assertRaises(NotImplementedError):
            QrcPath.cwd()

    def test_home(self):
        with self.assertRaises(NotImplementedError):
            QrcPath.home()

    def test_stat(self):
        with self.assertRaises(NotImplementedError):
            QrcPath(':').stat()

    def test_chmod(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').chmod(0o777)

    def text_exists(self):
        self.assertTrue(QrcPath(':'))

    def test_expand_user(self):
        with self.assertRaises(NotImplementedError):
            QrcPath(':').expanduser()

    def test_glob(self):
        self.assertEqual(
            set(QrcPath(':').glob('*.txt')),
            {
                QrcPath(':42.txt'),
                QrcPath(':привет.txt')
            }
        )

        self.assertEqual(
            set(QrcPath(':').glob('**/*.txt')),
            {
                QrcPath(':42.txt'),
                QrcPath(':привет.txt'),
                QrcPath(':dir/1.txt'),
                QrcPath(':dir/2.txt')
            }
        )

    def test_group(self):
        with self.assertRaises(NotImplementedError):
            QrcPath(':').group()

    def test_is_dir(self):
        self.assertTrue(QrcPath(':').is_dir())

    def test_is_file(self):
        self.assertTrue(QrcPath(':42.txt').is_file())
        self.assertTrue(QrcPath(':привет.txt').is_file())
        self.assertTrue(QrcPath(':dir/1.txt').is_file())

    def test_is_symlink(self):
        self.assertFalse(QrcPath(':').is_symlink())

    def test_is_socket(self):
        self.assertFalse(QrcPath(':').is_socket())

    def test_is_fifo(self):
        self.assertFalse(QrcPath(':').is_fifo())

    def test_is_block_device(self):
        self.assertFalse(QrcPath(':').is_block_device())

    def test_is_char_device(self):
        self.assertFalse(QrcPath(':').is_char_device())

    def test_iterdir(self):
        self.assertEqual(
            set(QrcPath(':dir').iterdir()),
            {
                QrcPath(':dir/1.txt'),
                QrcPath(':dir/2.txt'),
                QrcPath(':dir/image.jpeg')
            })

    def test_lchmod(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').lchmod(0o777)

    def test_lstat(self):
        with self.assertRaises(NotImplementedError):
            QrcPath(':').lstat()

    def test_mkdir(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').mkdir()

    def test_open(self):
        with self.assertRaises(IsADirectoryError):
            QrcPath(':').open()

        with self.assertRaises(FileNotFoundError):
            QrcPath(':doesnotexist.txt').open()

        with self.assertRaises(ValueError):
            QrcPath(':42.txt').open('rw')

        with self.assertRaises(ValueError):
            QrcPath(':42.txt').open(buffering=100)

        with self.assertRaises(ValueError):
            QrcPath(':42.txt').open(newline='\r')

        with QrcPath(':42.txt').open('rb') as f:
            self.assertEqual(f.read(), b'42\n')

        with QrcPath(':42.txt').open('r') as f:
            self.assertEqual(f.read(), '42\n')

    def test_owner(self):
        with self.assertRaises(NotImplementedError):
            QrcPath(':').owner()

    def test_read_bytes(self):
        self.assertEqual(QrcPath(':42.txt').read_bytes(), b'42\n')

    def test_read_text(self):
        self.assertEqual(QrcPath(':привет.txt').read_text(), 'привет\n')

    def test_rename(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').rename('new_name')

    def test_replace(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').replace('new_name')

    def test_resolve(self):
        self.assertEqual(QrcPath(':привет.txt').resolve(), QrcPath(':привет.txt'))

        with self.assertRaises(FileNotFoundError):
            QrcPath(':doesnotexist.txt').resolve()

    def test_rglob(self):
        self.assertEqual(
            set(QrcPath(':').rglob('*.txt')),
            {
                QrcPath(':42.txt'),
                QrcPath(':привет.txt'),
                QrcPath(':dir/1.txt'),
                QrcPath(':dir/2.txt')
            }
        )

        self.assertEqual(
            set(QrcPath(':').rglob('image.*')),
            {
                QrcPath(':image.png'),
                QrcPath(':dir/image.jpeg')
            }
        )

    def test_rmdir(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').rmdir()

    def test_samefile(self):
        self.assertTrue(QrcPath(':привет.txt').samefile(QrcPath(':привет.txt')))
        self.assertTrue(QrcPath(':/привет.txt').samefile(QrcPath(':привет.txt')))

        self.assertTrue(QrcPath(':dir').samefile(QrcPath(':dir')))
        self.assertTrue(QrcPath(':dir').samefile(QrcPath(':dir/')))
        self.assertTrue(QrcPath(':/dir').samefile(QrcPath(':dir')))

        self.assertFalse(QrcPath(':42.txt').samefile(QrcPath(':привет.txt')))

    def test_symlink_to(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').symlink_to('path')

    def test_touch(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').touch()

    def test_unlink(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').unlink()

    def test_write_bytes(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').write_bytes(b'data')

    def test_write_text(self):
        with self.assertRaises(PermissionError):
            QrcPath(':').write_text('data')
