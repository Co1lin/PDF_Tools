import os
import re

class IndexMap(object):

    def __init__(self):

        self.dir_path = ''
        self.patterns = []
        self.inf_index = 1000000000
        self.start_index = self.inf_index
        self.max_index = -self.inf_index
        self.map = {}
        self.valid = 0
        self.invalid = 0

    def set_patterns(self, RE_LIST):
        self.patterns = []
        for regexp in RE_LIST:
            self.patterns.append(re.compile(regexp))

    def append_patterns(self, RE_LIST):
        for regexp in RE_LIST:
            self.patterns.append(re.compile(regexp))

    def input_patterns(self):
        print('Please input the regular expressions.\nNO quotation marks! End with \"end\"')
        #re_list = []
        i = 1
        while True:
            regexp = input('    Please input expression %d: ' %i)
            if regexp == 'end':
                break
            else:
                self.patterns.append(re.compile(regexp))
                i += 1
        i -= 1
        print('%d expressions inputted and compiled to patterns.' %i)

    def __process_dir_path_str(self, dir_path):
        if dir_path[-1] == '/' or dir_path[-1] == '\\':
            dir_path = dir_path[:-1]
        return dir_path

    def set_dir(self, dir_path):
        self.dir_path = self.__process_dir_path_str(dir_path)

    def input_dir(self):
        self.dir_path = input('Please input the directory path. NO quotation marks!\n -> ')
        self.dir_path = self.__process_dir_path_str(self.dir_path)
        print("Read directory path: %s" % self.dir_path)

    def __get_index(self, name):
        original_name = name
        # perform the regular expression matching sequentially
        for regpat in self.patterns:
            name = regpat.search(name)
            if name is None:    # ignore the unexpected file
                print('    Find an invalid file: ', original_name)
                return self.inf_index
            else:
                name = name.group()
        if int(name) < self.inf_index:
            return int(name)
        else:
            return self.inf_index

    def construct_map(self, print_info = False):
        if print_info is True:
            print('Constructing map...')
        if len(self.patterns) > 0:
            files = os.listdir(self.dir_path)
            for f in files:
                index = self.__get_index(f)
                if index != self.inf_index:
                    self.map[index] = f
                    self.valid += 1
                    self.max_index = max(self.max_index, index)
                    self.start_index = min(self.start_index, index)
                    if print_info is True:
                        print('    %d -> %s  constructed.' % (index, f))
                else:
                    self.invalid += 1
        else:
            raise Exception('Error: Pattern list is empty. Please fill the regular expression list first.')

    def get(self, index):
        return self.map[index]

    def print_info(self):
        print('\n%d valid files and %d invalid files.\nIndex start from %d and end at %d.'
              % (self.valid, self.invalid, self.start_index, self.max_index))


if __name__ == '__main__':
    filemap = IndexMap()
    filemap.input_dir()
    filemap.input_patterns()
    filemap.construct_map(True)
    filemap.print_info()