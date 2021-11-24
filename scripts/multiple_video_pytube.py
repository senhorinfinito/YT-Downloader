import re
import os
from tqdm import tqdm
from pytube import Playlist
from pytube import YouTube
from pytube.cli import on_progress

def get_links(file_name):
    """
    returns a list of links which found in *.txt file
    """
    fname = (open(file_name))  #add path with file name 
    links = ([(i.strip().split()) for i in fname])
    return links 
def download_pytube_video(path,file_path):
    """
    links_list : this is list of urls from function get links 
    qulaity : You can choose quality based on the video available on online
    ex: 144p, 240p, 360p, 480p, 720p, 1080p
    """
    links_list = get_links(file_path)
    quality = input('enter the video quality (Resolution): ')
    for i, j in enumerate(links_list):
        yt_stream = YouTube(j[0], on_progress_callback= on_progress )
        t = yt_stream.streams.filter(res = f'{quality}p')
        try:
            t[0].download(path)
            print('considered specified solution')
        except:
            t = yt_stream.streams.get_highest_resolution().download(path)
            print("picked default resolution")
        print(f'video {yt_stream.title} {(i+1)}  Downloaded')

if __name__ == '__main__':
    save_path = input('Enter save path :  ')
    input_file = input('Enter input txt path with file :  ')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    try:
        video_links= get_links(input_file)
    except:
        print('[INFO]::  Please provide proper .txt file path with file name')
    
    download_video  = download_pytube_video(save_path, input_file)
    