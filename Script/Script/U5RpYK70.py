import os  # importing os module for interacting with operating system
import random  # importing random module for generating random values
from moviepy.editor import *  # importing necessary classes from moviepy module
from moviepy.video.VideoClip import TextClip

# creating a list of .mp4 files in the 'Episodes' directory using list comprehension
mp4_files = [file for file in os.listdir('Episodes') if file.endswith('.mp4')]
# randomly choosing a file from the list
random_file = random.choice(mp4_files)
# creating the full path of the chosen video file
video_file = os.path.join('Episodes', random_file)
# loading the video file using VideoFileClip() class
video = VideoFileClip(video_file)
# getting the duration of the video
duration = video.duration
# choosing a random start time between 30 seconds and 60 seconds before the end of the video
start = random.uniform(30, max(30, duration - 60))
# choosing a random length between 20 seconds and 40 seconds
lenght = random.randint(20, 40)
# extracting the clip from the video using the chosen start time and length
clip = video.subclip(start, start + lenght)
# getting the width and height of the clip
width, height = clip.size
# calculating the aspect ratio of the clip
aspect_ratio = width / height
# calculating the new width of the clip with a 16:9 aspect ratio
new_width = int(height * 9/16)
# calculating the left margin to center the clip horizontally
left_margin = (width - new_width) / 2
# cropping the clip to the new width and centering it horizontally
clip = clip.crop(x1=left_margin, x2=left_margin + new_width)
# increasing the speed of the clip by 10%
clip = clip.speedx(factor=1.1)
# flipping the clip horizontally
clip = clip.fx(vfx.mirror_x)
# creating a TextClip object with the desired text and properties
text = "Surprise in comments\nEnter & WIN!"
txt_clip = TextClip(text, fontsize=15, color='white', font='Arial-Bold')
# setting the position of the text clip to be centered near the bottom of the screen
txt_clip = txt_clip.set_position(('center', 0.8), relative=True)
# creating a CompositeVideoClip object by combining the clip and text clip
final_clip = CompositeVideoClip([clip, txt_clip])
# setting the duration of the final clip to be the same as the cropped clip
final_clip.duration = clip.duration
# writing the final clip to a file named 'clip.mp4'
final_clip.write_videofile("clip.mp4")

















# -- https://cracked.io/Evil-Corporation