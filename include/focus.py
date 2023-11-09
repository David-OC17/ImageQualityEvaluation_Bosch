import cv2
import matplotlib.pyplot as plt
import numpy as np


def sharp(testFileName:str, path:str='../data/') -> bool:

    path = f'{path}{testFileName}'
    image = cv2.imread(path)
    # Exact crop 50x50 pixels where change between black and white is noticeable
    crop_img = image[250:300, 370:420]

    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    #cv2.imwrite('image.jpg', crop_img)
    #cv2.imwrite("gray.jpg", gray)

    # Normalize 2500 pixels in image
    # Get the height and width of the image
    height, width = gray.shape

    norm_pixels = []
    pixels = []

    # Iterate through the grayscale image and print the pixel values
    for y in range(height):
        for x in range(width):
            pixel_value = gray[y, x]
            #print(f"Pixel at ({x}, {y}): {pixel_value/255}")
            norm_pixels.append(pixel_value/255)
            pixels.append(pixel_value)


    # Plot the ESF
    x_values = range(1, len(norm_pixels) + 1)
    sorted_pixels = sorted(norm_pixels)


    # Diff the ESF to get LSF
    esf_array = np.array(sorted_pixels)

    # Calculate the LSF by taking central differences
    lsf = np.diff(esf_array)

    # Create an array of x values corresponding to the LSF
    x_lsf = np.arange(1, len(lsf) + 1)

    # Normalize data with min-max
    min_vals = lsf.min(axis=0)
    max_vals = lsf.max(axis=0)

    # Perform Min-Max scaling
    normalized_data = (lsf - min_vals) / (max_vals - min_vals)


    # Plot the ESF and LSF
    #fig, ax = plt.subplots()
    #ax.plot(x_lsf, normalized_data)
    #ax.plot(x_values, sorted_pixels)
    #plt.show()

    # Make the MTF-50

    # Perform the discrete Fourier transform (DFT)
    fft_lsf = np.fft.fft(lsf)

    # Calculate the absolute value of the Fourier transform
    abs_fft_lsf = np.abs(fft_lsf)

    # Normalize the MTF to values between 0 and 1
    mtf = abs_fft_lsf / abs_fft_lsf[0]

    # Calculate the corresponding frequency values
    sampling_rate = 2  # Frequency
    n = len(lsf)
    freq = np.fft.fftfreq(n, d=1.0 / sampling_rate)


    # Filter the data to include only points where x > 0
    x_filtered = freq[freq > 0]
    y_filtered = mtf[freq > 0]


    # plt.plot(x_filtered, y_filtered)
    # plt.xlabel('Spatial Frequency (cycles per pixel)')
    # plt.ylabel('MTF')
    # plt.title('Modulation Transfer Function (MTF)')
    # plt.grid(True)
    # plt.show()


    # Find the frequency where MTF drops to 50% (0.5)
    mtf_threshold = 0.5  # MTF at 50%
    cut_off_index = np.where(y_filtered <= mtf_threshold)[0][0]
    #print(cut_off_index)

    # Calculate the cut-off frequency
    cut_off_mtf = y_filtered[cut_off_index]
    cut_off_frequency = x_filtered[cut_off_index]

    #print(f"Cut-off MTF: {cut_off_mtf}")

    #print(f"Cut-off Frequency: {cut_off_frequency}")

    #First index
    # index 8 and value 0.44 for 20
    #index 14 and value 0.49 for REF
    #index 12 and value 0.45 for 22
    #index 15 and value 0.49 for 36
    #index 18 for 32
    #index 9 for 21
    #index 17 for 26
    #index 12 for 19

    if cut_off_index > 12:
        #print("Image is Sharp")
        return True
    else:
        #print("Image is not Sharp")
        return False

