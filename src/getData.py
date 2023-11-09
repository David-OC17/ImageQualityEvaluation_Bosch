# Custom paths

from evaluateAll import evaluateAll
import pandas as pd

def getData() ->pd.DataFrame:
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
            path = f"{index}"
            results = evaluateAll(path)

            # Append elements to results
            centering.append(results[0])
            lightning.append(results[1])
            orientation.append(results[2])
            focus.append(results[3])

        df = pd.DataFrame({'File_Index': fileIndex, 'Centering': centering, "Lightning": lightning, "Orientation": orientation, "Sharpness": focus})
        return df
    
    except Exception as ex:
        print(ex)
