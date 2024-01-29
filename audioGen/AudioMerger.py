import os
from moviepy.editor import concatenate_audioclips, AudioFileClip

def merge_audio_files():
    # List all files in the folder with the ".mp3" extension
    input_audio_files = [file for file in os.listdir() if file.endswith(".mp3")]

    # Dynamically create a list of AudioFileClip objects
    input_audioclips = [AudioFileClip(file) for file in input_audio_files]

    # Concatenate the audio clips
    final_audio = concatenate_audioclips(input_audioclips)

    # Export the final merged audio to an MP3 file
    final_audio.write_audiofile('final_speech.mp3')

    # Close the AudioFileClip instances
    for audioclip in input_audioclips:
        audioclip.close()

    # Remove all other MP3 files
    for file in input_audio_files:
        if file != 'final_speech.mp3':
            try:
                os.remove(file)
            except PermissionError:
                print(f"Could not remove file: {file} (in use by another process)")



#Note: Punctuation in the script is really important for appropriate pauses.
