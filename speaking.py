import pyttsx3

def speak(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[0].id) #8 #9 ingles, #0 español
	engine.say(text)
	engine.runAndWait()