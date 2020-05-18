'''
* Simple python routine for speech-to-text function 
* Based on Google SpeechRecognition Library
* Bilishim R&D
'''

import speech_recognition as sr
import os


while True:
	r = sr.Recognizer()
	with sr.Microphone() as kaynak:
		ses = r.listen(kaynak,timeout = None)
		try:
		
			metin = r.recognize_google(ses,language="tr-TR")
			print(metin)
			
			if metin.lower() == "programı kapat":
				break
			
		except sr.UnknownValueError:
			print("Anlamadım.")
		except sr.RequestError:
			print("Kötü İstek")
			



