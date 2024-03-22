import numpy as np
from moviepy.editor import VideoClip, AudioFileClip, CompositeVideoClip
from PIL import Image
import os
import random

def choose_image():
    random_image_number = random.randint(1, 23)
    # images_folder = os.path.join(os.getcwd(), "shared","photos")
    images_folder = os.path.join(os.getcwd(), "photos")

    # Construct the filename based on the random number
    random_image_filename = f"BGImage{random_image_number}.png"
    random_image_path = os.path.join(images_folder, random_image_filename)
    return random_image_path

def generate_static_video():
    # File paths
    # image_path = "photos/BGImage3.png"
    # image_path = "text_to_image.png"
    #if the image generated is not suitable
    image_path = choose_image()
    # Construct the paths to the files in the 'tmp' folder
    tmp_folder = os.path.join(os.getcwd(), "tmp")
    # image_path = os.path.join(tmp_folder, 'text_to_image.png')
    mp3_path = os.path.join(tmp_folder, 'final_speech_with_music.mp3')
    output_video_path = os.path.join(tmp_folder, 'output_video.mp4')

    # Load image
    image = Image.open(image_path)

    # Convert PIL image to NumPy array
    image_array = np.array(image)

    # Get image dimensions
    height, width, _ = image_array.shape

    image_duration = AudioFileClip(mp3_path).duration

    # Create a VideoClip with a static image
    video_clip = VideoClip(lambda t: image_array, duration=image_duration)

    # Load the audio clip
    audio_clip = AudioFileClip(mp3_path)

    # Composite the video with the audio
    final_video_clip = CompositeVideoClip([video_clip.set_audio(audio_clip)])

    # Write the final video to an MP4 file
    final_video_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac", fps=30, threads=4, write_logfile=False)

if __name__ == '__main__':
     generate_static_video()