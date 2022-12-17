################################################
# Import Library
import re
import sys
from pathlib import Path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
sys.path.append(str(Path(__file__).resolve().parent))
sys.path.append(str(Path(__file__).resolve().parent.parent))

from video_editing.create_audio import get_audio_file
from video_editing.create_image import get_image_file


def creat_video_animation(heading,text,file_name):
    folder = 'store_data'
    heading_name = re.sub("[^0-9a-zA-Z]+","_",heading).lower()
    file_name = f"{file_name}_{heading_name}"
    text = text.strip()
    text = text.replace("  "," ")
    text = text.capitalize()
    audio_path = get_audio_file(heading=heading,summary=text,file_name=file_name)
    image_path = get_image_file(heading,text, file_name, folder)

    # # Create a video clip with the image and a typing sound effect
    video = ImageClip(image_path).set_audio(AudioFileClip(audio_path))
    # audio_path = f"{folder}/audio_files/audio_{file_name}.mp3"
    video = video.set_duration(AudioFileClip(audio_path).duration)
    video = video.set_fps(30)
    # Save the video file
    video_file = f"{folder}/video_files/video_{file_name}.mp4"
    video.write_videofile(video_file)
    return video_file

if __name__ == "__main__":
    text = """"Disclaimer: This video is created using crowd sourced data and has not been reviewed to avoid bias. As such, it may contain incorrect information. Please let us know if you find any errors or omissions. The information and views expressed in this video are not necessarily those of the creator and are for educational and entertainment purposes only. The creator cannot be held responsible for any damages or losses arising from the use of the information provided.
    """
    heading = "Disclaimer!."
    file_name = 'disclaimer_video'
    creat_video_animation(heading,text,file_name)

