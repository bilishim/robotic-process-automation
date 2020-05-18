import speech_recognition as sr
from gtts import gTTS
import os
from automagica import *
import codecs
import pyperclip
import random


ifadeler = {}

ifadeler["iyiyim"] =  "ben de iyiyim çok teşekkür ederim"
ifadeler["halsizim"] =  "biraz dinlenin o zaman"
ifadeler["hastayım"] =  "çok geçmiş olsun"
ifadeler["nasılsın"] =  "çılgınlar gibiyim"
ifadeler["ders çalış"] =  "başarılar dilerim"
ifadeler["adın ne"] =  "benim adım ace"
ifadeler["memnun oldum"] =  "ben de çok memnun oldum"

def open_word():

	press_key_combination('win', 'r')
	wait(1)

	press_key('w')
	press_key('i')
	press_key('n')
	press_key('w')
	press_key('o')
	press_key('r')
	press_key('d')
	press_key('enter')

	wait(3)
	press_key('enter')
	
	
def write_to_word():

	press_key_combination('ctrl', 'v')


def command_to_word(command):

	if command == "yeni paragraf":
		press_key('enter')
		press_key('enter')
	elif command == "iptal":
		press_key_combination('ctrl', 'z')
	elif command == "kaydet ve kapat":
		press_key_combination('ctrl', 'w')
		press_key('enter')	
		press_key_combination('ctrl', 'v')
		press_key('enter')
		press_key_combination('alt', 'f4')		
			

def konus(metin):

	try:
		tts = gTTS(text=metin, lang='tr')
		filename = "metin.mp3"
		tts.save(filename)
		os.system("mpg123 -q " + filename +  " >nul 2>&1")
	except:
		pass




		
		
try:
	
	tts = gTTS(text="merhaba Yılmaz Bey, size nasıl yardımcı olabilirim?", lang='tr')
	filename = "metin.mp3"
	tts.save(filename)
	os.system("mpg123 -q " + filename +  " >nul 2>&1")
except:
	pass
		
		
	
while True:
	r = sr.Recognizer()
	with sr.Microphone() as kaynak:
		ses = r.listen(kaynak,timeout = None)
		try:
		
			metin = r.recognize_google(ses,language="tr-TR")
			
			metin = metin.lower()
			
			print(metin)
			
	
			for key in ifadeler:
				if key in metin:
					konus(ifadeler[key])
					break
			
			
			if metin == "word aç" or metin == "döküman aç":
				open_word()
				
				
			elif metin == "yeni paragraf":
				command_to_word("yeni paragraf")
				
			elif metin == "iptal":
				command_to_word("iptal")
				
			elif metin == "kaydet ve kapat":
				sayi = random.randint(1, 100)   
				pyperclip.copy("doküman-" + str(sayi) +".docx")
				command_to_word("kaydet ve kapat")
			
			elif metin == "güle güle":
				break
			
			else:
				try:
					metin = metin.capitalize() + ". " 
					pyperclip.copy(metin)
					write_to_word()
				except:
					pass
			
		except sr.UnknownValueError:
			print("Anlamadım.")
		except sr.RequestError:
			print("Kötü İstek")
			



