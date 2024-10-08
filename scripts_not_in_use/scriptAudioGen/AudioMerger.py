import os
from moviepy.editor import concatenate_audioclips, AudioFileClip
from pydub import AudioSegment
import time


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


def adjust_music(music):
    # Adjust the volume of the music
    music = music - 28
    #Adjust the start of the music
    music = music[10000:]
    return music
def add_music_based_on_sentiment(audio_file_path, sentiment):

    # Define paths to your music files
    positive_music_path = "scripts/scriptAudioGen/music/sappheiros-embrace.mp3"
    negative_music_path = "scripts/scriptAudioGen/music/DangerousToys-SefChol.mp3"
    neutral_music_path = "scripts/scriptAudioGen/music/lost-ambient-lofi-60s-10821.mp3" #add more types

    # Load audio files as MP3
    positive_music = AudioSegment.from_mp3(positive_music_path)
    negative_music = AudioSegment.from_mp3(negative_music_path)
    neutral_music = AudioSegment.from_mp3(neutral_music_path)

    # Load the main audio file as MP3
    main_audio = AudioSegment.from_mp3(audio_file_path)


    # Overlay music based on sentiment
    if sentiment == "Positive":
        output_audio = main_audio.overlay(adjust_music(positive_music))
    elif sentiment == "Negative":
        output_audio = main_audio.overlay(adjust_music(negative_music))
    else:
        output_audio = main_audio.overlay(adjust_music(neutral_music))


    # Export the final audio as MP3
    # output_audio.export("server/scripts/scriptAudioGen/final_speech_with_music.mp3", format="mp3")
    output_audio.export("final_speech_with_music.mp3", format="mp3")

    try:
        os.remove("final_speech.mp3")
    except PermissionError:
        print(f"Could not remove file, (in use by another process)")
    # time.sleep(3) #gives time for audio file to get uploaded


#Note: Punctuation in the script is really important for appropriate pauses.


