from yt_dlp import YoutubeDL
import scrapetube, os

c = input('Enter YT Channel Here: ')

videos = scrapetube.get_channel(channel_url = c)
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
            os.rename(search_title, f'{i+1} {video_title}.mp4')
        except:
            print(f'FAILED TO RENAME FILE {search_title}')