from yt_dlp import YoutubeDL
import scrapetube, os, re
os.listdir(os.getcwd())

c = input('Enter Playlist URL Here: ')
play_id = ''
for i, char in enumerate(c):
    if char == '=':
        play_id += c[i+1:]
        break
print(play_id)

videos = scrapetube.get_playlist(play_id)
links = []
for video in videos:
    links.append('https://www.youtube.com/watch?v='+video['videoId'])


with YoutubeDL() as ydl: 
    for i, link in enumerate(links):
        info_dict = ydl.extract_info(link, download=False)
        video_title = info_dict.get('title', None)
        video_id = info_dict.get('id', None)
        search_title = f'{video_title} [{video_id}].mp4'



    
        try:
            ydl.download(link)
        except:
            print(f'FAILED TO DOWNLOAD {video_title}')
        try:
            os.rename(search_title, f'{i+1} {video_title}')
        except:
            print(f'FAILED TO RENAME FILE {search_title}')