import os
from arg_parse import parser

# Get args
args = parser.parse_args()


class LS:
    def __init__(self, args):
        self.args = args

    def run(self):
        if self.args.list_subdir:
            data = self._list_subdir(self.args.path)
            self.long_format(data)
        else:
            data = self._show_and_sort(self.args.path)
            self.long_format(data)

    def _list_subdir(self, path):
        lst = self._show_and_sort(path)
        yield path
        yield lst
        for file in lst:
            sub_path = os.path.join(path, file)
            if os.path.isdir(sub_path):
                # If the dir not empty
                if os.listdir(sub_path):
                    yield from self._list_subdir(sub_path)

    def _show_and_sort(self, path):
        if self.args.show_hidden:
            return self._sort_by_size(path, os.listdir(path))
        else:
            lst = [
                file for file in os.listdir(path)
                if not file.startswith('.')
            ]
            return self._sort_by_size(path, lst)

    def _sort_by_size(self, path, lst):
            if self.args.sort_by_size:
                return sorted(
                    lst,
                    key=lambda f: os.path.getsize(os.path.join(path, f)))
            else:
                return lst

    def long_format(self, data):
        for d in data:
            if isinstance(d, list):
                self._long_format(d)
        else:
            pass

    def _long_format(self, data):
        if self.args.long_format:
            pass
        else:
            pass


program = LS(args)
program.run()
