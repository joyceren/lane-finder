import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from helper_functions import grayscale, gaussian_blur, canny, \
            region_of_interest, hough_lines, weighted_img


def find_lanes_in_image(img):
    grey_img = grayscale(img)
    blurred_img = gaussian_blur(grey_img, 9)
    img_edges = canny(blurred_img, 30, 100)

    # defining mask vertices
    vertices = np.array([
        [
            (200/960*img.shape[1], 500/540*img.shape[0]),
            (420/960*img.shape[1], 340/540*img.shape[0]),
            (550/960*img.shape[1], 340/540*img.shape[0]),
            (800/960*img.shape[1], 500/540*img.shape[0]),
        ]
    ], dtype=np.int32)

    masked_img = region_of_interest(img_edges, vertices)

    # defining hough_lines variables
    rho = 2
    theta = np.pi / 360
    threshold = 50
    min_line_length = 50
    max_line_gap = img.shape[0]/3

    img_lines = hough_lines(masked_img, rho, theta, threshold, min_line_length,max_line_gap)

    lines_overlay_img = weighted_img(img_lines, img)

    # plt.imshow(lines_overlay_img)
    # plt.show()

    return lines_overlay_img


def test_images():
    for imgName in os.listdir("test_images/"):
        img = mpimg.imread("test_images/" + imgName)
        processed_img = find_lanes_in_image(img)
        plt.imshow(processed_img)
        plt.show()
