import os
from arg_parse import parser
from file_info import FileInfo

# Get args
args = parser.parse_args()


class LS:
    def __init__(self, args):
        '''
        para args: args input like -l, -a, -R
        '''
        self.args = args
        # Get generator depend on args input
        # ── foo
        #    ├── bar
        #    ├── hello
        # return generator -> ('/foo/', ['/bar', '/hello'])...
        data = self._list_subdir(self.args.path)
        self.choose_format(data)

    def _list_subdir(self, path):
        '''
        para args: full_path to run ls command

        First: Show and sort dirs in root path by _show_and_sort function
        Second: Recursion yield generator
        '''
        lst = self._show_and_sort(path)
        yield (path, lst)
        if self.args.list_subdir:
            for file in lst:
                sub_path = os.path.join(path, file)
                if os.path.isdir(sub_path):
                    # If the dir not empty
                    if os.listdir(sub_path):
                        yield from self._list_subdir(sub_path)

    def _show_and_sort(self, path):
        '''
        para args: full_path to run ls command

        Show hidden files and sort files depend on args input
        '''
        if self.args.show_hidden:
            lst = os.listdir(path) + ['.', '..']
        else:
            lst = [
                file for file in os.listdir(path)
                if not file.startswith('.')
            ]
        return self._sort_by_size(path, lst)

    def _sort_by_size(self, path, lst):
        '''
        para args: root_path
        para lst: subdir_path

        Sort files by file size
        '''
        if self.args.sort_by_size:
            return sorted(
                lst,
                key=lambda f: os.path.getsize(os.path.join(path, f)))
        else:
            return sorted(lst)

    def choose_format(self, gen):
        '''
        para gen: generator ('/foo/', ['/bar', '/hello'])...

        Display file format depend on args input
        '''
        for g in gen:
            if self.args.list_subdir:
                print(g[0])
            self._choose_format(g)

    def _choose_format(self, data):
        '''
        para: data like ('/foo/', ['/bar', '/hello'])

        Display long format or not
        '''
        if self.args.long_format:
            self._get_info(data)
        else:
            data = data[1]
            width = max(40, len(max(data, key=lambda k: len(k))))
            for k, v in enumerate(data):
                if k % 3 == 2 or k == len(data)-1:
                    print('{:<{width}}'.format(v, width=width))
                else:
                    print('{:<{width}}'.format(v, width=width), end='')
            print()

    def _get_info(self, data):
        '''
        para: data like ('/foo/', ['/bar', '/hello'])

        Get file long format indo
        '''
        for d in data[1]:
            f = FileInfo(os.path.join(data[0], d))
            file_info = (
                f.permission, f.link,
                f.owner, f.group,
                f.size, f.modi_time, f.name)
            self._format_info(file_info)

    def _format_info(self, info):
        print('{0:<12}{1:<4}{2:<10}{3:<10}{4:>4}{5:^15}{6:<10}'.format(*info))


program = LS(args)
