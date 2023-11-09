import cv2

def evaluateLighting(testFileNum:str, path:str='../data/') -> bool:
    '''
    Parameters ->   testFileNum: equivalent to testFileName. Name of image to evaluate in format 'filename.PNG'
                    path: path to the folder where test and reference images are
    
    Returns ->  bool: returns if the image is within the bounds of the tolerance for lighting (range is pixel intensity 170-250).
                      true if passes, false if it does not.
                      
    The function finds the edges of the center reference square and checks the lighting of a square of pixels that surrounds it.
    The function fails (returns false) if the mean of the analyzed region is outside the accepted range.
    '''
    
    # Assume all data is inside /data/
    path = f'{path}{testFileNum}'
    image = cv2.imread(path)
    
    crop_img = image[100:350, 100:500]

    #1.Read the Image and convert it to Grayscale Format
    
    # convert the image to grayscale format
    img_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    #2. Apply Binary Thresholding

    # apply binary thresholding
    ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

    #3. Find the Contours

    # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)


    #4.  draw contours on the original image
    image_copy = crop_img.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1,
                     lineType=cv2.LINE_AA)

    # see the result
    #cv2.imwrite('contours_none_image1.jpg', image_copy)

    list_light = []

    for x, y in enumerate(contours[1]):
        list_light.append(y)


    # Initialize variables to store the sum of RGB values
    total_red = 0
    total_green = 0
    total_blue = 0
    count = 0

    #print("/////////////////")

    for x in list_light:
        element1 = x[0][0]  # First integer
        element2 = x[0][1]  # Second integer
        #print(f"First element: {element1}, Second element: {element2}")

        if element1 < 235:
            element1 -= 5
        elif element1 > 235:
            element1 += 5
        if element2 < 100:
            element2 -= 5
        elif element2 > 100:
            element2 += 5

        pixel_color = crop_img[element2, element1]
        blue, green, red = pixel_color

        #print(f"RGB color of pixel ({element1}, {element2}): ({red}, {green}, {blue})")

        total_red += red
        total_green += green
        total_blue += blue
        count += 1


    # Calculate the mean RGB color
    mean_red = total_red // count
    mean_green = total_green // count
    mean_blue = total_blue // count

    color_mean = (mean_red + mean_blue + mean_green) / 3

    #print("/////")
    #print(f"Mean RGB color of the specified range: ({mean_red}, {mean_green}, {mean_blue})")
    #print(f"Mean Color : {color_mean}")

    if 170 <= color_mean <= 230:
        #print("Image with lightning within range")
        return True
    else:
        #print("Image lightning NOT in range")
        return False
