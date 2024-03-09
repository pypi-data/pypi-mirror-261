from .videos import list_videos

def total_duration():
    return sum(video.duration for video in list_videos)
