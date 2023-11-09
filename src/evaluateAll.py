'''
A main function for the app to run on an image, testing it on the 4 categories.
'''

#from paths import main_path
import sys
#sys.path.append(main_path)


from include.centering import evaluateCentering
from include.orientation import evaluateOrientation
from include.lighting import evaluateLighting
from include.focus import sharp


def evaluateAll(testFileNum:str) -> list:
    '''
    Evaluates the testFileNum image, comparing it to the reference image.
    The tests are: centering offset to reference, lighting, orientation, and focus.
    '''
    
    results = [False, False, False, False]
    referenceFile = 'REF_23'
    
    # offset to reference (centering) (tolerance +/- 10)
    results[0] = evaluateCentering(testFileNum, referenceFile, 10)
    
    # lighting
    results[1] = evaluateLighting(testFileNum)
    
    # orientation (50 seems to be a good number for most cases)
    results[2] = evaluateOrientation(testFileNum, 50)
    
    # focus (Sharpness of Image)
    results[3] = sharp(testFileNum)

    return results


#print(evaluateAll("1"))

