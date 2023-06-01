from yt_dlp import YoutubeDL
import scrapetube

c = input('Enter YT Channel Here: ')

videos = scrapetube.get_channel(channel_url = c)
links = []
for video in videos:
    links.append('https://www.youtube.com/watch?v='+video['videoId'])


ydl = YoutubeDL()
ydl.download(links)
