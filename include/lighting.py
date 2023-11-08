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
