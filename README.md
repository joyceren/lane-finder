# **Lane Finding* 
<!-- [![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" /> -->

Overview
---
This project serves demonstrates how one could process images and videos to procedurally find the guiding road lanes, using canny edge detection, a region of interest mask, and hough line calculation.

Files
---
Starting in the findlanes.py file, there is the find_lanes_in_images function, (which will take an inputed image and display the processed image) and the find_lanes_in_videos function (which takes a file location and saves a processed video in a new designated location). Also included are functions from the helper_functions.py file.

The test.py file is where the tests are. Run this file to process the images and videos in the test_images and test_videos folder.

Included also are the jupyter notebook file and the project writeup as per project rubric requirement.

Creating a Great Writeup
---
For this project, a great writeup should provide a detailed response to the "Reflection" section of the [project rubric](https://review.udacity.com/#!/rubrics/322/view). There are three parts to the reflection:

1. Describe the pipeline

2. Identify any shortcomings

3. Suggest possible improvements

We encourage using images in your writeup to demonstrate how your pipeline works.  

All that said, please be concise!  We're not looking for you to write a book here: just a brief description.

You're not required to use markdown for your writeup.  If you use another method please just submit a pdf of your writeup. Here is a link to a [writeup template file](https://github.com/udacity/CarND-LaneLines-P1/blob/master/writeup_template.md).
