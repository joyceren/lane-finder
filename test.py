import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from find_lanes import find_lanes_in_image
from video_lanes import find_lanes_in_video

for imgName in os.listdir("test_images/"):
    img = mpimg.imread("test_images/" + imgName)
    processed_img = find_lanes_in_image(img)
    plt.imshow(processed_img)
    plt.show()

for videoName in os.listdir("test_videos"):
    print(videoName)
    output_name = 'test_videos_output/' + videoName
    find_lanes_in_video('test_videos/'+videoName, output_name)
