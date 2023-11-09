'''
A main function for the app to run on an image, testing it on the 4 categories.
'''

# from paths import main_path
# sys.path.append(main_path)


from centering import evaluateCentering
from orientation import evaluateOrientation
from lighting import evaluateLighting
from focus import sharp


def evaluate(testFileNum: str) -> list:
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
