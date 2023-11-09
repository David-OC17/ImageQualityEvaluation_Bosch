'''
A main function for the app to run on an image, testing it on the 4 categories.
'''

#from paths import main_path
# import sys
#sys.path.append(main_path)


from include.centering import evaluateCentering
from include.orientation import evaluateOrientation
from include.lighting import evaluateLighting
from include.focus import sharp

# Remember to pass testFileNum with format '1.PNG', since the code does not add the extension by default
def evaluateAll(testFileNum:str, referenceFile:str='REF_23.PNG', path:str='../data/') -> list:
    '''
    Parameters ->   testFileNum: equivalent to testFileName. Name of image to evaluate in format 'filename.PNG'
                    path: path to the folder where test and reference images are
    
    Returns ->  bool: returns if the image is within the bounds of the tolerance for lighting (range is pixel intensity 170-250).
                      true if passes, false if it does not.
                      
    The function finds the edges of the center reference square and checks the lighting of a square of pixels that surrounds it.
    The function fails (returns false) if the mean of the analyzed region is outside the accepted range.
    '''
    
    '''
    Evaluates the testFileNum image, comparing it to the reference image.
    Receives a path to where the images are.
    The tests are: centering offset to reference, lighting, orientation, and focus.
    '''
    
    # Define the path where the data images are (provide a way )
    
    results = [False, False, False, False]
    
    # offset to reference (centering) (tolerance +/- 10)
    results[0] = evaluateCentering(testImageName=testFileNum, refImageName=referenceFile, tolerance=10, path=path)
    
    # lighting
    results[1] = evaluateLighting(testFileNum=testFileNum, path=path)
    
    # orientation (50 seems to be a good number for most cases)
    results[2] = evaluateOrientation(testFileName=testFileNum, maxBrightness=50, path=path)
    
    # focus (Sharpness of Image)
    results[3] = sharp(testFileName=testFileNum, path=path)

    return results