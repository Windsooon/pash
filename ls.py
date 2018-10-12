"""
Implement Bash command ls with Python
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
        "-l", action="store_true",
        dest="long_format",
        help="use a long listing format")
parser.add_argument(
        "-a",
        action="store_true",
        dest="ignore_hide",
        help="do not ignore entries starting with .")
parser.add_argument(
        "-S",
        action="store_true",
        dest="sort_size",
        help="sort by file size")
parser.add_argument(
        "-R",
        action="store_true",
        dest="list_sub",
        help="list subdirectories recursively")
args = parser.parse_args()

if args.long_format:
    pass
