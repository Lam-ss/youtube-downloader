# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=7W4PD4BN3eY&list=PLcvhF2Wqh7DNVy1OCUpG3i5lyxyBWhGZ8&index=70")
# yt = yt.get('mp4', '720p')
# # yt.download('/path/to/download/directory')
# yt.download()

from pytube import YouTube
import os
from pytube import Playlist
from pytube import Channel


def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    print(f'    downloaded...  {yt.title}')
# downloadYouTube('https://www.youtube.com/watch?v=7W4PD4BN3eY&list=PLcvhF2Wqh7DNVy1OCUpG3i5lyxyBWhGZ8&index=70', './videos/FindingNemo1')


p = Playlist(
    'https://www.youtube.com/playlist?list=PL0FGkDGJQjJG9eI85xM1_iLIf6BcEdaNl')
print(f'Downloading: {p.title}')
for i in p.video_urls:
    if '#14' in YouTube(i).title:
        downloadYouTube(i, './../../youTubeVideos/' + p.title)
        print('+++', p.index(i)+1, YouTube(i).title)


# c = Channel('https://www.youtube.com/c/ITKAMASUTRA/videos')
# print(f'Downloading video from channel: {c.channel_name}')
# for i in c.video_urls:
#     # downloadYouTube(i, './../../youTubeVideos/' + p.title)
#     print('+++', c.index(i)+1, YouTube(i).title)
#     if 'Путь Самурая 2.0' in YouTube(i).title:
#         downloadYouTube(i, './../../youTubeVideos/' + c.channel_name)
