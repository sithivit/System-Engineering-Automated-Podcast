import os

def run():
    try:
        os.remove(os.path.join("tmp", "final_speech_with_music.mp3"))
        os.remove(os.path.join("tmp", "text_to_image.png"))
        os.remove(os.path.join("tmp", "output_video.mp4"))
    except PermissionError:
        print(f"Could not remove file, (in use by another process)")

if __name__ == "__main__":
    run()