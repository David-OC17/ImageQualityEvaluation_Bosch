'''
These functions aim to facilitate a way to evaluate centering of an image in comparison to a reference. 
The comparison is done by detecting shapes, or interest points, and comparing the discrepacy of centering, which may
also be though as a transformation of the image, by calculating a homography matrix.
'''

import numpy as np
from PIL import Image
import scipy.signal


# Provide the images as a matrix
def cross_image(im1:np.ndarray, im2:np.ndarray):
   # get rid of the color channels by performing a grayscale transform
   # the type cast into 'float' is to avoid overflows
   im1_gray = np.sum(im1.astype('float'), axis=2)
   im2_gray = np.sum(im2.astype('float'), axis=2)

   # get rid of the averages, otherwise the results are not good
   im1_gray -= np.mean(im1_gray)
   im2_gray -= np.mean(im2_gray)

   # calculate the correlation image; note the flipping of onw of the images
   return scipy.signal.fftconvolve(im1_gray, im2_gray[::-1,::-1], mode='same')

def evaluateCentering(refImageName :str = 'REF_23.PNG', testImageName :str = '12.PNG', tolerance:int=10, path:str='../data/') -> bool:
    '''
    Parameters ->   refImageName: name of reference image in format 'filename.PNG'
                    testImageName: name of image to compare in format 'filename.PNG'
                    tolerance: number of pixels the image can be off-center to pass (default tolerance is +/- 10 pixels)
                    path: path to the folder where test and reference images are
    
    Returns ->  bool: returns if the image is within the bounds of the tolerance for offset from the center.
                      true if passes, false if it does not.
                      
    The function uses cross-reference to find a point from which to compare, and calculates the deviation from the center for both images.
    '''
    
    # Load reference and new image
    reference_path = f'{path}{refImageName}'
    reference_image = Image.open(reference_path)
    
    new_path = f'{path}{testImageName}'
    new_image = Image.open(new_path)
    
    ###############################################
    #             Optional operation              #
    # Crop both images to reduce the comparison   #
    # area. Try to reduce compute time, and       #
    # increase accuracy.                          #
    ###############################################
        
    width, height = reference_image.size
        
    # Define the position and size of the crop
    crop_width = 320
    crop_height = 240

    # Calculate the center coordinates
    center_x = width // 2
    center_y = height // 2

    # Calculate the left, right, top, and bottom coordinates for cropping
    x_left = center_x - crop_width // 2
    x_right = center_x + crop_width // 2
    y_top = center_y - crop_height // 2
    y_bottom = center_y + crop_height // 2

    # Crop the center region
    reference_image = reference_image.crop((x_left, y_top, x_right, y_bottom))
    new_image = new_image.crop((x_left, y_top, x_right, y_bottom))
    
    ###############################################
    
    width, height = reference_image.size
    
    # Cut the images to avoid unnecessary work on the image, as well as providing less points in which the images may coincide
    # Cut them to a rectangle of the same relation height-width, in the center, and of 

    # Convert the image to a NumPy array
    reference_np = np.array(reference_image)
    new_np = np.array(new_image)

    # Calculate the cross-correlation between the two images (pass them as numpy arrays)
    correlation_result = cross_image(reference_np, new_np)

    # Perform further processing or analysis on the correlation_result
    # For example, finding the location of the maximum correlation peak
    max_corr_position = np.unravel_index(np.argmax(correlation_result), correlation_result.shape)
    
    #print("Max correlation position:", max_corr_position)
    
    max_corr_y = max_corr_position[0]
    max_corr_x = max_corr_position[1]
    
    # Calculate the offsets from the center
    x_offset = (max_corr_x - (width / 2)) * 2
    y_offset = (max_corr_y - (height / 2)) * 2

    # Uncomment to debug
    print(testImageName)
    print("X Offset (in pixels):", x_offset)
    print("Y Offset (in pixels):", y_offset)
    print("\n\n")
    
    # Add or substract to offsets to account for some error
    x_offset -= 0.5
    y_offset -= 0.5
    
    # Check if the offsets are inside the accepted margins
    if abs(x_offset) < tolerance and abs(y_offset) < tolerance:
        return True
    else:
        return False