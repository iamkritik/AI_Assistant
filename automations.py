from os import startfile
import os
from click import command
from pyautogui import click
from keyboard import press, press_and_release
from keyboard import write
from keyboard import press_and_release
from time import sleep
import pyttsx3
import speech_recognition as sr
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
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
        r.pause_threshold = 1
        
        audio=r.listen(source)
        
    try:
        
        print(":Recognizing...")    
        
        query=r.recognize_google(audio,language='en-in')
        
        print(f": Your Command :{query}\n")
    except:   
        return ""
    return query.lower() 

def TakeCommandHindi(audio):
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print(": listening...")
        r.pause_threshold = 1
        
        audio=r.listen(source)
        
    try:
        
        print(":Recognizing...")    
        
        query=r.recognize_google(audio,language='hi')
        
        print(f": Your Command :{query}\n")
    except:   
        return ""
    
    return query.lower()

def ChromeAuto(command):
    query =command

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close tab' in query:

        press_and_release('ctrl + w')
        
    elif 'close current window' in query:
        press_and_release('ctrl + shift + w') 
        
    elif 'open home page' in query:
        press_and_release('alt + home')
        
    elif 'minimize window' in query or 'minimize' in query:
        press_and_release('alt+space+n')           
    
    elif 'maximize window' in query or 'maximize' in query:
        press_and_release('alt+space+x')
        
    elif 'search' in query:
        press_and_release('ctrl + f')
        query = query.replace('search','')
        write(query)  
        
    elif 'open developer tools' in query:
        press_and_release('ctrl + shift + j')      
    
    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:
        press_and_release('ctrl + h')
         
    elif 'bookmark' in query:
        press_and_release('ctrl + d')
        
    elif 'download' in query:
        press_and_release('ctrl + j')
    
    elif 'incognito' in query:
        press_and_release('ctrl + Shift + n') 
        
    elif 'reload' in query:
        press_and_release('ctrl + r')
    
    elif 'source code' in query:
        press_and_release('ctrl + u')        
        
    elif 'switch tab' in query:
        Speak("To which tab ?")
        
        tab=TakeCommand()
        Tab=int(tab)    
        
        if '1' in Tab:
            press_and_release('ctrl + 1')  
        elif '2' in Tab:
            press_and_release('ctrl + 2')    
        elif '3' in Tab:
            press_and_release('ctrl + 3')  
        elif '4' in Tab:
            press_and_release('ctrl + 4')              
        elif '5' in Tab:
            press_and_release('ctrl + 5')        
        elif '6' in Tab:
            press_and_release('ctrl + 6')           
        elif '7' in Tab:
            press_and_release('ctrl + 7')
        elif '8' in Tab:
            press_and_release('ctrl + 8')             
    elif 'open' in query:
        name=query.replace("open", "")
        nameA=str(name)
        
        if 'youtube' in nameA:
            web.open('https://youtube.com/')
        
        elif 'instagram' in nameA:
            web.open('https://www.instagram.com/')
            
        elif 'facebook' in nameA:
            web.open('https://www.facebook.com/')
        
        elif  'twitter' in nameA:
            web.open('https://www.twitter.com/')
            
        elif 'whatsapp website' in nameA:
            web.open('https://www.whatsappweb.com/')
        elif 'geeks for geeks' in nameA:
            web.open('https://www.geeksforgeeks.org/')
            
        else:
            string="https://" + nameA + ".com"
            
            string_2 = string.replace("  ", "")
            
            web.open(string)                  

def YouTubeAuto(command):
    query=command
    
    if 'pause' in query or 'video roko' in query or 'stop video' in query or 'video stop' in query:

        press_and_release('space bar')

    elif 'resume' in query:

        press_and_release('space bar')

    elif 'full screen' in query or 'ful screen' in query:

        press_and_release('f')

    elif 'film screen' in query:

        press_and_release('t')

    elif 'skip' in query:

        press_and_release('l')

    elif 'back' in query:

        press('j')

    elif 'increase' in query:

        press_and_release('SHIFT + .')

    elif 'decrease' in query:

        press_and_release('SHIFT + ,')

    elif 'previous' in query:

        press_and_release('SHIFT + p')

    elif 'next' in query:

        press_and_release('SHIFT + n')
        
    elif 'open captions' in query or 'subtitles' in query:
        press_and_release('c')
        
    elif 'speedup' in query or 'increse speed' in query:
        press_and_release('>') 
        
    elif 'search' in query:
        press_and_release('/')
        query=query.replace('search', '')
        query=query.replace(' ', '')
        write(query)  
        
    elif 'forward' in query or 'move' in query:
        press_and_release('I')
        
    elif 'backward' in query:
        press_and_release('j')                 
    
    elif 'search' in query:

        click(x=667, y=146)

        Speak("What To Search Sir ?")

        search = TakeCommand()

        write(search)

        sleep(0.8)

        press('enter')

    elif 'mute' in query:

        press_and_release('m')

    elif 'unmute' in query:

        press_and_release('m')

    else:
        Speak("No Command Found!")
        
def google_maps(place):
    url_place="https://www.google.com/maps/place/" +str(place )
    
    geolocator=Nominatim(user_agent="http")
    location=geolocator.geocode(place, addressdetails=True)
    target_lat_long=location.latitude,location.longitude
    
    web.open  (url=url_place) 
    
    location=location.raw['address']
    
    target={'city':location.get('city','') ,'state':location.get('state','') ,'country':location.get('country','')}
    
    current_location=geocoder.ip('me')
    
    current_lat_long=current_location.latlng
    
    distance=str(great_circle(current_lat_long,target_lat_long,current_lat_long))
    distance=str(distance.split(' ',1)[0])
    distance=round(float(distance),2)
    
    Speak(target)
    Speak(f"sir ,{place} is {distance} kilometer away from your location.")
    
def Notepad():
    Speak("what should i write ,sir.")
    Speak("I am ready to write")
    
    writes=TakeCommand("hello")
    
    time=datetime.datetime.now().strftime("%H:%M:")
    filename=str(time).replace(":","-")+"note.txt"
    
    with open(filename, "w") as file:
        file.write(writes)
        
    path_1="C:\\Users\\HP\\My AI assistant\\"+str(filename)
    path_2="C:\\Users\\HP\\My AI assistant\\Database\\notepad\\" +str(filename)
    
    os.rename(path_1, path_2) 
    os.startfile(path_2)
    
def showNote():
    Speak("Showing Notes")
    file = open("C:\\Users\\HP\\My AI assistant\\Database\\notepad\\*", "r")
    print(file.read())
    Speak(file.read(6))    
    
def CloseNotepad():
      os.system("TASKKILL /im Notepad.exe")    


    
    
    


    
    