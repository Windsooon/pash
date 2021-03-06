import os
import shutil
import unittest
from unittest.mock import MagicMock
from pash.arg_parse import parser
from pash.ls_class import LS


class LsFunctionTestCase(unittest.TestCase):
    path = os.path.join(os.getcwd(), 'tests_path/')

    @classmethod
    def setUpClass(cls):
        try:
            os.mkdir(cls.path)
        except FileExistsError:
            pass
        else:
            with open(cls.path + 'a_small.txt', 'w') as f:
                f.write('foo')
            with open(cls.path + 'big.txt', 'w') as f:
                f.write('barbarbarbar')
            with open(cls.path + '.hidden.txt', 'w') as f:
                f.write('hiddenhiddenhiddenhidden')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.path)

    def test_long_info(self):
        args = parser.parse_args(['-p', self.path, '-l'])
        self.ls = LS(args)
        f = MagicMock()
        f.permission = '-rw-r--r--'
        f.link = 1
        f.owner = 'Owner'
        f.group = 'Group'
        f.size = 1024
        f.modi_time = 'Oct 15 15:06'
        f.name = 'file.txt'
        self.assertEqual((
            '-rw-r--r--', 1, 'Owner', 'Group',
            1024, 'Oct 15 15:06', 'file.txt'),
            (self.ls._long_info(f)))

    def test_sort_by_size_or_not(self):
        args = parser.parse_args(['-p', self.path, '-S'])
        self.ls = LS(args)
        self.assertEqual(
            ['big.txt', 'a_small.txt'],
            self.ls._sort_by_size(
                self.path, ['a_small.txt', 'big.txt']))

        args = parser.parse_args(['-p', self.path])
        self.ls = LS(args)
        self.assertEqual(
            ['a_small.txt', 'big.txt'],
            self.ls._sort_by_size(
                self.path, ['a_small.txt', 'big.txt']))

    def test_show_hidden_files_or_not(self):
        args = parser.parse_args(['-p', self.path, '-a'])
        self.ls = LS(args)
        self.assertEqual(
            ['big.txt', 'a_small.txt', '.hidden.txt', '.', '..'],
            self.ls._show_hidden_files(
                self.path))

        args = parser.parse_args(['-p', self.path])
        self.ls = LS(args)
        self.assertEqual(
            ['big.txt', 'a_small.txt'],
            self.ls._show_hidden_files(
                self.path))

        args = parser.parse_args(['-p', self.path, '-a'])
        self.ls = LS(args)
        self.assertEqual(
            ['big.txt', 'a_small.txt', '.hidden.txt', '.', '..'],
            self.ls._show_hidden_files(
                self.path))

    def test_list_subdir_or_not(self):
        args = parser.parse_args(['-p', self.path, '-R'])
        return_lst = (self.path, ['a_small.txt', 'big.txt'])
        self.ls = LS(args)
        for gen in self.ls._list_subdir(self.path):
            self.assertEqual(
                gen, return_lst)

    def test_list_subdir_show_hidden(self):
        args = parser.parse_args(['-p', self.path, '-R', '-a'])
        return_lst = (
            self.path,
            ['.', '..', '.hidden.txt',
                'a_small.txt', 'big.txt'])
        self.ls = LS(args)
        for gen in self.ls._list_subdir(self.path):
            self.assertEqual(
                gen, return_lst)

    def test_list_subdir_and_sort(self):
        args = parser.parse_args(['-p', self.path, '-R', '-S'])
        return_lst = (
            self.path,
            ['big.txt', 'a_small.txt'])
        self.ls = LS(args)
        for gen in self.ls._list_subdir(self.path):
            self.assertEqual(
                gen, return_lst)

    def test_list_subdir_and_sort_and_show_hidden(self):
        args = parser.parse_args(['-p', self.path, '-R', '-S', '-a'])
        return_lst = (
            self.path,
            ['..', '.', '.hidden.txt', 'big.txt', 'a_small.txt'])
        self.ls = LS(args)
        for gen in self.ls._list_subdir(self.path):
            self.assertEqual(
                gen, return_lst)
