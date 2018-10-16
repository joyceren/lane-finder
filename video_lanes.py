from moviepy.editor import VideoFileClip
import os
from find_lanes import find_lanes_in_image, test_images


for videoName in os.listdir("test_videos"):
    print(videoName)
    clip = VideoFileClip("test_videos/" + videoName)
    processed_clip = clip.fl_image(find_lanes_in_image)
    output_name = 'test_videos_output/' + videoName
    processed_clip.write_videofile(output_name, audio=False)

# test_images()

videoName = "challenge.mp4"