# Tuberculosis Detection Model Dataset

We have compiled the Tuberculosis and non-Tuberculosis (includes healthy individuals and sick individuals with other pulmonary diseases) images from the original TBX11K, NIH, and TBXpredict dataset.

Currently the dataset contains the files from the Kaggle TBX11K, Kaggle Qatar, and TBXpredict datasets:

- Non-TB:
  - 6600 healthy from TBX11K
  - 1800 sick non-TB from TBX11K
  - 406 normal from Qatar (NIH)
  - 52 TB-negative from DA (TBXpredict)

- Tuberculosis:
  - 306 TB from Qatar (Belarus)
  - 394 TB from Qatar (NIH)
  - 800 TB from TBX11K
  - 52 TB from DA (TBXpredict)

The rough estimate so far is 1491 TB images and 7507 non-TB images.

The link to the dataset (TBX11K, NIH, RSNA) is the following URL:  https://drive.google.com/drive/folders/1FTOEkBmq7kIpklYlEMKm8g8VwxQFhvP5?usp=drive_link

The link to the dataset (TBXpredict): https://drive.google.com/drive/folders/1HhICaP7ICDqoyNVYfRdMVTCc8SKX1NYR?usp=drive_link

tuberculosis-detection-model currently has the following directory structure:

	├── Tuberculosis 
	├── Non-Tuberculosis

TBXpredict (DA) currently has the following directory structure:

```
|-- non-tb
|-- tb
└── label_information.txt
```
