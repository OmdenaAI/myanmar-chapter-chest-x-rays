# Tuberculosis Detection Model Dataset

We have compiled the Tuberculosis and non-Tuberculosis (includes healthy individuals and sick individuals with other pulmonary diseases) images from the NIH, Belarus, TBX11K and TBXpredict (also called DA and DB) datasets.

We are constructing a binary classification model to identify whether a patient has tuberculosis through analysis of the chest X-ray images. Currently the breakdown of the origins of the images are the following:

Non-Tuberculosis:
- 3800 healthy CXR images from TBX11K
- 3800 sick non-TV images from TBX11K

Tuberculosis:
- 1048 TB CXR images from Belarus (converted from DICOM)
- 394 TB CXR images from NIH Montgomery and Shenzhen
- 800 TB CXR images from TBX11K
- 45 and 52 TB CXR images from DA (TBXpredict) and DB (converted from DICOM)

The rough estimate so far is 7600 non-TB images and 2339 TB and 2339 augmented TB images.

The link to the dataset: https://drive.google.com/drive/folders/1FTOEkBmq7kIpklYlEMKm8g8VwxQFhvP5?usp=drive_link
The link to the dataset (TBXpredict): https://drive.google.com/drive/folders/1HhICaP7ICDqoyNVYfRdMVTCc8SKX1NYR?usp=drive_link

tuberculosis-detection-model currently has the following directory structure:

  ```
  datasets
  │
	├── augmented_class
	│   ├── TB
	│   └── Non-TB
  │
  ├── augmented_train_val_test
	│   ├── train
  │   │   ├── Non-TB
  │   │   └── TB 
  │   ├── val
  │   │   ├── Non-TB
  │   │   └── TB 
	│   └── test
  │       └── test  
  │
  ├── original
	│   ├── Non-TB
  │   └── TB
  │
  └── tb_albumentations
      
  ```
