import os
from moviepy.editor import concatenate_audioclips, AudioFileClip
from pydub import AudioSegment

def merge_audio_files():
    # Define the path to the tmp folder
    tmp_folder = os.path.join(os.getcwd(), "tmp")

    # List all MP3 files in the tmp folder
    input_audio_files = [os.path.join(tmp_folder, file) for file in os.listdir(tmp_folder) if file.endswith(".mp3")]

    # Dynamically create a list of AudioFileClip objects
    input_audioclips = [AudioFileClip(file) for file in input_audio_files]

    # Concatenate the audio clips
    final_audio = concatenate_audioclips(input_audioclips)

    # Export the final merged audio to an MP3 file in the tmp folder
    final_audio.write_audiofile(os.path.join(tmp_folder, 'final_speech.mp3'))

    # Close the AudioFileClip instances
    for audioclip in input_audioclips:
        audioclip.close()

    # Remove all other MP3 files from the tmp folder
    for file in input_audio_files:
        if file != os.path.join(tmp_folder, 'final_speech.mp3'):
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
    # Define the path to the tmp folder
    tmp_folder = os.path.join(os.getcwd(), "tmp")

    # root_path = os.path.join(os.getcwd(), "shared","music")
    root_path = os.path.join(os.getcwd(), "shared", "music")
    # Define paths to your music files
    positive_music_path = os.path.join(root_path, "sappheiros-embrace.mp3")
    negative_music_path = os.path.join(root_path, "DangerousToys-SefChol.mp3")
    neutral_music_path = os.path.join(root_path, "lost-ambient-lofi-60s-10821.mp3") #add more types

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

    # Export the final audio as MP3 in the tmp folder
    output_audio.export(os.path.join(tmp_folder, 'final_speech_with_music.mp3'), format="mp3")

    try:
        os.remove(os.path.join(tmp_folder, "final_speech.mp3"))
    except PermissionError:
        print(f"Could not remove file, (in use by another process)")


#Note: Punctuation in the script is really important for appropriate pauses.


