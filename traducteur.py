import speech_recognition as sr 
from googletrans import Translator
print("   ___   __________     ___      ___ ")
print("  / _ | / __/_  __/    <  /     / _ \ ")
print(" / __ |/ _/  / /       / / _   / // /")
print("/_/ |_/_/   /_/       /_/ (_)  \___/ ")
print()
print("-AudioFilesTranslator 1.0-")

echantillon_audio = "audio.wav"
r = sr.Recognizer() 
##print(type(r))
with sr.AudioFile(echantillon_audio) as source: 
    audio = r.record(source)
##print(type(audio)) 
print("Currently reading the audio file...")
audiototxt = r.recognize_google(audio,language = "fr-FR")
print()
print("Original Audio:")
print(audiototxt)
traducteur = Translator()
resultat = traducteur.translate(audiototxt, src='fr', dest='en')
print()
print("Translated Audio File:")
print(resultat)
##dialogue rigolo trouvé sur youtube

