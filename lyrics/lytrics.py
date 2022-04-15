import lyricsgenius
import pyautogui
import time
import pyperclip

genius = lyricsgenius.Genius("sIEUYbTfkwI59C3dQMfPx7Zwo_9u_oOdmvw3VJzPIm54HbCOtFxq6ONIohDUsJnn")

artista = input("Digite o nome do artista: ")
artist = genius.search_artist(artista, max_songs=0)

musica = input(f"Agora digite o nome da musica de {artista}: ")
song = artist.song(musica)


letra = song.lyrics
fraseSplit = letra.split("\n")
contar = len(fraseSplit)

for i in range(contar):
    pyperclip.copy(fraseSplit[i])
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.keyDown('enter')