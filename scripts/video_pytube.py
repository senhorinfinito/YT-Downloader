#import necessory library
import os
from pytube import YouTube
from pytube.cli import on_progress

def download_individual(path, link):
    resolution = input('Please enter the quality:  ')
    yt = YouTube(link, on_progress_callback=on_progress)
    t = yt.streams.filter(res =f'{resolution}p')
    try:
        print('considered specified solution')
        t[0].download(path)
    except:
        print("picked default resolution")
        t = yt.streams.get_highest_resolution().download(path)
    print(f'{yt.title}  Downloaded')

if __name__ == '__main__':
    path = input('Enter the save path: ')
    if not os.path.exists(path):
        os.makedirs(path)
    url = input('Input video url:  ')
    download_individual(path, url)