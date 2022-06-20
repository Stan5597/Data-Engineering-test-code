import csv
import pandas
import pandas as pd
import zipfile
from csv import writer
from zipfile import ZipFile
import os

# Script to loop through a zip folder and loop through the csv file and combine them.


#Print every csv files in the provided pathname directory
for filename in os.listdir("Engineering Test Risk Analytics .zip"):
    if filename.endswith('.csv'):
        print (filename)# print csv filename 
        

# loop through each csv file and append them to the combine.csv file
def zipfile_list():

    z = zipfile.ZipFile("Engineering Test Risk Analytics .zip", "r")# read the zip folder

    for filename in z.namelist():
        print('File:', filename)
        z.namelist()
        df = pd.read_csv(z.open(filename))
        print(df)
        with open(filename) as file:
            rows = [[row[0].strip()] for row in csv.reader(file)]
        with open("Combine.csv", "a") as f: # open the combine.csv and append the file

            csv_writer = writer(f)
            csv_writer.writerow(rows)
            
