import os

def run():
    try:
        os.remove("final_speech_with_music.mp3")
        os.remove("text_to_image.png")
        os.remove("output_video.mp4")
    except PermissionError:
        print(f"Could not remove file, (in use by another process)")

if __name__ == "__main__":
    run()