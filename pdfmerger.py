import os
import re
import time
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

class PdfMerger(object):

    def __init__(self):
        print('Initializing...')
        '''Set some constants according to your needs'''
        # directory of PDFs need to be merged (DON'T end with "/")
        self.DIR_PATH = ' '
        # times that the match operation needs to be performed
        # TIMES = 2
        # the list of regular expressions
        RE_LIST = [
            '\d+'
        ]
        # the start index that can be matched of the PDF
        self.START_INDEX = 1
        # a value greater than the number of PDFs
        self.INF_VALUE = 100000  # usually don't need to change unless you have toooo many PDFs
        '''Values below are not supposed to be changed'''
        # max of the index that can be matched of the PDF
        self.max_index = -100000
        # number of invalid files
        self.invalid = 0
        # number of valid files
        self.valid = 0
        #
        self.merged = 0
        # patterns that will be generated according to RE_LIST
        self.PATTERNS = []
        # compile regular expressions to patterns
        for regexp in RE_LIST:
            self.PATTERNS.append(re.compile(regexp))
        # dictionary for iterate
        self.map = {}

    def __get_index(self, name):
        original_name = name
        # perform the regular expression matching sequentially
        for regpat in self.PATTERNS:
            name = regpat.search(name)
            if name is None:    # ignore the unexpected file
                print('    find an invalid file: ', original_name)
                return self.INF_VALUE
            else:
                name = name.group()

        return int(name)

    def __construct_dict(self):
        files = os.listdir(self.DIR_PATH)
        for f_name in files:
            index = self.__get_index(f_name)
            if index != self.INF_VALUE:
                self.map[index] = f_name
                self.valid += 1
                self.max_index = max(self.max_index, index)
            else:
                self.invalid += 1

    def work1(self, output = 'merged.pdf'):
        print('Working...')
        self.__construct_dict() # construct the map that from index to file name

        pdf_writer = PdfFileWriter()

        print('    Merging...')
        # iterate every PDF file
        # end = self.START_INDEX + self.valid - 1
        end = self.max_index + 1
        for i in range(self.START_INDEX, end):
            try:    # support for the discontinuous index
                f_name = self.map[i]
            except KeyError as err_key: # when the key doesn't exists
                print('Can\'t find key: ', err_key, ' , ignored.')
                continue

            file_path = self.DIR_PATH + '/' + f_name

            pdf_reader = PdfFileReader(file_path)
            # read every page
            for page in range(pdf_reader.getNumPages()):
                # add every page read into the writer
                pdf_writer.addPage(pdf_reader.getPage(page))

            print('    ', f_name, ' is merged.')
            self.merged += 1

        output_file = self.DIR_PATH + '/' + output
        with open(output_file, 'wb') as outf:
            pdf_writer.write(outf)  # output
            print('Finished merging ', self.merged, ' files.')

    def work2(self, output = 'merged.pdf'):
        print('Working...')
        self.__construct_dict()  # construct the map that from index to file name

        pdf_merger = PdfFileMerger()

        print('    Merging...')
        # iterate every PDF file
        # end = self.START_INDEX + self.valid - 1
        end = self.max_index + 1
        for i in range(self.START_INDEX, end):
            try:
                f_name = self.map[i]
            except KeyError as err_key:
                print('Can\'t find key: ', err_key, ' , ignored.')
                continue
            file_path = self.DIR_PATH + '/' + f_name
            pdf_merger.append(file_path)
            print('    ', f_name , ' is merged.')
            self.merged += 1

        output_file = self.DIR_PATH + '/' + output
        pdf_merger.write(output_file)
        print('Finished merging ', self.merged, ' files.')

    def work3(self, output = 'merged.pdf'):
        print('Working...')
        self.__construct_dict() # construct the map that from index to file name

        pdf_writer = PdfFileWriter()

        print('    Merging...')
        # end = self.START_INDEX + self.valid - 1
        end = self.max_index + 1
        for i in range(self.START_INDEX, end):
            try:
                f_name = self.map[i]
            except KeyError as err_key:
                print('Can\'t find key: ', err_key, ' , ignored.')
                continue

            file_path = self.DIR_PATH + '/' + f_name

            pdf_reader = PdfFileReader(file_path)
            pdf_writer.appendPagesFromReader(pdf_reader)
            print('    ', f_name, ' is merged.')
            self.merged += 1

        output_file = self.DIR_PATH + '/' + output
        with open(output_file, 'wb') as outf:
            pdf_writer.write(outf)
            print('Finished merging ', self.merged, ' files.')

    def work(self, output = 'merged.pdf', work_type = 2):
        start_time = time.time()

        if work_type is 1:
            self.work1(output)
        elif work_type is 2:
            self.work2(output)
        elif work_type is 3:
            self.work3(output)

        end_time = time.time()
        print('Merging completed in ', end_time - start_time, ' s')


if __name__ == '__main__':
    merger = PdfMerger()
    merger.work('output.pdf', work_type = 3)
