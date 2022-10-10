
#Credit https://www.youtube.com/watch?v=vEQ8CXFWLZU&t=278s
from pickletools import string1
import string
from pytube import YouTube
from sys import argv
from pathlib import Path
import argparse
import os

class YouTubeDownloader(object):

    def __init__(self, link):
        # https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder
        self.downloads_path = str(Path.home() / "Downloads")
        self.link = link #argv[1]
        self.yt = YouTube(link)

    def print_stats(self):
        print("Title: ", self.yt.title)
        print("View: ", self.yt.views)

    def download(self, output= None):
        yd = self.yt.streams.get_highest_resolution()
        if(output):
            yd.download(output)
        else:
            yd.download(self.downloads_path)

def return_urls(filepath):
    urls = []
    
    with open(filepath) as f:
        path = f.readline()
        while(path is not None):
            urls.append(path)
            path = f.readline()
    return urls

def progress_func(*args):
    print(args)

def main(link, output= None):
    #try:
    downloader = YouTubeDownloader(link)
    # downloader.register_on_progress_callback(progress_func)
    print(f"/n/'{downloader.yt.title}/' Download Started!")
    downloader.download(output)
    print("Done!")
    #except:
    #    print(f"Could not find link {link}!")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description= "Downloads YouTube Videos")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--link", help= "Provide link to Youtube URL")
    group.add_argument("-f", "--filepath", help= "Provide filepath to input Youtube URLs")
    parser.add_argument("-o", "-output_path", help="Optional - output path location")
    parser.add_argument("-p", "--prompt", choices=[True, False], help="Run using prompts")
    parser.add_argument("-r", "--resolution", choices=["high", "low"], default="low", help="Specify high or low resolution")


    args = parser.parse_args()

    # print(args)

    if((args.prompt == True)):
        #Process using prompt method
        print("Welcome to YouTube downloader!")
        format = input("Select single (L)ink or (F)ile download: ")

        if (format.lower() == "l"):
            # Single link
            link = input("Link: ")
            main(link)
        elif (format.lower() == "f"):
            # File
            print(f"Current filepath: {os.getcwd()}")
            path = input("Path: ")
            links = return_urls(path)
            for link in links:
                main(link)
        else:
            print("Invalid option!")
    elif((args.link == None) & (args.filepath == None)):
        print("Need to provide link or filepath!")
    else:
        #Process filepath or link
        print("Welcome to YouTube downloader!")
        if(args.link is not None):
            #Process link
            main(args.link)
        else:
            #Process filepath
            links = return_urls(args.filepath)
            for link in links:
                main(link)



