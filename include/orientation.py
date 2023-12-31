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
def evaluateOrientation(testFileName:str, maxBrightness:int, path:str='../data/') -> bool:
    '''
    Receives -> Path(optional) and name of the image to evaluate
                maxBrightness - Maximum allowed value for top right dark square testing

    Returns ->  Bool - which indicates wheter the image is correctly oriented or not

    Checks whether the kernel which should contain top right dark square has a mean lightness 
    below a threshold and returns if it is below it.
    '''    
    # Determine the relative path to the images
    path = f'{path}{testFileName}'
    image = Image.open(path)

    # Get the dimensions of the image
    width, height = image.size

    # Define the position and size of the crop
    crop_width = 50
    crop_height = 50
    x_left = width - crop_width - 80
    x_right = width - 80
    y_top = 0 + 20
    y_bottom = crop_height + 20

    # Crop the top right corner
    selection = image.crop((x_left, y_top, x_right, y_bottom))
    
    # Convert the image to B&B
    image = image.convert('L')
    
    if selection.width > 0 and selection.height > 0:
        # Calculate the statistics for the selected region
        mean = ImageStat.Stat(selection).mean
        #print("Mean:", mean)
    else:
        print("Selected region is empty, cannot calculate the mean.")

    # Return if the average is below or above what is expected
    if mean[0] > maxBrightness:
        return False
    else:
        return True