from playsound import playsound 
import speech_recognition as sr  
from googletrans import Translator  
from gtts import gTTS  
import os


from google.cloud import translate_v2 as translate

# Initialize the Google Cloud Translation client
client = translate.Client()

# Input text
speech_text = "hello"

try:
    # Translate the text
    result = client.translate(speech_text, target_language="fr")
    print("Translated:", result["translatedText"])
except Exception as e:
    print("Translation Error:", e)
