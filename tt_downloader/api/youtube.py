from pytube import YouTube

class short:

    path = None
    link = None
    name = None
    output_path = f"youtube_shorts/"

    def __init__(self, link, name) -> None:
        self.link = link
        self.name = name

    def download(self):

        video = YouTube(self.link).streams.get_by_itag(22)

        video.download(filename=f"{self.name}.mp4", output_path=self.output_path)

        self.path = self.output_path + f"{self.name}.mp4"