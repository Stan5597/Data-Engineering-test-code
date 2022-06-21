import unittest

import zipfile

import codecs
import csv
from csv import writer

from csv import reader

from zipfile import ZipFile

import os

#Script test case to test function in the main

#Class to test the Ziplist function in the main
class TestZipList(unittest.TestCase):

    def test_zip_list(self):

        z_read = zipfile.ZipFile("zipfile.zip", "r")
        z_write = zipfile.ZipFile("zipfile.zip", "a")

        for file in z_read.namelist():

            print('File:', file)

            z_read.namelist()

            with z_read.open(file, "r") as read_files:

                reader = csv.DictReader(codecs.iterdecode(read_files, 'utf-8'))

                for line in reader:
                    print(line)

        with z_write.open('Combined.csv', "w") as write:

            fieldname = ['Adress', 'Name']

            csv_writer = csv.DictWriter(write, fieldnames=fieldname, delimiter='\t')

            csv_writer.writeheader

            for line in reader:
                csv_writer.writerow(line)

        return line, file

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.TestCase()
