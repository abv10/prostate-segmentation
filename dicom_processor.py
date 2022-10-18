import os

import pydicom as pyd
import pydicom.data
import csv
from os.path import exists
import dicom2nifti
import SimpleITK as sitk

metadata_file = open("segmented_images/manifest-1605042674814/metadata.csv")
csvreader = csv.reader(metadata_file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
loc_index = header.index("File Location")
print(len(rows))
i = 1
for row in rows:
    file = row[loc_index].replace(".\\", "segmented_images/manifest-1605042674814\\")
    absolute = os.path.abspath(file)
    print(absolute)
    series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(absolute)
    print(len(series_file_names))
    series_reader = sitk.ImageSeriesReader()
    series_reader.SetFileNames(series_file_names)
    image3d = series_reader.Execute()

    save_img_file = "testlabels/" + str(i) + ".nii.gz"
    sitk.WriteImage(image3d, save_img_file, True)
    i += 1
    #print(os.path.exists(absolute))
    #print(dicom2nifti.convert_directory(absolute, os.path.abspath("test")))

exit(-3)


