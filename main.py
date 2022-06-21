import csv
import zipfile
import codecs
from csv import writer
from zipfile import ZipFile
import os

#Script to loop through a zip folder, it reads and writes CSV files and combine them.

#Function to read and write files to a Zipfolder
def zipfile_list():
    z_read = zipfile.ZipFile("zipfile.zip", "r")
    z_write = zipfile.ZipFile("zipfile.zip", "a")

    for filename in z_read.namelist(): # for loop to read file in the zip folder
        print('File:', filename)
        z_read.namelist()
        with z_read.open(filename, "r") as read_files:
            reader = csv.DictReader(codecs.iterdecode(read_files, 'utf-8'))
            for line in reader:
                print(line)

    with z_write.open('Combined.csv', "w") as write: # Open the csv file in zip folder then try to write in it
        fieldname = ['Source IP', 'Count']
        csv_writer = csv.DictWriter(write, fieldnames=fieldname, delimiter='\t')
        csv_writer.writeheader
        for line in reader: # loop through each line in the csv file then write rows to Combined.csv
            csv_writer.writerow(line)

    return line, filename

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zipfile_list()
