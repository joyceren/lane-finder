import math
import numpy as np
import cv2
from statistics import stdev


def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)


def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices):
    """
    Applies an image mask.


    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    `vertices` should be a numpy array of integer points.
    """
    # defining a blank mask to start with
    mask = np.zeros_like(img)

    # defining a color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    # returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def average_slope(lst):
    return sum([i[0] for i in lst]) / len(lst)

def draw_lines(img, lines=[], color=[255, 0, 0], thickness=2):
    left = []
    right = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            y_slope = (x2-x1)/(y2-y1)
            x_slope = (y2-y1)/(x2-x1)
            b = x1-(y_slope*y1)
            if x_slope < 0 and x1 < img.shape[1]/2 and x2 < img.shape[1]/2:
                if len(left) < 2:
                    left.append([y_slope, b])
                elif y_slope > average_slope(left)-(2*stdev([i[0] for i in left])) and y_slope < average_slope(left)+(2*stdev([i[0] for i in left])):
                    left.append([y_slope, b])
            elif x_slope > 0 and x1 >= img.shape[1]/2 and x2 >= img.shape[1]/2:
                if len(right) < 2:
                    right.append([y_slope, b])
                elif y_slope > average_slope(right)-(2*stdev([i[0] for i in right])) and y_slope < average_slope(right)+(2*stdev([i[0] for i in right])):
                    right.append([y_slope, b])

    def create_coords(side):
        if len(side) is not 0:
            slope = sum([e[0] for e in side]) / len(side)
            if slope == float('Inf'):
                return None
            else:
                b = sum([e[1] for e in side]) / len(side)
                return [
                    (int(slope*img.shape[0]+b), img.shape[0]),
                    (int(slope*(340/540*img.shape[0])+b), int(340/540*img.shape[0]))
                ]
    
    sides = [create_coords(left), create_coords(right)]

    for coords in sides:
        if coords:
            cv2.line(img, coords[0], coords[1], color, thickness)

def draw_lines_basic(img, lines=[], color=[255, 0, 0], thickness=2):
    for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(
        img, rho, theta, threshold, np.array([]),
        minLineLength=min_line_len,
        maxLineGap=max_line_gap
    )
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines, [255, 0 , 0], 10)
    return line_img

#  Python 3 has support for cool math symbols.


def weighted_img(img, initial_img, α=0.8, β=1., γ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.

    `initial_img` should be the image before any processing.

    The result image is computed as follows:

    initial_img * α + img * β + γ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, γ)
