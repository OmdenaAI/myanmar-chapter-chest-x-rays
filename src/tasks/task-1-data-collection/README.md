# Tuberculosis Detection Model Dataset

**Task 1:  Data Collection**

We have compiled a set of PNG and JPG files of tuberculosis X-ray images from patients diagnosed with tuberculosis (TB+) and those who are healthy or sick individuals with another respiratory diseas (TB-). 

There are few gold standard datasets, which are cited by most if not all published acadmic papers. Such datasets can include images in the DICOM, PNG, and JPG format and include segmentation masks and/or bounding boxes to facilitate object segmentation and detection. We have opted not to use either.  

The main datasets are:

1. the Omdena dataset, published by the National Institutes of Health in Montgomery, AL and Shenzhen, China 
2. the Belarus dataset, provided by NIH and represents patients resitant to conventional treatment regimnes
3. the TBX11K dataset, published by
4. and the TBXpredict (DA and DB, perhaps for Delhi) datasets.

We are doing a binary classification model with the possibility of a multi-class of active TB, latent TB, sick non-TB, and healthy perhaps if there is more manpower. Currently the breakdown of the TB (1) and non-TB (0) Chest X-Ray (CXR) images are the following:

- Non-TB:
  - 6600 healthy CXR images from TBX11K
  - 1800 sick non-TV images from TBX11K
  - 406 normal CXR images from NIH Montgomery and Shenzhen

- Tuberculosis:
  - 1058 TB XCR images from Belarus (converted from DICOM)
  - 394 TB XCR images from NIH Montgomery and Shenzhen
  - 800 TB XCR images from TBX11K
  - 100 TB XCR images from DA (TBXpredict) and DB (converted from DICOM)

**Total Dataset:**  

- 8006 TB positive CXR files 
- 2339 TB negative CXR files (core dataset before employing undersamplings, oversamplings, andor augmentations)

**Our main goals were:**

1. Collect as many individual instances of TB infection as possible to combat class imbalance, preferably returning to the original data source
   - Determine if there are any duplicates as data scientists often incorporates any gold standard data published prior to the study

2. Making sure the dataset has a good balance of sick vs. healhy in the TB-minus group
   - To make a more balanced dataset, one of the steps we undertook was to convert those DICOMs, instead leaving them out. We employed different techniques which will be discussed in the next task.


**Google Drive Link:** https://drive.google.com/drive/folders/1FTOEkBmq7kIpklYlEMKm8g8VwxQFhvP5?usp=drive_link

**Google Drive link to TBXpredict:** https://drive.google.com/drive/folders/1HhICaP7ICDqoyNVYfRdMVTCc8SKX1NYR?usp=drive_link

`tuberculosis-detection-model` currently has the following directory structure:

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

`TBXpredict (DA)` currently has the following directory structure:

```
├── non-tb
├── tb
└── label_information.txt
```

