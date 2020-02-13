import os
import re
import time
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from IndexMap import IndexMap

class PdfMerger(object):

    def __init__(self, files, output = 'output.pdf'):
        print('Initializing...')
        self.files = files
        self.merged = 0
        self.output = output

    def work(self):
        print('Working...')
        start_time = time.time()

        pdf_writer = PdfFileWriter()

        print('    Merging...')
        end = self.files.max_index + 1
        for i in range(self.files.start_index, end):
            try:
                f_name = self.files.get(i)
            except KeyError as err_key:
                print('Can\'t find key: ', err_key, ' , ignored.')
                continue

            file_path = self.files.dir_path + '/' + f_name

            pdf_reader = PdfFileReader(file_path)
            pdf_writer.appendPagesFromReader(pdf_reader)
            print('    ', f_name, ' is merged.')
            self.merged += 1

        output_file = self.files.dir_path + '/' + self.output
        with open(output_file, 'wb') as outf:
            pdf_writer.write(outf)
            print('Finished merging ', self.merged, ' files.')

        end_time = time.time()
        print('Merging completed in ', end_time - start_time, ' s')

if __name__ == '__main__':
    files = IndexMap()
    files.set_dir('/path/to/dir_of_PDF_files')
    RE_LIST = [
        '\d+'
    ]
    files.set_patterns(RE_LIST)
    files.construct_map()
    merger = PdfMerger(files, 'output.pdf')
    merger.work()