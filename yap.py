'''
* Simple Robotic Process Automation demo
* Based on Automagica Library
* Bilishim R&D
'''

import speech_recognition as sr
from gtts import gTTS
import os
from automagica import *
import codecs
import pyperclip

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
	
	
open_word()