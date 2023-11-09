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

def evaluateCentering(refImageName :str = 'REF_23', testImageName :str = '12', tolerance:int=10) -> bool:
    '''
    Evaluate if the test image is off-center from the reference image, by more than the tolerance permits it to be.
    If the image is within bounds, returns true (else false). Defualt tolerance is +/- 10 pixels.
    '''
    
    # Load reference and new image
    reference_path = f"../data/{refImageName}.PNG"
    reference_image = Image.open(reference_path)
    new_path = f'../data/{testImageName}.PNG'
    new_image = Image.open(new_path)
    
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
    x_offset = max_corr_x - (width / 2)
    y_offset = max_corr_y - (height / 2)

    # Uncomment to debug
    print("X Offset (in pixels):", x_offset)
    print("Y Offset (in pixels):", y_offset)
    
    # Check if the offsets are inside the accepted margins
    if x_offset > tolerance or y_offset > tolerance:
        return True
    else:
        return False