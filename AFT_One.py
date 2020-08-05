import speech_recognition as sr 
from googletrans import Translator
print("   ___   __________     ___      ___ ")
print("  / _ | / __/_  __/    <  /     / _ \ ")
print(" / __ |/ _/  / /       / / _   / // /")
print("/_/ |_/_/   /_/       /_/ (_)  \___/ ")
print()
print("-AudioFilesTranslator 1.0-")

audio_sample = "audio.wav"
r = sr.Recognizer() 
##print(type(r))
with sr.AudioFile(audio_sample) as source: 
    audio = r.record(source)
##print(type(audio)) 
print("Currently reading the audio file...")
ScratchTXT = r.recognize_google(audio,language = "fr-FR") ##Language from the source can be edited here
print()
print("Original Audio File:")
print(ScratchTXT)
traducteur = Translator()
TranslatedTXT = traducteur.translate(ScratchTXT, src='fr', dest='en') ##"src" is the source language, and "dest" the destination one; here we want to translate from French to English.
print()
print("Translated Audio File:")
print(TranslatedTXT)
##dialogue rigolo trouvé sur youtube
