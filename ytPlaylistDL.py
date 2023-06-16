from yt_dlp import YoutubeDL
import scrapetube

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

ydl = YoutubeDL()
ydl.download(links)