# Import the necessary libraries and modules
import nltk  # for natural language processing tasks
import datetime  # for date and time manipulation
from TTS.api import TTS  # text to speech package
from moviepy.editor import *  # video editing package
from nltk.tokenize import sent_tokenize  # sentence tokenization from natural language
from moviepy.video.tools.subtitles import SubtitlesClip # tools for reading and displaying subtitles
# Download the 'punkt' module used for sentence tokenization if it has not already been downloaded
nltk.download('punkt')

# Select the model for text-to-speech conversion
model_name = TTS.list_models()[12]
# Create an instance of the selected text-to-speech model
tts = TTS(model_name)
# Open the text file containing the video script, and read the contents
video_script = open('video_script.txt', 'r').read()
# Convert the video script to an audio file using the selected text-to-speech model
tts.tts_to_file(text=video_script, file_path="voiceover.wav")
# Load the newly created audio file, and adjust the volume of the background music
new_audioclip = CompositeAudioClip([
    AudioFileClip("voiceover.wav"),
    AudioFileClip('background_music.mp3').volumex(0.2)
])
# Load the video file that will be used as the background of the final clip
video = VideoFileClip('background_video.mp4')
# Determine the dimensions of the video, and calculate the desired width based on the aspect ratio of 16:9
width, height = video.size
new_width = int(height * 9/16)
# Crop the video to the desired width, centered horizontally
clip = video.crop(x1=(width - new_width) / 2, x2=(width - new_width) / 2 + new_width)
# Set the audio of the cropped video to the adjusted background music and voiceover audio
clip.audio = new_audioclip
# -- https://cracked.io/Evil-Corporation
# Define a function to create subtitles for the video
def subtitles(sentences):
    # Initialize an empty list to store the SRT file contents
    srt_lines = []
    # Initialize the start and end time to zero
    start = datetime.timedelta(seconds=0)
    end = datetime.timedelta(seconds=0)
    # Initialize a counter to keep track of subtitle numbers
    counter = 1
    # Loop over each sentence in the list of sentences passed to the function
    for sentence in sentences:
        # Split the sentence into words
        words = sentence.split()
        # Calculate the number of lines needed for this sentence (assuming each line has 4 words)
        num_lines = len(words) // 4 + 1
        # Loop over each line of the sentence
        for j in range(num_lines):
            # Get the words for this line
            line_words = words[j * 4: (j + 1) * 4]
            # Join the words into a single string to form the line
            line = ' '.join(line_words)
            # Calculate the end time for this line based on the length of the line
            end += datetime.timedelta(seconds=len(line_words) * 0.35)
            # Check if the line is not empty
            if line:
                # Format the start and end times as strings in the SRT format
                start_str = '{:02d}:{:02d}:{:02d},{:03d}'.format(
                    start.seconds // 3600,
                    (start.seconds // 60) % 60,
                    start.seconds % 60,
                    start.microseconds // 1000
                )
                end_str = '{:02d}:{:02d}:{:02d},{:03d}'.format(
                    end.seconds // 3600,
                    (end.seconds // 60) % 60,
                    end.seconds % 60,
                    end.microseconds // 1000
                )
                # Add the subtitle number, start and end times, and line to the SRT list
                srt_lines.append(str(counter))
                srt_lines.append(start_str + ' --> ' + end_str)
                srt_lines.append(line)
                srt_lines.append('')
                # Increment the subtitle counter
                counter += 1
            # Update the start time for the next line
            start = end
    # Join the lines of the SRT file into a single string
    srt_file = '\n'.join(srt_lines)
    # Write the SRT file to disk
    with open("subtitles.srt", "w") as f:
        f.write(srt_file)

# Call the 'subtitles' function with a list of sentences, which are obtained by tokenizing the video script
subtitles(list(filter(None, (sent_tokenize(video_script)))))
# Define a lambda function to generate the subtitle clips from the SRT file
generator = lambda txt: TextClip(txt, font='Arial-Bold', fontsize=20, color='white', bg_color='rgba(0,0,0,0.4)')
# Create the subtitle clip from the SRT file
subtitle_source = SubtitlesClip("subtitles.srt", generator)
# Combine the video clip and the subtitle clip, and adjust the speed and length of the result
clip = CompositeVideoClip([clip, subtitle_source.set_pos(('center', 400))]).speedx(factor=1.1).subclip(0, 60)
# Write the final video clip to disk
clip.write_videofile("clip.mp4")















# -- https://cracked.io/Evil-Corporation