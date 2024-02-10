# Voice:
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0
# Name: Microsoft Maria Desktop - Portuguese(Brazil)
# Age: None
# Gender: None
# Languages Known: []
# Voice:
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
# Name: Microsoft Zira Desktop - English (United States)
# Age: None
# Gender: None
# Languages Known: []
# Voice:
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
# Name: Microsoft David Desktop - English (United States)
# Age: None
# Gender: None
# Languages Known: []

# import pyttsx3

# class TextToSpeech:
#     def __init__(self):
#         self.speech = pyttsx3.init() 
#         self.speech.setProperty('rate', 150)
#         self.speech.setProperty('volume', 1)
    
#     def speak(self, text):
#         self.speech.say(text)
#         self.speech.runAndWait()

from gtts import gTTS
from playsound import playsound
import os
import time

class Speech:
    def __init__(self):
        self.lang = "pt-BR"
        self.slow = False

    def speak(self, audio_file_name, text):
        text_to_speech = text
        myobj = gTTS(text=text_to_speech, lang=self.lang, slow=self.slow)
        audio = f"{audio_file_name}.mp3"
        myobj.save(audio)
        time.sleep(1)

        try:
            print("Tocando áudio...")
            playsound(audio)
        except Exception as e:
            print(f"Erro ao tocar áudio: {e}")
        finally:
            print("Apagando arquivos temporários...")
            os.remove(audio)