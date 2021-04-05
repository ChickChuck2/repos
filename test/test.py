from pytube import YouTube, Playlist

PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLyORnIW1xT6waC0PNjAMj33FdK2ngL_ik'
playlist = Playlist(PLAYLIST_URL)

for url in playlist:
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    
    stream.download(output_path='playlist')