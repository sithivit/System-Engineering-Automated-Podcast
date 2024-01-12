from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.editor import concatenate_videoclips

class AudioEdit:
    def __init__(self):
        pass
    
    def combineVideos(video_1, video_2):
        video_1 = VideoFileClip(video_1)
        video_2 = VideoFileClip(video_2)

        # video_1 = video_1.subclip(0,3)
        # video_2 = video_2.subclip(5,8)

        output = concatenate_videoclips([video_1, video_2])
        output.write_videofile("video_new.mp4")

        output.close()
        video_1.close()
        video_2.close()


    def addAudioToVideo(video_path, audio_path):

        videoclip = VideoFileClip(video_path)
        audioclip = AudioFileClip(audio_path)

        audioclip = audioclip.subclip(0, videoclip.duration)
        videoclip.audio = audioclip
        videoclip.write_videofile("video_new.mp4")

        videoclip.close()
        audioclip.close()
