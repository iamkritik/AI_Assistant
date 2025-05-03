import random
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[4] .id)
engine.setProperty('ratte',180)
def speak(audio):
    print("   ")
    print(f":{audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")                         


speak("okay sir.")
speak("let's play number guessing game.")
speak('in this game sir, i will generate a random number between 1 and 50 you have to guess it and enter the number. ')
n=random.randint(1,50)
guess=int(input("enter here:-"))
count=0
while guess!=n:
    count=count+1
    if guess<n:
        speak("the number is higher")
        speak('try again sir')
        guess=int(input("enter here:-"))
    elif guess>n:
        speak("the number is lower")
        speak('try again sir')
        guess=int(input("enter here:-"))
    else:
        break
speak(f"sir,you guessed the right number in:-[{count} chance.]")    
    