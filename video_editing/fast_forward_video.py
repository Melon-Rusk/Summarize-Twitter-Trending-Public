from moviepy.editor import VideoFileClip

# Open the video file
def fast_forward_video():
    clip = VideoFileClip('store_data\\video_disclaimer_video_disclaimer_.mp4')

# Create a new video clip that is twice as fast as the original
    fast_clip = clip.speedx(2)

# Save the edited video
    fast_clip.write_videofile('store_data\\video_disclaimer_video_disclaimer_2.mp4')

# fast_forward_video()

def crop_video():
    clip = VideoFileClip('store_data\\video_disclaimer_video_disclaimer_.mp4')

# Crop the video by specifying the coordinates of the top-left and bottom-right corners of the cropped area
    cropped_clip = clip.crop(x1=0, y1=0, x2=960, y2=540)

# Save the edited video
    cropped_clip.write_videofile('store_data\\video_disclaimer_video_disclaimer_2.mp4')

crop_video()

#9:16