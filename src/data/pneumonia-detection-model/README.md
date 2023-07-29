# Pneumonia Detection Model Dataset

Compilation of dataset images with labels (Normal/Non-Pneumonia, Pneumonia) from the NIH, Mendeley, and RSNA.

Breakdown of data sources used Chest X-Ray images are the following:

- Non-Pneumonia/Normal:
  - 1,591 Normal images from Mendeley
  - 3,003 Non-Pneumonia from NIH
  - 5,000 Normal from RSNA

- Pneumonia:
  - 4,281 from Mendeley
  - 313 from NIH
  - 5000 from RSNA

Total images for each classification is 9,594. The NIH CXR normal/non_pneumonia images have a total amount of approximately ~114,000 but these have been moved from the original directory to an excess folder. The total images or excess folder were not uploaded on GitHub or Google Drive as the total memory space needed is 45 GB. This has been diminished to 3,003 to match the amount of images for each classification.

The link to the datasets: (Extract the zip files and follow the directory structure or mount your own drive and change the path structure in the script).

Mendeley: https://drive.google.com/file/d/1a2mW94hFRjXP3UaAApD4XF2XO_Cxvcur/view?usp=drive_link

NIH CXR: https://drive.google.com/file/d/12LIUfjcTBhDyYhmxWUpZLRKXtfvTOZQ6/view?usp=drive_link

RSNA: https://drive.google.com/file/d/1cMptR9UPgnVd3eAJO-zB_EXriizrhvgH/view?usp=drive_link

Each of the datasets have a directory of:

```
├── Parent Folder
    ├── Normal (or non_pneumonia)
    └── Pneumonia
```
