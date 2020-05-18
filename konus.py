'''
* Simple python routine for text-to-speech function 
* Based on Google TextToSpeech Library
* Bilishim R&D
'''
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

konus("merhaba yılmaz bey nasılsınız")	

