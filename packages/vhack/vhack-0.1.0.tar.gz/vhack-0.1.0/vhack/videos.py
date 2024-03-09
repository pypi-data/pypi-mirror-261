class Videos:
    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    def __repr__(self):
        return f"\n {self.name} | duration  {self.duration}mins \n  {self.link}"


list_videos = [
    Videos("Python en 2 minutos", 2, "https://youtu.be/GnaDddI9sQs"),
    Videos("Maquina Sequel", 17, "https://youtu.be/Q-ITw2JlKFk"),
    Videos("Maquina Cocodrile", 25, "https://youtu.be/0pdMzpgNt9U")
]

def show_videos():
    for video in list_videos:
        print(video)

def video_by_name(name):
    for video in list_videos:
        if video.name == name:
            return video
    return ValueError("[!] Video not found")
