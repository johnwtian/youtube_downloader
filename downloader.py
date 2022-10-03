
#Credit https://www.youtube.com/watch?v=vEQ8CXFWLZU&t=278s
from pytube import YouTube
from sys import argv
from pathlib import Path

class YouTubeDownloader(object):

    def __init__(self, link):
        # https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder
        self.downloads_path = str(Path.home() / "Downloads")
        self.link = link #argv[1]
        self.yt = YouTube(link)

    def print_stats(self):
        print("Title: ", self.yt.title)
        print("View: ", self.yt.views)

    def download(self):
        yd = self.yt.streams.get_highest_resolution()
        yd.download(self.downloads_path)

def main(link):
    downloader = YouTubeDownloader(link)
    print("Download Started!")
    downloader.download()
    print("Done!")

if __name__ == "__main__":

    print("Welcome to YouTube downloader!")

    format = input("Select single (L)ink or (F)ile download: ")

    if (format.lower() == "l"):
        # Single link
        link = input("Link: ")
        main(link)
    elif (format.lower() == "f"):
        # File
        pass
    else:
        print("Invalid option!")

    