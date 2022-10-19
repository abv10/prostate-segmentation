import os.path

import numpy as np
import pydicom
from nnunet.dataset_conversion.utils import generate_dataset_json
from nnunet.paths import nnUNet_raw_data, preprocessing_output_dir

ds = pydicom.dcmread(os.path.abspath("segmented_images/manifest-1605042674814/PROSTATEx/ProstateX-0044/11-14-2011-NA-MC prostaat kliniek detectie-mc MCPROSKL30-92752/300.000000-Segmentation-3.186/1-1.dcm"))
pixel = ds.pixel_array
output_file = os.path.abspath("nnUNET_raw_data_base/nnUNET_raw_data/Task501_Prostate/dataset.json")
images_tr = os.path.abspath("nnUNET_raw_data_base/nnUNET_raw_data/Task501_Prostate/imagesTr/")
labels_tr = os.path.abspath("nnUNET_raw_data_base/nnUNET_raw_data/Task501_Prostate/labelsTr/")
modalities = ("T2", )
labels = {1: 'peripheral zone', 2: 'transition zone', 2: 'prostatic urethra', 3: 'anterior fibromuscalar stroma of prostate'}
dataset_name = 'TASK501_Prostate'
generate_dataset_json(output_file, images_tr, labels_tr, modalities, labels, dataset_name)
