'''
The purpose of this of this file is to present a way to evaluate if the orientation of the iamges is the correct one.
To be considered with the right orientation, the image must have one of the black reference squared at the center, and the other one at the top right corner. 
If the corner square is out of place, then the image has incorrect orientation.

Dimensions of the kernel for brightness evaluation: 50 * 50 pixels

Absolute position of kernel for evaluation:
515 (x) left - right
30 (y) top - bottom
'''

from PIL import Image
from PIL import ImageStat

# Assume that all images are of size 640 * 480 pixels
def evaluateTopRightCorner(image:Image, maxBrightness:int ) -> bool:
    '''
    Checks whether the kernel has a mean lightness below a threshold and returns if it is below it.
    Is below the value: true
    Is NOT below the value: false
    '''    
    # Determine the relative path to the images
    # path = f"../data/{filename}"
        
    # Define the position and size of the kernel
    y_size = 50
    x_size = 50
    
    # The position is given by the starting point of the image, which is the bottom left corner
    y_top, y_bottom = 480 - 20, 480 - 20 - y_size
    x_left, x_right = 515, 515 + x_size
    
    # Convert the image to B&B
    image = image.convert('L')
    
    # Calculate the mean of the region specified by the position and size of the kernel
    # Crop to the wanted region
    selection = image.crop((x_left, y_bottom, x_right, y_top))
    selection.show()
    
    if selection.width > 0 and selection.height > 0:
        # Calculate the statistics for the selected region
        mean = ImageStat.Stat(selection).mean
        print("Mean:", mean)
    else:
        print("Selected region is empty, cannot calculate the mean.")

    # Return if the average is below or above what is expected
    if mean[0] > maxBrightness:
        return False
    else:
        return True