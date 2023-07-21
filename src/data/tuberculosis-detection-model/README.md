# Tuberculosis Detection Model Dataset

We have compiled the Tuberculosis and non-Tuberculosis (includes healthy individuals and sick individuals with other pulmonary diseases) images from the original TBX11K dataset and the NIH dataset.

We have not decided whether to include the bounding boxes into the dataset, so the XML and JSON files have not been included.

The link to the dataset is the following URL:  https://drive.google.com/drive/folders/1FTOEkBmq7kIpklYlEMKm8g8VwxQFhvP5?usp=drive_link

tuberculosis-detection-model currently has the following directory structure:

	├── Tuberculosis  
	│   ├── Kaggle TBX11K
	│	│   ├── health
	│	│   └── sick
	│   ├── NIH Montgomery 
	│   └── NIH Shenzhen
	│ 
	├── Non-Tuberculosis
	│   ├── Kaggle TBX11K
	│	│   └── tb
	│   ├── NIH Montgomery
	│   └── NIH Shenzhen


The rough estimate so far is 1194 TB images and 8006 non-TB images.

