
import speech_recognition as sr
import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)
def Speak(audio):   
    print("    ")   
    print(f":{audio}")    
    engine.say(audio)
    engine.runAndWait()
    print(" ")
           

def TakeCommand(audio):
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print(": listening...")
        r.pause_threshold = 0.5
        
        audio=r.listen(source)
        
    try:
        
        print(":Recognizing...")    
        
        query=r.recognize_google(audio,language='en-in')
        
        print(f": Your Command:{query}\n")
    except:   
        return "none"
    return query.lower() 


while True:
    wake_up=TakeCommand('audio')
    wake_up=str(wake_up)
    wake_up=wake_up.replace(" ","_")
    if 'wake_up' in wake_up:
        os.startfile('C:\\Users\\HP\\My AI assistant\\main.py')
        Speak("wake up detected,sir")
        
    else:
        print("nothing.....") 