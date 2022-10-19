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
for row in rows:
    file = row[loc_index].replace(".\\", "segmented_images/manifest-1605042674814\\")
    absolute = os.path.abspath(file)
    pat_id = absolute.split("-")[2][1:4]

    series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(absolute)
    series_reader = sitk.ImageSeriesReader()
    series_reader.SetFileNames(series_file_names)
    image3d = series_reader.Execute()

    save_img_file = "nnUNet_raw_data_base/nnUNet_raw_data/Task501_Prostate/imagesTr/PROS_" + pat_id + ".nii.gz"
    sitk.WriteImage(image3d, save_img_file, True)

exit(-3)