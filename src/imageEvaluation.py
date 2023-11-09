'''
This script provides a simple way to execute a full evaluation of all the images inside a folder, by specifying the folder during
call in the terminal.

The syntax looks like the following:
python3 imageEvaluation.py <path_to_data_folder"

By using this, the full evaluation may be run without modifying any of the scripts, and without having to change the images to evaluate 
to the default ./data/ directory.

Pass the absolute path to the folder in order to ensure good execution.
The script writes a .csv
'''

from paths import main_path
import sys
sys.path.append(main_path)

import sys
import os 
import csv
from evaluateAll import evaluateAll

def evaluateExec(path: str = '../data/', referenceImage: str = 'REF_23.PNG') -> None:
    # Create an empty list to store evaluation results
    evaluation_results = []

    try:
        # List all files in the specified directory
        files = os.listdir(path)

        # Iterate through each file in the directory
        for file in files:
            if file != referenceImage:
                # Placeholder for evaluation logic, replace with actual evaluation code
                evaluation_result = evaluateAll(os.path.join(path, file)) 

                # Append the filename and evaluation result to the list
                evaluation_results.append({'filename': file, 'result': evaluation_result})

        # Create a CSV file with the evaluation results
        csv_filename = 'evaluation_results.csv'
        csv_path = os.path.join(path, csv_filename)
        with open(csv_path, mode='w', newline='') as csv_file: 
            fieldnames = ['FIleNumber', 'result'] 
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            # Write the evaluation results for each image
            for result in evaluation_results:
                writer.writerow(result)

        print(f"Evaluation results saved to {csv_path}")

    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")


def main():
    # There are two options for the use
    # Specify the path to the images (absolute path) or not
    # Specify the name of the reference file
    
    if len(sys.argv) > 2:
        path = sys.argv[1]
        reference_file = sys.argv[2] 
        print(f"Received string: {path} and {reference_file}")
        evaluateExec(path, reference_file)
    
    elif len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if os.path.exists(arg):
            print(f"Received path: {arg}")
            evaluateExec(path=arg)
        else:
            # Assume that the string was not a path and consider it as a file
            print(f"Received file: {arg}")
        
    else:
        # Normal execution using the default path to data
        print("No string provided.")
        evaluateExec()

if __name__ == "__main__":
    main()
