'''
* Simple digital assistant doing simple conversation
* Based on Google TTS and SpeechRecognition Libraries
* Bilishim R&D
'''

import speech_recognition as sr
import os
import os
from gtts import gTTS

def konus(metin):

	try:
		tts = gTTS(text=metin, lang='tr')
		filename = "metin.mp3"
		tts.save(filename)
		os.system("mpg123 -q " + filename +  " >nul 2>&1")
	except:
		pass


ifadeler = {}

ifadeler["iyiyim"] =  "ben de iyiyim çok teşekkür ederim"
ifadeler["halsizim"] =  "biraz dinlenin o zaman"
ifadeler["hastayım"] =  "çok geçmiş olsun"
ifadeler["nasılsın"] =  "çılgınlar gibiyim"


konus("merhaba yılmaz bey nasılsınız")	



while True:
	r = sr.Recognizer()
	with sr.Microphone() as kaynak:
		ses = r.listen(kaynak,timeout = None)
		try:
		
			metin = r.recognize_google(ses,language="tr-TR")
			print(metin)
			
			for key in ifadeler:
				if key in metin:
					konus(ifadeler[key])
					break
			
			if metin.lower() == "güle güle":
				break
			
		except sr.UnknownValueError:
			print("Anlamadım.")
		except sr.RequestError:
			print("Kötü İstek")
			



