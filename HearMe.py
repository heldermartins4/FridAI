import speech_recognition as sr

class HearMe:
    def __init__(self):
        pass

    def hear(self):
        mic = sr.Recognizer()
        print("Estou ouvindo...")
        with sr.Microphone() as source:
            mic.adjust_for_ambient_noise(source)
            audio = mic.listen(source)

            try:
                phrase = mic.recognize_google(audio, language='pt-BR')
                return phrase
            except sr.UnknownValueError:
                return "Não entendi"
            except sr.RequestError:
                return "Desculpe, houve um erro no sistema..."