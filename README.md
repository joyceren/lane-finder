# **Lane Finding** 
<!-- [![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" /> -->

Overview
---
This project serves demonstrates how one could process images and videos to procedurally find the guiding road lanes, using canny edge detection, a region of interest mask, and hough line calculation.

Files
---
Starting in the findlanes.py file, there is the find_lanes_in_images function, (which will take an inputed image and display the processed image) and the find_lanes_in_videos function (which takes a file location and saves a processed video in a new designated location). Also included are functions from the helper_functions.py file.

The test.py file is where the tests are. Run this file to process the images and videos in the test_images and test_videos folder.

Included also are the jupyter notebook file and a Project_Writeup.md as per project rubric requirement.