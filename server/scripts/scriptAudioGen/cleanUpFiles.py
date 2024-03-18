import os

def run():
    try:
        os.remove(os.getcwd() + "\\final_speech_with_music.mp3")
        os.remove(os.getcwd() + "\\text_to_image.png")
        os.remove(os.getcwd() + "\\output_video.mp4")
    except PermissionError:
        print(f"Could not remove file, (in use by another process)")

if __name__ == "__main__":
    run()