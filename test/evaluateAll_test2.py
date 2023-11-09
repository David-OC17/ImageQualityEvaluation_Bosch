# Custom paths

from paths import main_path
import sys
sys.path.append(main_path)

from src.evaluateAll import evaluateAll
import pandas as pd


def main():
    # Array for storing the results of each image
    centering = [] # Format -> [orientation, centering, brightness, focus]
    lightning = []
    orientation = []
    focus = []
    
    try:
        fileIndex = [1, 2, 4, 8, 9, 11, 12, 14, 18, 19, 20, 
                     21, 22, 24, 26, 27, 28, 29, 32, 36, "REF_23"]

        # Evaluation section
        for index in fileIndex:
            results = evaluateAll(f"{index}.PNG")

            # Append elements to results
            centering.append(results[0])
            lightning.append(results[1])
            orientation.append(results[2])
            focus.append(results[3])

        df = pd.DataFrame({'File_Index': fileIndex, 'Centering': centering, "Lightning": lightning, "Orientation": orientation, "Sharpness": focus})
        print(df)

    except Exception as ex:
        print(ex)


main()