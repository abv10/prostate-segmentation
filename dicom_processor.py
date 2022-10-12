import pydicom as pyd
import pydicom.data
import csv
from os.path import exists

metadata_file = open("segmented_images/manifest-1605042674814/metadata.csv")
csvreader = csv.reader(metadata_file)
header = []
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
loc_index = header.index("File Location")
all_name = "1-1.dcm"
for row in rows:
    original_path = row[loc_index]
    new_path = original_path.replace(".\\", "segmented_images/manifest-1605042674814\\") + "\\" + all_name
    ds = pyd.dcmread(new_path)
    print(ds.pixel_array.sum())

for image in ds.pixel_array:
    print(image.shape)
    print(image.sum())



exit(-3)