import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from helper_functions import grayscale, gaussian_blur, canny, \
            region_of_interest, hough_lines

for img in os.listdir("test_images/"):
    image = mpimg.imread("test_images/"+img)
    plt.imshow(image)
    plt.show()

    grey_img = grayscale(image)
    blurred_img = gaussian_blur(grey_img, 5)
    img_edges = canny(blurred_img, 50, 150)

    # defining mask vertices
    vertices = np.array([
        [
            (50, image.shape[0]),
            (400, 320),
            (550, 320),
            (900, image.shape[0]),
        ]
    ])

    masked_img = region_of_interest(img_edges, vertices)

    # defining hough_lines variables
    rho = 1
    theta = np.pi / 180
    threshold = 20
    min_line_length = 50
    max_line_gap = 25

    img_lines = hough_lines(masked_img, rho, theta, threshold,
                            min_line_length, max_line_gap)
