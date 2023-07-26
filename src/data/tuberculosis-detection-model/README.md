# Tuberculosis Detection Model Dataset

We have compiled the Tuberculosis and non-Tuberculosis (includes healthy individuals and sick individuals with other pulmonary diseases) images from the NIH, Belarus, TBX11K and TBXpredict (also called DA and DB) datasets.

We are doing a binary classification model with the possibility of a multi-class of active TB, latent TB, sick non-TB, and healthy perhaps.

Currently the breakdown of the origins of the TB nd non-TB Chest X-Ray images are the following:

- Non-TB:
  - 6600 healthy CXR images from TBX11K
  - 1800 sick non-TV images from TBX11K
  - 406 normal CXR images from NIH Montgomery and Shenzhen
  - 52 TB-negative from DA (TBXpredict)

- Tuberculosis:
  - 1058 TB XCR images from Belarus (converted from DICOM)
  - 394 TB XCR images from NIH Montgomery and Shenzhen
  - 800 TB XCR images from TBX11K
  - 52 TB from DA (TBXpredict)
  - 48 TB positive XCR images from DB (converted from DICOM)

The rough estimate so far is 7559 non-TB images and 2352 TB images. Whenever possible, we would go to the source of the dataset to collect the original files themslves since subseqeunt studies or projects would combine different datasets together.

To make a more balanced dataset, we converted the DICOM files of active TB patients into PNG format to bolster that class. We additionally only populated the TB files from the PB dataset for 75/25 roughly split for majority/minority class, which we use image augmentation to further address the class imbalance.

The link to the dataset: https://drive.google.com/drive/folders/1FTOEkBmq7kIpklYlEMKm8g8VwxQFhvP5?usp=drive_link

The link to the dataset (TBXpredict): https://drive.google.com/drive/folders/1HhICaP7ICDqoyNVYfRdMVTCc8SKX1NYR?usp=drive_link

tuberculosis-detection-model currently has the following directory structure:

  ```
  tuberculosis-detection-model
  │
	├── augmented (used Albumentations for image augmentation of minority class)
	│   ├── Augmented TB (images created through augmentation pipeline)
	│   ├── Non-Tuberculosis (link to folder in original)
  │   ├── output (training and validation datasets with augmented data)
  │   │   ├── train
  │   │   │   ├── Non-Tuberculosis
  │   │   │   └── Tuberculosis 
  │   │   └── val
  │   │       ├── Non-Tuberculosis
  │   │       └── Tuberculosis
  │   └── Tuberculosis (link to folder in original)
  │
  └── original 
      ├── Non-Tuberculosis (original non-TB set)
      ├── output (training and validation datasets without augmentation)
      │   ├── train
      │   │   ├── Non-Tuberculosis
      │   │   └── Tuberculosis 
      │   └── val
      │       ├── Non-Tuberculosis
      │       └── Tuberculosis     
      └── Tuberculosis (original TB set)
      
  ```

TBXpredict (DA) currently has the following directory structure:

```
├── non-tb
├── tb
└── label_information.txt
```

