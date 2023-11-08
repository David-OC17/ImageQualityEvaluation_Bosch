# import sys
# sys.path.append("../include/")

from orientation import evaluateTopRightCorner
from PIL import Image

def main() -> None:
    try:
        # Reference image
        path = "../data/REF_23.PNG"
        refImg = Image.open(path)
        maxBrightness = 50

        over = evaluateTopRightCorner(refImg, maxBrightness)
        
        if over:
            print(f"Image {path} is oriented correctly")
        else:
            print(f"Image {path} is NOT oriented correctly")

    except Exception as ex:
        print(ex)    

if __name__ == '__main__':
    main()