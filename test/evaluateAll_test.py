'''
Test the implementation of evaluateAll function.
'''

from paths import main_path
import sys
sys.path.append(main_path)

from src.evaluateAll import evaluateAll

def main() -> None:
    fileIndex = [1, 2, 4, 8, 9, 11, 12, 14, 18, 19, 20, 
                 21, 22, 24, 26, 27, 28, 29, 32, 36]
    
    # Evaluate all the images
    # Remember to pass the test image name, reference image name and path to the data (as needed)
    
    # We may skip the path and let it be the default '../data/
    # Also skip passing the reference file name, use the default 'REF_23.PNG'
    
    for fileNum in fileIndex:
        print(f"Checking image {fileNum}:\n")
        evaluateAll(testFileNum=fileNum)
        print("--------------------")
        
if __name__ == "__main__":
    main()
