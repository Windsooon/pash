import unittest
import os
from pash_src.arg_parse import parser, args


class ParseTestCase(unittest.TestCase):

    def test_all_args_parser(self):
        tem_args = parser.parse_args(['-p', 'hello', '-l', '-a', '-S', '-R'])
        self.assertEqual(tem_args.path, 'hello')
        self.assertTrue(tem_args.long_format)
        self.assertTrue(tem_args.show_hidden)
        self.assertTrue(tem_args.sort_by_size)
        self.assertTrue(tem_args.list_subdir)

    def test_no_path_args_parser(self):
        tem_args = parser.parse_args(['-l'])
        self.assertEqual(tem_args.path, None)
        self.assertEqual(args.path, os.getcwd())
