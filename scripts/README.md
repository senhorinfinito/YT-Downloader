## PYTUBE- Donwloading youtube videos

* PYTUBE is a python library  can used to download videos from YouTube.

To start downloading clone the repository & to fulfill pre-requisites run following code.

```pip install -r requirements.txt```

-  To download single video
    * To download single video  follow:
    ```python video_pytube.py```

    It will ask for following things shown with a sample example.
    * Enter the save path:  ***Enter your save path***  ex . ```C:\Users\myuser\Desktop\videos```
    * Input vide URL : ***Enter video URL copied from YouTube***  ex.```https://youtu.be/2NIytNJr6hw```
    * Please enter the quality : ***please enter the video resolution such as ```144,240,360,480,720,1080,1440``` etc.***

  It will save your  video into save path.

  - To download complete playlist.
    * Follow steps which are mentioned below to downlead complete playlist.
    ```python playlist_pytube.py```
    
    After running  provide proper inputs mentioned below
    * Enter the save path:  ***Enter your save path***   ex . ```C:\Users\myuser\Desktop\videos```
    * Input vide URL : ***Enter playlist URL copied from YouTube***  ex:- ```https://youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3```
    * Please enter the quality : ***please enter the video resolution such as ```144,240,360,480,720,1080,1440``` etc.***

  - To download multiple videos using .txt files
    * refer following steps to download multiple videos
    First needs to copy all video links into a '.txt' file. refer ```sample.txt``` for input file format.
    run ```multiple_video_pytube.py```
    * Enter the save path:  ***Enter your save path***   ex . ```C:\Users\myuser\Desktop\videos```
    * Input txt path : ***Enter text file where all URL copied from YouTube***  
    * Please enter the quality : ***please enter the video resolution such as ```144,240,360,480,720,1080,1440``` etc.***
