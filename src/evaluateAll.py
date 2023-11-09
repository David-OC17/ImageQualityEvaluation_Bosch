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
    Evaluates the testFileNum image, comparing it to the reference image.
    Receives a path to where the images are.
    The tests are: centering offset to reference, lighting, orientation, and focus.
    '''
    
    # Define the path where the data images are (provide a way )
    
    results = [False, False, False, False]
    
    # offset to reference (centering) (tolerance +/- 10)
    results[0] = evaluateCentering(testImageName=testFileNum, refImageName=referenceFile, path=path)
    
    # lighting
    results[1] = evaluateLighting(testFileNum=testFileNum, path=path)
    
    # orientation (50 seems to be a good number for most cases)
    results[2] = evaluateOrientation(testFileNum=testFileNum, maxBrightness=50, path=path)
    
    # focus (Sharpness of Image)
    results[3] = sharp(testFileNum=testFileNum, path=path)

    return results