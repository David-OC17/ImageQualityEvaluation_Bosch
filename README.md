# Bosch Hackathon - ADAS Camera Image Quality Evaluation
## Introduction
This repository is dedicated to the evaluation of ADAS (Advanced Driver Assistance Systems) camera images for the Bosch Hackathon. The goal is to assess the quality of the images captured by ADAS cameras and ensure they meet the required standards. All images in this dataset are standardized to be 640 by 480 pixels.

## Evaluation Categories
The image evaluation process is divided into four main categories:

<<<<<<< Updated upstream
### 1. Centering
This category assesses whether the subject of the image is properly centered. An image is considered centered when the main subject or region of interest is well-aligned within the frame.
=======
## Quick start and installation

>>>>>>> Stashed changes

### 2. Focus
The focus evaluation checks the sharpness and clarity of the image. It helps determine whether the camera captured a clear and focused image or if blurriness or distortion is present.

<<<<<<< Updated upstream
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
=======
Centering refers to the positioning of an image within its frame or field of view. It's a critical aspect of image quality evaluation as defined by ISO standards. Proper centering ensures that the subject of the image is correctly aligned and doesn't appear off-center. This involves evaluating how well an image's main subject or object is positioned relative to the center of the frame.

To evaluate centering according to ISO standards, the image can be compared to a reference image or template. Various image processing techniques can be applied to assess how closely the subject of interest aligns with the center point. This assessment is crucial for applications like photography, computer vision, and quality control in fields such as manufacturing.

To correct centering issues, adjustments may be made by shifting or cropping the image to reposition the subject accurately within the frame.

<p align="center">
  <img src="./images/comparison23-12_centering.png" alt="Centering comparison: Reference vs 12" width="600">
</p>

## Focus

Focus in image quality evaluation pertains to the sharpness and clarity of an image. It is a key aspect assessed using standards such as ISO 12233. Focus evaluation involves determining how well-defined the subject or object in an image appears. A focused image should exhibit crisp and clear details, while an out-of-focus image may appear blurry or lack sharpness.

To evaluate focus, ISO 12233 provides a standardized test pattern that can be used to measure the sharpness of an image. This involves analyzing how well-defined certain elements in the image are, often using metrics like the Modulation Transfer Function (MTF).

For correction, if an image is found to be out of focus, techniques such as image sharpening may be employed to enhance the clarity of the subject.

## Lighting

Lighting, also known as brightness, plays a significant role in image quality assessment. Proper lighting ensures that an image is adequately illuminated, allowing for clear and accurate visibility of the subject. ISO standards address the evaluation of brightness, ensuring that images are neither underexposed (too dark) nor overexposed (too bright).

To evaluate lighting, ISO standards may specify methods for measuring the luminance or intensity of light in an image. This involves assessing whether the image's brightness falls within the acceptable range.

For correction, adjustments to the exposure settings during image capture or post-processing techniques can be applied to achieve the desired level of lighting. Balancing lighting is crucial for applications ranging from photography to medical imaging.

These aspects—centering, focus, and lighting—constitute key components of image quality evaluation, ensuring that images are visually clear, properly aligned, and appropriately illuminated for their intended purpose. Adhering to ISO standards for these parameters can lead to improved image quality in various fields.
>>>>>>> Stashed changes

