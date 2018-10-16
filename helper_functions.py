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
    left_starting_vertices = [
        200/960*img.shape[1],
        500/540*img.shape[0],
        420/960*img.shape[1],
        340/540*img.shape[0]
    ]
    right_starting_vertices = [
        550/960*img.shape[1],
        340/540*img.shape[0],
        800/960*img.shape[1],
        500/540*img.shape[0]
    ]

    def calculate_slope(x1, y1, x2, y2):
        xchange = x2-x1
        ychange = y2-y1
        if xchange is not 0 and ychange is not 0:
            slope = ychange/xchange
            b = x1-(slope*y1)
            return [slope, b]

    left = [calculate_slope(*left_starting_vertices)]
    right = [calculate_slope(*right_starting_vertices)]

    for line in lines:
        for x1, y1, x2, y2 in line:
            coefficients = calculate_slope(x1, y1, x1, y2)
            if coefficients[0] < 0 and x1 < img.shape[1]/2 and x2 < img.shape[1]/2:
                if len(left) < 2:
                    left.append(coefficients)
                elif coefficients[0] > average_slope(left)-(2*stdev([i[0] for i in left])) and coefficients[0] < average_slope(left)+(2*stdev([i[0] for i in left])):
                    left.append(coefficients)
            elif coefficients[0] > 0 and x1 >= img.shape[1]/2 and x2 >= img.shape[1]/2:
                if len(right) < 2:
                    right.append(coefficients)
                elif coefficients[0] > average_slope(right)-(2*stdev([i[0] for i in right])) and coefficients[0] < average_slope(right)+(2*stdev([i[0] for i in right])):
                    right.append(coefficients)
        
    print(left)
    print(right)

    def create_coords(side):
        if len(side) is not 0:
            slope = sum([e[0] for e in side]) / len(side)
            if math.isnan(slope) is False:
                b = sum([e[1] for e in side]) / len(side)
                return [
                    (int(slope*img.shape[0]+b), img.shape[0]),
                    (int(slope*(340/540*img.shape[0])+b), int(340/540*img.shape[0]))
                ]
    
    # sides = [create_coords(left), create_coords(right)]

    # for coords in sides:
    #     if coords:
    #         cv2.line(img, coords[0], coords[1], color, thickness)

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
