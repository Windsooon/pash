import unittest
from arg_parse import parser


class ParseTestCase(unittest.TestCase):

    def test_parser(self):
        args = parser.parse_args(['-p', 'hello', '-l', '-a', '-S', '-R'])
        self.assertEqual(args.path, 'hello')
        self.assertTrue(args.long_format)
        self.assertTrue(args.show_hidden)
        self.assertTrue(args.sort_by_size)
        self.assertTrue(args.list_subdir)
