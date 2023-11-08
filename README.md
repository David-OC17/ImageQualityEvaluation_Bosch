# ImageQualityEvaluation_Bosch
Evaluation of ADAS camera images for Bosch Hackathon.

The size of all the images is 640 by 480 pixels.


## Centering

## Focus

## Lighting 

## Orientation
To be considered with the right orientation, the image must have one of the black reference squared at the center, and the other one at the top right corner. 
If the corner square is out of place, then the image has incorrect orientation. The tests consists of defining a _window_ where the top right black reference square should be if oriented correctly, and checking if the average brightness of the region is as low is would need to be for the square to be the reference square.