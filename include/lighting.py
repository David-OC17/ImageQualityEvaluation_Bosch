import cv2
import numpy as np
from PIL import Image

def find_white_shapes(image_path, output_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    image_gray = image.convert('L')

    # Convert the grayscale image to a NumPy array
    image_array = np.array(image_gray)

    # Calculate the center coordinates
    center_x, center_y = image_array.shape[1] // 2, image_array.shape[0] // 2

    # Define the width and height of the area you want to crop
    crop_width = 200  # Adjust this value as needed
    crop_height = 200  # Adjust this value as needed

    # Calculate the coordinates for cropping
    x1 = center_x - crop_width // 2
    x2 = center_x + crop_width // 2
    y1 = center_y - crop_height // 2
    y2 = center_y + crop_height // 2

    # Crop the image to the desired region
    cropped_image_array = image_array[y1:y2, x1:x2]

    # Apply Canny edge detection to the cropped image
    edges = cv2.Canny(cropped_image_array, 250, 200)

    # Find contours in the binary image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a three-channel image with white lines
    white_lines = np.zeros((crop_height, crop_width, 3), dtype=np.uint8)
    white_lines[edges != 0] = (255, 255, 255)  # White color in BGR format

    # Draw the contours on the white_lines image
    cv2.drawContours(white_lines, contours, -1, (255, 0, 0), 2)

    # Save the image with white contours
    Image.fromarray(white_lines).save(output_path)

    # Adjust contour coordinates for the cropping
    for contour in contours:
        for point in contour:
            x, y = point[0]
            # Adjust the coordinates to account for the cropping
            x += x1
            y += y1
            print(f"Contour Coordinate: x={x}, y={y}")

    return contours

# Specify the path to the input image file
input_image_path = "REF_23.PNG"

# Specify the path to the output image with white contours
output_image_path = "White_Contours_new.png"

# Perform edge detection and find white shapes (contours)
contours = find_white_shapes(input_image_path, output_image_path)

def measure_image_intensity(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    image_gray = image.convert('L')

    # Convert the grayscale image to a NumPy array
    image_array = np.array(image_gray)

    # Find contours in the binary image
    edges = cv2.Canny(image_array, 250, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the minimum and maximum X and Y coordinates among all contours
    min_x = min(contour[:, 0, 0].min() for contour in contours)
    max_x = max(contour[:, 0, 0].max() for contour in contours)
    min_y = min(contour[:, 0, 1].min() for contour in contours)
    max_y = max(contour[:, 0, 1].max() for contour in contours)

    # Define the region for intensity measurement, moving 5 pixels away from the edge
    center_x = (min_x + max_x) // 2
    center_y = (min_y + max_y) // 2
    region_width = 200  # Adjust this value as needed
    region_height = 200  # Adjust this value as needed

    x1 = max(center_x - region_width // 2, min_x + 5)
    x2 = min(center_x + region_width // 2, max_x - 5)
    y1 = max(center_y - region_height // 2, min_y + 5)
    y2 = min(center_y + region_height // 2, max_y - 5)

    # Crop the image to the defined region
    cropped_image_array = image_array[y1:y2, x1:x2]

    # Calculate the average intensity in the cropped region
    average_intensity = np.mean(cropped_image_array)

    return average_intensity

# Specify the path to the input image file
input_image_path = "REF_23.PNG"

# Perform intensity measurement
average_intensity = measure_image_intensity(input_image_path)

# Output the result
print(f"Average Intensity: {average_intensity}")

