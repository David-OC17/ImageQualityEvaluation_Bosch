from paths import main_path
import sys
sys.path.append(main_path)

from include.centering import evaluateCentering

def main() -> None:
    # Evaluate centering offset to reference image for all images
    # Evaluate all images recursivelly
    fileIndex = [1, 2, 4, 8, 9, 11, 12, 14, 18, 19, 20, 
                     21, 22, 24, 26, 27, 28, 29, 32, 36]
    
    for fileNum in fileIndex:
        print(f"Checking image {fileNum}:\n")
        test_result = evaluateCentering(str(fileNum), 'REF_23', 10)
        if test_result:
            print(f'Image {fileNum} NOT is compliant.')
        else:
            print(f'Image {fileNum} is compliant.')
        print("--------------------")

if __name__ == "__main__":
    main()
