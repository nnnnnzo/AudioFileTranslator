#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:36:20 2020

@author: enzo
"""

def TranslationEngine(audio_sample, SLAC, SL, DL):
    import speech_recognition as sr 
    from googletrans import Translator
    r = sr.Recognizer() 
    with sr.AudioFile(audio_sample) as source: 
        audio = r.record(source)
    ScratchTXT = r.recognize_google(audio,language = SLAC)
    traducteur = Translator()
    TranslatedTXT = traducteur.translate(ScratchTXT, src=SL, dest=DL)
    return TranslatedTXT
