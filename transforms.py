import os
import random

import torch
import numpy as np
import torchio as tio


def augment_images(image_path, label_path, task, new_id, transform):
    original_image = tio.ScalarImage(image_path)
    original_label = tio.LabelMap(label_path)

    transformed_image = transform(original_image)
    transformed_label = transform(original_label)

    transformed_label.save("nnUNET_raw_data_base/nnUNET_raw_data/" + task + "/labelsTr/PROS_" + str(new_id) + ".nii.gz")
    transformed_image.save("nnUNET_raw_data_base/nnUNET_raw_data/" + task + "/imagesTr/PROS_" + str(new_id) + "_0000.nii.gz")
    print(new_id)


def flip_images(task, max_id):
    image_path = "nnUNET_raw_data_base/nnUNET_raw_data/" + task + "/imagesTr/"
    label_path = "nnUNET_raw_data_base/nnUNET_raw_data/" + task + "/labelsTr/"

    images = os.listdir(image_path)
    labels = os.listdir(label_path)
    if len(images) != len(labels):
        print("EXCEPTION: NOT MATCHED DATASET and LABEL SIZE")
    flip = tio.RandomFlip(flip_probability=1.0, axes=('LR',))
    current_id = max_id + 1
    for i in range(len(images)):
        or_im = image_path + images[i]
        or_lab = label_path + labels[i]
        augment_images(or_im, or_lab, task, pad(current_id), flip)
        current_id += 1


def affine_transform(task, max_id):
    image_path = "nnUNET_raw_data_base/nnUNET_raw_data/" + task + "/imagesTr/"
    label_path = "nnUNET_raw_data_base/nnUNET_raw_data/" + task + "/labelsTr/"

    images = os.listdir(image_path)
    labels = os.listdir(label_path)
    if len(images) != len(labels):
        print("EXCEPTION: NOT MATCHED DATASET and LABEL SIZE")
    current_id = max_id + 1
    for i in range(len(images)):
        or_im = image_path + images[i]
        or_lab = label_path + labels[i]

        transform_one = get_transform()
        augment_images(or_im, or_lab, task, pad(current_id), transform_one)
        current_id += 1

        transform_two = get_transform()
        augment_images(or_im, or_lab, task, pad(current_id), transform_two)
        current_id += 1


def get_transform():
    scale1 = random.uniform(0.8, 1.2)
    scale2 = random.uniform(0.8, 1.2)
    degrees = random.randint(0, 10)

    print(degrees)
    return tio.RandomAffine(
        scales=(min(scale1, scale2), max(scale1, scale2)),
        degrees=degrees,
    )


def pad(id_num):
    if id_num < 10:
        return "00" + str(id_num)
    elif id_num < 100:
        return "0" + str(id_num)
    else:
        return str(id_num)

if __name__ == "__main__":
    affine_transform("Task602_Prostate", 415)