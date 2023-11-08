# Custom paths
import sys
sys.path.append('/home/david/Documents/Code/BoschHackathon/ImageQualityEvaluation_Bosch')
from include.orientation import evaluateTopRightCorner

from PIL import Image
import csv

# Array for storing the results of each image
results = [[]] # Format -> [orientation, centering, brightness, focus]

# Write to a CSV file the evaluation results
def writeToCsv():
    fields = ['Image', 'Orientation', 'Centering', 'Brightness', 'Focus']
    file = "../Results.csv"
    with open(file, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(fields)
        writer.writerows(results)


def main():
    try:
        fileIndex = [1, 2, 4, 8, 9, 11, 12, 14, 18, 19, 20, 
                     21, 22, 24, 26, 27, 28, 29, 32, 36]
        
        # Reference image
        path = "../data/REF_23.PNG"
        refImg = Image.open(path)

        # Images to evaluate 
        index = 1
        imgName = str(index) + ".PNG"
        path = "../data/" + imgName
        evImg = Image.open(path)
        
        # Evaluation section
        for img in fileIndex:
            print()
        
        # Write results to a csv file
        writeToCsv()

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()