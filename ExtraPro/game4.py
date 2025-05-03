import pyttsx3
import speech_recognition as sr
import random

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


list=['structure','python','random','hello','world','haramjada','madarchood','bhosdike','gandu','laundiyabaj']
count=1

Speak("sir ,let's play word guesing game")
while True:
    word=random.choice(list)
    splitWord = []
    for letter in word:
        splitWord.append(letter)
    rr= ''.join(random.sample(word, len(word)))
    Speak("here is the word")
    print(rr)

    inp=input("enter here:")

    if inp in list:
        Speak("you got right answer")
        count=count+1
        print(f"your score is:{count}")
        
        
    else:
        Speak("no match , try again") 
        inp=input("enter here:")  
    