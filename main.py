import HearMe as hm
import Speech as sp
import WikiSearch as ws

mic = hm.HearMe()
spk = sp.Speech()

spk.speak("salutation", "Olá, eu sou a Sexta-Feira, sua assistente virtual. Como posso te chamar?")

name = mic.hear()

isNotCorrect = True

while isNotCorrect:
    confirm = f"""Você disse: {name}?"""
    spk.speak("confirm", confirm)
    res = mic.hear()
    res = res.lower()
    if res == "sim":
        isNotCorrect = False
    else:
        name = mic.hear()

spk.speak("whoiam", "Olá " + name + "! Como posso te ajudar?")

phrase = mic.hear()

isNotCorrect = True

while isNotCorrect:
    confirm = f"""Você disse: {phrase}?"""
    spk.speak("confirm", confirm)

    res = mic.hear()
    res = res.lower()
    if res == "sim":
        isNotCorrect = False
    else:
        phrase = mic.hear()

search = ws.WikiSearch(phrase)

search_res = search.getSummary()
print(search_res)

spk.speak("search", search_res)