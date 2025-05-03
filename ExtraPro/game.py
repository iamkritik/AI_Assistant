import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)
def Speak(audio):   
    print("    ")   
    print(f":{audio}")    
    engine.say(audio)
    engine.runAndWait()
    print(" ")
    
def TakeCommand():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print(":listening.....")
        print("\n") 
        r.pause_threshold = 0.5
        
        audio=r.listen(source)
        
    try:
        
        print(":Recognizing...") 
        query=r.recognize_google(audio,language='en-in')
        
        print(f": Your::{query}\n")
    except:   
        return "none"
    return query.lower() 

list = ['stone','paper','scissor']
Speak("okay sir let's play stone paper scissor")
Speak('start')
while True: 
   
    Speak('stone paper scissor')

    s=TakeCommand()
    s=str(s)
    for word in list:
      if word in list:
        reply=random.choice(list)  
    Speak(reply)    
    if reply==s:
        Speak('draw')       
    
    

      

    