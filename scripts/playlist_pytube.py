# import necessory library
import re
import os
from pytube import Playlist
from pytube import YouTube
from pytube.cli import on_progress

#  download youtube playlist
def download_from_playlist(path, playlist_url):
    """need to pass playlist url"""
    all_urls = []
    playlist = Playlist(playlist_url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for url in playlist.video_urls:
        all_urls.append(url)
    resolution = input('Please enter the quality:  ')
    for i, j in enumerate(all_urls):
        yt = YouTube(j, on_progress_callback=on_progress)
        t = yt.streams.filter(res =f'{resolution}p')
        try:
            print('considered specified solution')
            t[0].download(path)
        except:
            print("picked default resolution")
            t = yt.streams.get_highest_resolution().download(path)
        print(f'video {yt.title} {(i+1)}  Downloaded')

if __name__ == '__main__':
    path = input('Enter the save path: ')
    if not os.path.exists(path):
        os.makedirs(path)
    url = input('Input playlist url:  ')
    download_from_playlist(path, url)