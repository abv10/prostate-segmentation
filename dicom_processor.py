import csv
import os
from math import floor
import multiprocessing as mp
import matplotlib.pyplot as plt

import SimpleITK as sitk

# TODO Add args to make it more easily resuable
from SimpleITK import sitkLabelUInt8, sitkUInt8


def convert(dicom_path):
    file = dicom_path.replace(".\\", "segmented_images/manifest-1605042674814\\")
    absolute = os.path.abspath(file)
    print(absolute)
    pat_id = absolute.split("-")[2][1:4]
    original_image = sitk.ReadImage(os.path.abspath("nnUNET_raw_data_base/nnUNET_raw_data/Task501_Prostate/imagesTr"
                                                    "/PROS_" + pat_id + "_0000.nii.gz"))
    or_origin = original_image.GetOrigin()
    or_direction = original_image.GetDirection()
    or_spacing = original_image.GetSpacing()

    series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(absolute)
    series_reader = sitk.ImageSeriesReader()
    series_reader.SetFileNames(series_file_names)
    image3d = series_reader.Execute()
    size = image3d.GetSize()

    series = floor(size[2] / 4)
    new_image = sitk.Image([size[0], size[1], series], sitkUInt8)
    new_image.SetOrigin(or_origin)
    new_image.SetDirection(or_direction)
    new_image.SetSpacing(or_spacing)

    for s in range(series):
        for i in range(size[1]):
            for j in range(size[0]):
                if image3d[i, j, s, 0] > 0:
                    new_image[i, j, s] = 1
                elif image3d[i, j, s + series, 0] > 0:
                    new_image[i, j, s] = 2
                elif image3d[i, j, 0 + series * 2, 0] > 0:
                    new_image[i, j, s] = 3
                elif image3d[i, j, s + series * 3, 0] > 0:
                    new_image[i, j, s] = 4

    save_img_file = "nnUNet_raw_data_base/nnUNet_raw_data/Task501_Prostate/labelsTr/PROS_" + pat_id + ".nii.gz"
    sitk.WriteImage(new_image, save_img_file, True)
    return new_image.GetOrigin(), new_image.GetDirection(), new_image.GetSpacing()


if __name__ == "__main__":
    metadata_file = open("segmented_images/manifest-1605042674814/metadata.csv")
    csvreader = csv.reader(metadata_file)
    header = []
    header = next(csvreader)
    rows = []
    for r in csvreader:
        rows.append(r)
    loc_index = header.index("File Location")

    print(len(rows))
    print(len(rows[0]))
    print(loc_index)
    pool = mp.Pool(6)

    list_of_results = pool.map(convert, (row[loc_index] for row in rows[6:]))
    pool.close()
    pool.join()
