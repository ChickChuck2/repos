import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=5)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        print("Você disse: " + frase)
    except sr.UnknownValueError:
        print("Não entendi")
        
    return frase

def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    tts.save('hello.mp3')

    playsound('hello.mp3')

frase = ouvir_microfone()
cria_audio(frase)