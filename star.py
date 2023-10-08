import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime


name = "marc"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# engine.say("Hola, soy mark, tu asistente espacial")
engine.runAndWait()

def talk (text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="es-US")
            command = command.lower()
            if name in command:
                command = command.replace(name, '') 
                
    except:
        pass
    return command

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk('La hora es' +hora )
    else:
        talk('No te entiendo')

run()