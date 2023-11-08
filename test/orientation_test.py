import sys
sys.path.append('/home/david/Documents/Code/BoschHackathon/ImageQualityEvaluation_Bosch')

from include.orientation import evaluateTopRightCorner
from PIL import Image

def evaluateOrientation(num:int) -> None:
    try:
        # Reference image
        path = f"../data/{num}.PNG"
        refImg = Image.open(path)
        maxBrightness = 50

        over = evaluateTopRightCorner(refImg, maxBrightness)
        
        if over:
            print(f"Image {path} is oriented correctly")
        else:
            print(f"Image {path} is NOT oriented correctly")

    except Exception as ex:
        print(ex)    

def main() -> None:
    # Evaluate all images recursivelly
    fileIndex = [1, 2, 4, 8, 9, 11, 12, 14, 18, 19, 20, 
                     21, 22, 24, 26, 27, 28, 29, 32, 36]
    
    for fileNum in fileIndex:
        print(f"Checking image {fileNum}:\n")
        evaluateOrientation(fileNum)
        print("--------------------")

if __name__ == '__main__':
    main()