import os.path

import numpy as np
import pydicom
from nnunet.dataset_conversion.utils import generate_dataset_json
from nnunet.paths import nnUNet_raw_data, preprocessing_output_dir


output_file = os.path.abspath("nnUNET_raw_data_base/nnUNET_raw_data/Task603_Prostate/dataset.json")
images_tr = os.path.abspath("nnUNET_raw_data_base/nnUNET_raw_data/Task603_Prostate/imagesTr/")
labels_tr = os.path.abspath("nnUNET_raw_data_base/nnUNET_raw_data/Task603_Prostate/labelsTr/")
modalities = ("T2", )
labels = {0: "background", 1: 'peripheral zone', 2: 'transition zone', 3: 'prostatic urethra', 4: 'anterior fibromuscalar stroma of prostate'}
dataset_name = 'TASK603_Prostate'
generate_dataset_json(output_file, images_tr, labels_tr, modalities, labels, dataset_name)
