import os

import pydicom as pyd
import pydicom.data
import csv
from os.path import exists
import dicom2nifti

metadata_file = open("segmented_images/manifest-1605042674814/metadata.csv")
csvreader = csv.reader(metadata_file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
loc_index = header.index("File Location")

all_name = "1-1.dcm"
for row in rows:
    original_path = row[loc_index]
    new_path = original_path.replace(".\\", "segmented_images/manifest-1605042674814\\")  + "\\" + all_name
    ds = pyd.dcmread(new_path)
    print(ds.pixel_array.shape)


metadata_file = open("original_images/manifest-1605042674814/metadata.csv")
csvreader = csv.reader(metadata_file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
loc_index = header.index("File Location")

path = rows[0][loc_index].replace(".\\", "original_images/manifest-1605042674814\\")
for file in os.listdir(path):
    ds = pyd.dcmread(path +"\\" + file)
    print(ds.pixel_array.shape)

exit(-3)