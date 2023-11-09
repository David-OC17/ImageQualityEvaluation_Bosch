# Bosch Hackathon - ADAS Camera Image Quality Evaluation
## Introduction
This repository is dedicated to the evaluation of ADAS (Advanced Driver Assistance Systems) camera images for the Bosch Hackathon. The goal is to assess the quality of the images captured by ADAS cameras and ensure they meet the required standards. All images in this dataset are standardized to be 640 by 480 pixels.

## Quick start

### Installation
**Prerequisites:**
Python3

1. Clone the repository to your computer.

2. To install the full requirements of the application, use the following command:
```python
pip install -r requirements.txt
```
3. Create `paths.py` inside `src/` directory. It should contain something like the following:
```python
main_path = '/<path_to_repo>/ImageQualityEvaluation_Bosch'
```  

### Usage
There are two main ways to use the system, one is by running a script of Python which analyzes all the images inside the data directory and produces a `.csv` file with the results of evaluating all the images in the 4 test. 


## Evaluation Categories
The image evaluation process is divided into four main categories:

### 1. Centering
This category assesses whether the subject of the image is properly centered. An image is considered centered when the main subject or region of interest is well-aligned within the frame.

The following figure shows two overlaping images; the reference on the back and with the black features painted in blue, and the testing image `12.PNG` in the front with the black sections painted in red.
<p align="center">
  <img src="./images/comparison23-12_centering.png" alt="Centering comparison: Reference vs 12" width="500">
</p>
The figure shows how a part of the images' reference figures overlap, and also helps to distinguish how the offset from the reference presents itself in some images.

The way in which we asses the centering of an image respect to the reference is by performing the following operations:

1. Load the reference and comparison images
2. Convert the images to Numpy arrays
3. Calculate cross-correlation betweent the two images
4. Find the location of the maximum correlation peak
5. Calculate offsets from the center
6. Check if the offset is inside the desired limits

Via this method we may determine if the new image is compliant with the tolerances, all comparing to the reference image.

### 2. Focus
The focus evaluation checks the sharpness and clarity of the image. It helps determine whether the camera captured a clear and focused image or if blurriness or distortion is present.

### 3. Lighting
The lighting test measures pixel intensity to assess image brightness, offering a reliable indicator. Test limits range from a minimum of 170 to a maximum of 250. This test evaluates if the lighting in a set of 20 images complies with these limits. Passing signifies meeting standards, while failing suggests deviation. Proper lighting is pivotal for clear and precise image analysis.

The way in which we asses the lighting of an image respect to the reference is by performing the following operations:

1. Read the Image and Convert to Grayscale Format. 
2. Apply Binary Thresholding.
3. Find the Contours of the shape.
4. Draw Contours on the Original Image.
5. Collect Contour Data.
6. Calculate Mean RGB Color.
7. Evaluate Lighting regarding the calculation. 

By employing this method, we can ascertain whether the new image complies with the established tolerances, all while comparing it to the reference image.


### 4. Orientation
Orientation is crucial for image interpretation. Images must be in the correct orientation to facilitate accurate analysis. To be considered correctly oriented, an image must adhere to the following guidelines:

One of the black reference squares should be positioned at the center of the image.
The other black reference square should be at the top right corner of the image.
If the top right corner square is not in its designated position, the image is considered to have an incorrect orientation. Tests for correct orientation involve defining a "window" where the top right black reference square should be if oriented correctly. The system then checks if the average brightness of this region is as low as it should be for the square to be considered the reference square.

Here are two examples of images being checked via this method:

**Valid orientation**
<p align="center">
  <img src="./images/REF_23_evaluateOrientation.PNG" alt="Centering comparison: Reference vs 12" width="400">
</p>

This image is considered to be valid, as when the top right red region is checked for averag black and white instensity of the channel, it lands below the given threshold. _Note that the threshold may be determined by heuristics

**Invalid orientation**
<p align="center">
  <img src="./images/36._evaluateOrientation.PNG" alt="Centering comparison: Reference vs 12" width="400">
</p>


### Contribute
We welcome contributions from the Bosch Hackathon community. If you have ideas for improving the image quality evaluation process or want to contribute code or documentation, please feel free to open an issue or submit a pull request.

### License
This project is licensed under the MIT License, which means you are free to use and modify the code as long as you comply with the license terms. 