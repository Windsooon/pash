import os
import unittest
from unittest.mock import patch
from file_info import FileInfo


class FileInfoTestCase(unittest.TestCase):

    @patch('os.path.isdir')
    @patch('os.path.basename')
    @patch('os.path.getmtime')
    @patch('grp.getgrgid')
    @patch('pwd.getpwuid')
    @patch('os.stat')
    @patch('os.listdir')
    def setUp(
            self, list_dir,
            stat, pwuid,
            grgid, getmtime,
            basename, isdir):
        full_path = os.path.abspath(__file__)
        list_dir.return_value = ['first.txt', '.second.txt', 'third.py']
        # 33206
        stat.return_value.st_mode = 33188
        stat.return_value.st_size = 1024
        pwuid.return_value.pw_name = 'Owner'
        grgid.return_value.gr_name = 'Group'
        getmtime.return_value = 1539587180.8723469
        basename.return_value = 'file.txt'
        isdir.return_value = False

        self.file = FileInfo(full_path)
        self.permission = self.file.permission
        self.link = self.file.link
        self.owner = self.file.owner
        self.group = self.file.group
        self.size = self.file.size
        self.modi_time = self.file.modi_time
        self.name = self.file.name

    def test_permission(self):
        # Default permission is 644
        self.assertEqual('-rw-r--r--', self.permission)

    @patch('os.path.isdir')
    @patch('os.listdir')
    def test_link(self, listdir, isdir):
        isdir.return_value = False
        full_path = os.path.abspath(__file__)
        self.file = FileInfo(full_path)
        listdir.return_value = ['first.txt', '.second.txt', 'third.py']
        self.link = self.file.link
        self.assertEqual(1, self.link)
        isdir.return_value = True
        self.file = FileInfo(full_path)
        self.link = self.file.link
        self.assertEqual(5, self.link)

    def test_owner(self):
        self.assertEqual('Owner', self.owner)

    def test_group(self):
        self.assertEqual('Group', self.group)

    def test_size(self):
        self.assertEqual(1024, self.size)

    def test_modi_time(self):
        self.assertEqual('Oct 15 15:06', self.modi_time)

    def test_basename(self):
        self.assertEqual('file.txt', self.name)
