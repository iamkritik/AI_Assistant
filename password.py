import pyttsx3
import speech_recognition as sr
import os

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
        
        print(f": Your Command :{query}\n")
    except:   
        return ""
    return query.lower() 

def Pass(pass_inp):
    password="sample password"
    
    passs=str(password)
    
    if passs==str(pass_inp):
        
        Speak("Access Granted.")  
 
    else:
        Speak(" Password is Wrong , Access not granted.")



    
Speak("This Particular File is Password Protected.")
Speak("Kindly Provide The Password To Access.")
Speak("tell me the password")
    
password_inp=TakeCommand('audio')
Pass(password_inp)
    
    