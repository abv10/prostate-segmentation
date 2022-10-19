import os

training = []
for file in os.listdir("nnUNET_raw_data_base/nnUNET_raw_data/Task501_Prostate/imagesTr"):
    training.append({"image":"./imagesTr/"+file, "label": "./labelsTr/" +file})

print(training)