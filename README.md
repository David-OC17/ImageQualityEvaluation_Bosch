# Bosch Hackathon - ADAS Camera Image Quality Evaluation
## Introduction
This repository is dedicated to the evaluation of ADAS (Advanced Driver Assistance Systems) camera images for the Bosch Hackathon. The goal is to assess the quality of the images captured by ADAS cameras and ensure they meet the required standards. All images in this dataset are standardized to be 640 by 480 pixels.

## Evaluation Categories
The image evaluation process is divided into four main categories:

### 1. Centering
This category assesses whether the subject of the image is properly centered. An image is considered centered when the main subject or region of interest is well-aligned within the frame.

### 2. Focus
The focus evaluation checks the sharpness and clarity of the image. It helps determine whether the camera captured a clear and focused image or if blurriness or distortion is present.

### 3. Lighting
Lighting is a critical factor in image quality. This category evaluates the brightness and illumination of the image to ensure it meets the desired standards. Proper lighting is essential for clear and accurate analysis.

### 4. Orientation
Orientation is crucial for image interpretation. Images must be in the correct orientation to facilitate accurate analysis. To be considered correctly oriented, an image must adhere to the following guidelines:

One of the black reference squares should be positioned at the center of the image.
The other black reference square should be at the top right corner of the image.
If the top right corner square is not in its designated position, the image is considered to have an incorrect orientation. Tests for correct orientation involve defining a "window" where the top right black reference square should be if oriented correctly. The system then checks if the average brightness of this region is as low as it should be for the square to be considered the reference square.

### Usage
For evaluating images, refer to the specific scripts or tools provided in this repository. Detailed instructions and guidelines for each evaluation category can be found within their respective directories or files.

### Contribute
We welcome contributions from the Bosch Hackathon community. If you have ideas for improving the image quality evaluation process or want to contribute code or documentation, please feel free to open an issue or submit a pull request.

### License
This project is licensed under the MIT License, which means you are free to use and modify the code as long as you comply with the license terms.

