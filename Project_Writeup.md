# **Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

---

### Reflection

### 1. Pipeline

In order to get to the final image with detected lines, each image is processed as such:
- 1. Image is converted to grayscale
- 2. Noise is filtered out of the image using Gaussian smoothing
- 3. The edges of shapes are found by checking the gradient derivative with the Canny algorithm
- 4. Next, we define the vertices of our region of interest
- 5. Those vertices are used to create a mask which is overlayed on our image of edge points
- 6. We then calculate which points have the highest probability of being in a line together, by calculating their values in Hough space
- 7. This returns the endpoints of the most likely lines in the image. We take the average intercepts and coefficients of those lines and calculate one line to represent them all
- 8. That line is then drawn on the original image and our fully processed image is returned

In addition to averaging the lines to form one line, I also tried to  account for potential outlier lines by comparing each line's slope to the current running average within 2 standard deviations.

I also updated the vertices to scale with the image size


### 2. Challenges

The processed challenge video still has some flaws.

For example, there is a hard line in the road where new black asphalt changes to old, light, concrete. The contrast between these two is much higher than the contrast between the light concrete and the yellow line. As such, this confuses our edges detection.

I tried increasing the minimum line length parameter, but that only made it so that the little road turtles were no longer being caught.

I also tried decreasing the lower color threshold on our canny detection, and increasing our blur, but because the contrast so much higher between the new road and the old road, it did not do much to solve the problem.

I also tried increasing the hough_line threshold, but the line in the asphalt is almost as straight as the guiding road lines, so it didn't make much impact either.


### 3. Possible Improvements

Some ideas to address the issues I encountered in the challenge video:
- adding color selection: most road lines are either yellow or white, and that might mitigate the effects of other hard lines
- starting out with a guide so the program knows what to expect in terms of our lines and can better get rid of outliers
