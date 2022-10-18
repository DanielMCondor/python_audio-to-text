
from os import path
import speech_recognition as sr
from pydub import AudioSegment

sound = AudioSegment.from_mp3("audio/audio.mp3")
sound.export("audio/audio.wav", format="wav")

AUDIO_FILE = "audio/audio.wav"

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    print("Text: ", r.recognize_google(audio))