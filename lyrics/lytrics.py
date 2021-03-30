import lyricsgenius
import pyautogui
import time

genius = lyricsgenius.Genius("sIEUYbTfkwI59C3dQMfPx7Zwo_9u_oOdmvw3VJzPIm54HbCOtFxq6ONIohDUsJnn")

artista = input("Digite o nome do artista: ")
artist = genius.search_artist(artista, max_songs=0)

musica = input(f"Agora digite o nome da musica de {artista}: ")
song = artist.song(musica)


letra = song.lyrics
fraseSplit = letra.split("\n")
contar = len(fraseSplit)

for i in range(contar):
    time.sleep(1)
    pyautogui.write(fraseSplit[i])
    pyautogui.keyDown('enter')