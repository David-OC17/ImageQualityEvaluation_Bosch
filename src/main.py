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

        # Evaluation section
        for index in range(len(fileIndex)):
            path = f"../data/{fileIndex[index]}.PNG"
            evImg = Image.open(path)
            oriented = evaluateTopRightCorner(evImg, 50)
            # Append elements to results
            results.append(list())
            results[index].append(f"{fileIndex[index]}.PNG")
            results[index].append(str(oriented))
        
        # Write results to a csv file
        writeToCsv()

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()