from time import sleep
import pyttsx3
import subprocess
import speech_recognition as sr
import datetime
import pyautogui
import os
import pyjokes
import wolframalpha
from keyboard import press_and_release
import keyboard
import webbrowser
import requests
import pywhatkit
from pywikihow import search_wikihow
import wikipedia
from win10toast import ToastNotifier
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
###
#Design and Developed by Dheerendra
###
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)
def Speak(audio):   
    print("    ")   
    print(f":{audio}")    
    engine.say(audio)
    engine.runAndWait()
    print(" ")
  


    
      
ToastNotifier().show_toast("Your A.I. is  now activated")
# os.startfile('C:\\Users\\HP\\My AI assistant\\aiGui.py')
#uncomment above to implement gui interface
Speak("Activated")
Speak("hello sir!")  
Speak("it is very nice to meet you again")


def TakeCommand(audio):
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print(":listening.....")
        print("\n") 
        r.pause_threshold = 0.5
        
        audio=r.listen(source)
        
    try:
        
        print(":Recognizing...") 
        query=r.recognize_google(audio,language='en-in')
        
        print(f": Your Command:{query}\n")
    except:   
        return "none"
    return query.lower() 



def TaskExe():

    
    
    while True:
        query=TakeCommand('audio')
         
        if 'open google and search' in query or 'google search' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            import wikipedia as googleScrap
            query=query.replace("ruby","")
            query=query.replace("search","")
            query=query.replace("and",'')
            query=query.replace("on",'')
            query=query.replace("open",'')
            query=query.replace("open google and search",'')
            query=query.replace("google","")
            Speak('okay sir!')
            Speak("According to google search.")
            
            try:
                pywhatkit.search(query)
                result=googleScrap.summary(query,4)
                Speak(result)
            except:
                print("no speakable data available")
                
        elif 'how many' in query or 'voices' in query:
            for i in range (1,6):
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[i-1].id)
                engine.setProperty('rate',170)
                Speak(f"this is my voice {i}")  
                engine.setProperty('voice', voices[0].id) 
            Speak("if you like to change my voice you can choose one of them")
            print('say->yes/no')
            response1=TakeCommand('audio')
            if response1=='yes':
                Speak('which voice would you like to chose?')
                response2=TakeCommand('audio')
                response2=response2.replace('voice','')
                response2=response2.replace(' ','')
                x=int(response2)
                engine.setProperty('voice', voices[x].id)
                engine.setProperty('rate',170)
                Speak("according to your prefrence now this is my voice")
            else:
                Speak("ok, sir")
                continue    
                            
        elif 'current time' in query or 'what is the time' in query or 'kitna time hua hai' in query or 'what is time now' in query or 'kitna time hua hai' in query or 'time' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            strTime = datetime.datetime.now().strftime("%H:%S %p")
            print(f"\n\tit is {strTime}")
            Speak(f"Sir the time is: {strTime}")
            
        elif 'directory' in query or 'make folder' in query or 'make a folder' in query or 'create a folder' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Sir, Tell me the directory name")
            directory_name=TakeCommand('audio')
            Speak("Ok sir, I am Creating.")
                        
            def create_directory(directory_name):
                try:

                    subprocess.run(f'mkdir {directory_name}', shell=True, check=True)
                    Speak(f"Directory '{directory_name}' created successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error creating directory '{directory_name}':")
                    print(e.stderr)
            create_directory(directory_name)
        
                
        elif 'delete directory' in query or 'delete folder' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Sir, Tell me the directory name")
            directory_name=TakeCommand('audio')
            Speak("Ok sir, I am deleting.")
            def delete_directory(directory_name):
                try:
                    subprocess.run(f'rmdir /s /q {directory_name}', shell=True, check=True)
                    Speak(f"Directory '{directory_name}' deleted successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error deleting directory '{directory_name}':")
                    print(e.stderr)
            delete_directory(directory_name)
        
        
        elif 'create a txt file' in query or 'text file' in query or 'make txt file' in query or 'txt file' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Sir, Tell me the text file name")
            file_name=TakeCommand('audio')
            Speak("Ok sir, I am deleting.")
            def create_textfile(file_name):
                try:
                    subprocess.run(f'echo >{file_name}', shell=True, check=True)
                    Speak(f"file {file_name} created successfully")
                except subprocess.CalledProcessError as e:
                    print(f"Error deleting directory '{file_name}':")
                    print(e.stderr)
            create_textfile(file_name)
            
        elif 'delete file' in query or 'delete txt file' in query or 'delete text file' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Sir, Tell me the directory name")
            directory_name=TakeCommand('audio')
            Speak("Ok sir, I am deleting.")
            def delete_directory(directory_name):
                try:
                    subprocess.run(f'rmdir /s /q {directory_name}', shell=True, check=True)
                    Speak(f"Directory '{directory_name}' deleted successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error deleting directory '{directory_name}':")
                    print(e.stderr)
            delete_directory(directory_name)
            
        elif 'create a file' in query or 'create a file of' in query or 'make a file' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Sir, Tell me the file name")
            file_name=TakeCommand('audio')
            file_name=file_name.replace('and write in it','')
            Speak("Ok sir, I am creating.")
            
            def create_typefile(file_name):
                
                try:
                    subprocess.run(f'echo >{file_name}', shell=True, check=True)
                    Speak(f"file {file_name} created successfully")
                except subprocess.CalledProcessError as e:
                    print(f"Error deleting directory '{file_name}':")
                    print(e.stderr)
            create_typefile(file_name)    
            
        elif 'delete file' in query or 'delete the recent file' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak('okay sir i am deleting the recent file')
            deletefile=TakeCommand('audio')
            Speak('okay sir i am deleting')
            
            
            def Delete_file(deletefile):
                try:
                    subprocess.run(f'rmdir /s /q {deletefile} ',shell=True, check=True)
                    Speak(f'file {deletefile} deleted successfully')
                except subprocess.CalledProcessError as e:
                    Speak(f'there is an error in deleting a file')
                    print(e.stderr)
                    
            Delete_file(deletefile)
                 
                             
                      
            
        elif 'open youtube and search' in query or 'open youtube' in query or 'youtube search' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Searching ,sir")
            from features import YouTubeSearch
            
            YouTubeSearch(query) 
            
        elif 'scrap' in query or 'get image from internet' in query or 'get images' in query:
            from G_Imagescrap import main
            main() 
            
        elif 'translater' in query or 'tranlater kholo' in query or 'translate' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("why not, sir")
            from features import Tran
            Tran() 
            
        elif 'calendar of' in query or 'generate calander' in query:
            query=query.replace('calendar of','')
            query=query.replace('give','')
            query=query.replace('can you','')
            query=query.replace('for me','')
            query=query.replace('me','')
            query=query.replace('the','')
            query=query.replace('print','')
            query=query.replace(' ','')
            year=int(query)
            import calendar  
            Speak("yes sir")
            Speak(f"The calendar of year {year} is :- ")
            print("******************************************************************************")   
            print (calendar.calendar(year))
            print("******************************************************************************") 
            sleep(2)
            Speak("sir do you want any specific month calender of any year?")
            print("say->(yes/no)")
            response=TakeCommand('audio')
            if response=='yes':                                      
              Speak("give me the year")
              input1=TakeCommand('audio')
              yy=int(input1)
              Speak("give me the month")
              input2=TakeCommand('audio')
              mm=int(input2)
              Speak("the calander of that year and month is:-")
              print("**************************")
              print(calendar.month(yy, mm))
              print("**************************")
            elif response=='no':
                Speak("okay sir!")
                continue   
            
        elif 'aaj kaun sa din hai' in query: 
            from datetime import date
            import calendar
            current_date = date.today()
            din=calendar.day_name[current_date.weekday()]
            Speak(din)
            
        elif 'detect the color' in query or 'can you detect color' in query or 'which color' in query:
            from ExtraPro.colorDetect import ColorDetect
        
        elif 'generate code' in query or 'write code' in query or 'code in python' in query:
            import openai
            openai.api_key = os.getenv('OPEN_AI_API_KEY')
            messages = [ {"role": "system", "content":  
                        "You are a intelligent assistant."} ] 
            message = query
            Speak("okay sir")
            Speak("i am writing sir wait a few seconds")   
            if message: 
                messages.append( 
                    {"role": "user", "content": message}, 
                ) 
                chat = openai.chat.completions.create( 
                    model="gpt-3.5-turbo", messages=messages 
                ) 
            reply = chat.choices[0].message.content 
            print(f"ChatGPT: {reply}") 
            messages.append({"role": "assistant", "content": reply}) 
          
            
        elif 'fact' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            query=query.replace('tell me fact about','')
            query=query.replace(' ','')
            query=query.replace('fact about','')
            url =f"https://numbersapi.p.rapidapi.com/{query}/math"
            querystring = {"fragment":"true","json":"true"}
            headers = {
	        "X-RapidAPI-Key": os.loadenv("RAPID_API_KEY"),
	        "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            data=response.json()
            Speak(data['text'])     
            
        elif 'mera name kya hai' in query or 'mera naam kya hai' in query or 'mera nam batao' in query or 'can you tell my name' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("ofcourse,sir")
            Speak("your name is Dheerendra Dixit ,Sir.")
            
        elif 'tumhara naam kya hai' in query or 'what ise your name?' in query or 'apna naam batao' in query:   
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("My name is ruby ,Sir.")      
        
        elif 'youtube auto' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            sleep(3)
            from automations import YouTubeAuto
            query=query.replace('youtube','')
            query=query.replace('youtube auto','')
            YouTubeAuto(query) 
           
            
        elif 'chrome auto' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            print("opening....")
            Speak("opening chrome")
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
            sleep(3)
            from automations import ChromeAuto
            query = query.replace('chrome', '')
            query = query.replace('chrome auto', '')
            ChromeAuto(query) 
            
        elif 'open brave' in query or 'brave kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening brave")
            os.startfile('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe') 
            
        elif 'close chrome' in query or 'chrome band karo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("closing chrome")
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'can you detect text for me' in query:
            from ExtraPro.Text_Detection import main     
            
        elif 'close brave' in query or 'brave band karo' in query: 
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay,sir") 
            os.system("TASKKILL /F /im brave.exe")   
            
        elif 'open file explorer' in query or 'file explorer kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay ,sir")
            press_and_release('windows + E')
            
        elif 'open settings' in query or 'settings kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            press_and_release('windows + I')
            Speak("okay ,sir")
        elif 'lock window' in query or 'window lock kardo' in query: 
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close() 
            press_and_release('windows + L')      
            Speak("okay ,sir") 
            
        elif 'open my sql' in query or 'my sql kholo' in query or 'my sql' in query :
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay ,sir") 
            os.stratfile("C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe") 
            
        elif 'take screenshot' in query or 'screenshot lo' in query or 'screenshot' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            press_and_release("windows + PrtScn")    
            os.startfile('C:\\Users\HP\\Pictures\\Screenshots')
            sleep(3)
            os.close('C:\\Users\HP\\Pictures\\Screenshots')
        elif 'open microsoft excel' in query or 'microsoft excel kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening....")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')   
            
        elif 'microsoft word kholo' in query or 'open microsoft word' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening....")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007') 
            
        elif 'open this pc' in query or 'this pc kholo' in query or 'this pc' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak('okay,sir')
            press_and_release('windows+E')
            sleep(1)
            pyautogui.click(x=202, y=434)
            
        elif 'open amazon' in query or 'amazon open' in query or 'amazon' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening amazon.com...")
            webbrowser.open('http://www.amazon.com')
            
        elif 'open flipkart' in query or 'flipkart open' in query or 'flipkart' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening amazon.com...")
            webbrowser.open('http://www.flipkart.com')          
            
        elif 'open pycharm' in query or 'py charm kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            os.startfile('D:\\PyCharm\\PyCharm 2023.2.3\\bin\\pycharm64.exe')
            
        elif 'open command prompt' in query or 'command prompt kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            os.startfile('C:\\Windows\\system32\\cmd.exe')     
            
        elif 'open apache' in query or 'apache' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            os.startfile('C:\\Program Files\\NetBeans-18\\netbeans\\bin\\netbeans64.exe')  
            
        elif 'open mangodb' in query or 'mangodb' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            os.startfile('C:\\Users\\HP\\AppData\\Local\\MongoDBCompass\\MongoDBCompass.exe')       
                
            
        elif 'open power point' in query or 'power point kholo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("opening....")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007')    
        
             
        elif 'speed test' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            print("opening ,sir")
            Speak("opening speed test")
            from features import SpeedTest
            SpeedTest()
          
        elif 'temperature' in query or 'temperature kya hai' in query or 'tapman kaisa hai' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from features import temp
            temp(query)
            
        elif 'weather in' in query or "today's weather in" in query or "what is today's weather in" in query or 'aaj ka weather kaisa hai' in query or 'aaj mausam kaisa hai' in query or 'kaisa mausam hai' in query or 'show weather' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            query=query.replace('weather in','')
            query=query.replace('in','')
            query=query.replace('show weather','')
            query=query.replace('data','')
            query=query.replace("what is today's weather in",'')
            query=query.replace("today's weather in",'')
            query=query.replace("me",'')
            query=query.replace("mein",'')
            query=query.replace("aaj ka weather kaisa hai",'')
            query=query.replace("aaj mausam kaisa hai",'')
            url='https://wttr.in/{}'.format(query)
            Speak(f"you can see the data for the weather in {query}")
            res=requests.get(url)
            print(res.text)   
          
                
        
        elif "calculate" in query: 
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()  
            app_id = "6X5GUL-WUH3JHJAR9"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            Speak("The answer is " + answer)  
             
        elif 'my current location' in query or 'meri location kya hai' in query or 'meri current location kya hai' in query or 'loaction' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from features import my_location
            my_location()   
            
        elif "what is" in query or 'kya hota hai' in query or 'who is' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            query=query.replace("kya hota hai",'')
            query=query.replace("kaun hai",'')
            client = wolframalpha.Client("6X5GUL-WUH3JHJAR9")
            res = client.query(query)
             
            try:
                Speak (next(res.results).text)
            except StopIteration:

                from chatbot.chatbot import Chatterbot
                reply=Chatterbot(query)
                Speak(reply)   
              
    
                
          
        elif 'space news' in query or 'Space news' in query or 'NASA news' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            
            Speak("write the date for news extracting process.")
            
            value=(input('date:-'))
            
            from nasa import NasaNews
            NasaNews(value)
            
        elif 'mars images' in query or 'mars image' in query or 'Mars' in query or 'mars' in query or 'Mars images' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            
            from nasa import MarsImage
            
            MarsImage()
            
        elif 'near earth' in query or 'near earth objects' in query or 'passed through earth' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            
            from nasa import Astro
            
            Speak("tell me the starting date")
            start=input("enter the starting date::")
            Speak("tell me the ending date")
            end=input("enter the ending date::")
            
            Astro(start, end)
        
        elif 'solar system' in query or 'solar bodies in solar system' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            url="https://api.le-systeme-solaire.net/rest/bodies/"
            r=requests.get(url)
            Data=r.json()
            bodies=Data['bodies']
            Number=len(bodies)
            Speak(f"Number of bodies in solar System :{Number}")
            from nasa import SolarBodies
            Speak("tell me the name of body in solar system , you want to know about.")
            bod=TakeCommand('audio')
            body=bod.replace(" ", "")
            body=body.replace(" ", "")
            Body=str(body)
            SolarBodies(body=Body)
            
        elif 'meaning of' in query or 'ka kya matlab hai' in query or 'can you tell me meaning of' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            query=query.replace('meaning of','')
            query=query.replace('can you tell me meaning of','')
            query=query.replace('ka kya matlab hai','')
            query=query.replace(' ','')
            try:
                url=(f'https://api.dictionaryapi.dev/api/v2/entries/en/{query}')
                result=requests.get(url)
                res=result.json()
                meanings=res[0]['meanings'][0]['definitions'][0]['definition']
                Speak(f"meaning of {query}:{meanings}")
                
            except Exception:
                query=query.replace('meaning of','')
                query=query.replace('can you tell me meaning of','')
                query=query.replace('ka kya matlab hai','')
                query=query.replace(' ','')
                wiki=wikipedia.summary(query,2)  
                Speak(f"meaning of:{wiki}")
        
        elif 'tell me story' in query or 'kahani' in query or 'mujhe koi kahani sunao' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from Database import story
        
                
        elif 'can you detect objects' in query:  
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("can you give me the path of the image")
            path=input("path of the image")
            
            upadtePath=path.replace('/','\\')
            from ultralytics import YOLO

            model=YOLO('yolov8n.pt')
            def detect_objects(image):
                results=model(image)[0]
                detections=[]
                
                for result in results.boxes.data.tolist():
                    x1,y1,x2,y2,score,class_id=result
                    detections.append([int(x1),int(y1),int(x2),int(y2),round(score,3),results.names[int(class_id)]])
                    
                return detections



            for detection in detect_objects(f'{upadtePath}'):
                print (detection)   

          
        elif 'where is' in query or 'kaha hai' in query or 'located' in query or 'distance' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            place=query.replace("where is", "")
            place=place.replace("located", "")
            place=place.replace("from me", "")
            place=place.replace("of", "")
            place=place.replace("me", "")
            place=place.replace("my", "")
            place=place.replace("location", "")
            place=place.replace("alex", "")
            place=place.replace("ruby","")
            from automations import google_maps
            google_maps(place)
           
        elif 'write a note' in query or 'note likho' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from automations import Notepad    
            Notepad()  
        
        elif 'close notepad' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            print("closing..")
            Speak("closing notepad")
            from automations import CloseNotepad
            
            CloseNotepad()
            
        elif 'change your voice' in query or 'apni awaj badlo' in query or 'awaj change karo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay sir, i am changing my voice")
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            Speak("now that is my voice, sir ") 
            
        elif 'back to your voice' in query or 'back to your original voice' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay sir, i am changing to my original voice")
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            Speak("now that is my orginal voice ")             
            
        elif 'how to' in query or 'kaise' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("getting data from internet.")
            op=query.replace("ruby","")
            max_result= 1
            how_to_func=search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
            
        elif 'website' in query :
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Ok sir,Launching...") 
            query=query.replace("ruby","")
            query=query.replace("website", "")
            query=query.replace(" ","")
            web1=query.replace("open","")
            web2='https://www.'+web1+'.com'  
            webbrowser.open(web2)
            Speak("Launched!")
            
            
        elif 'wikipedia' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("searching Wikipedia....")
            query=query.replace("ruby","")
            query=query.replace("wikipidea", "")  
            wiki=wikipedia.summary(query,2)  
            Speak(f"According to Wikipedia:{wiki}")
            
    
            
        elif 'set alarm' in query or 'set the alarm' in query or 'alarm set karo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("Enter the time ,sir")
            time=input("Enter the time:")
            Speak(f"setting the alarm to:{time}")
            Speak("Aalarm has been set")
            
            while True:
                time_ac=datetime.datetime.now()
                now=time_ac.strftime("%H:%M")
                
                if now==time:
                    os.startfile('C:\\Users\\HP\\My AI assistant\\Database\\Sound\\1.mp3')
                    Speak("time to wake up sir")
                elif now>time:
                    Speak("Alarm Closed")
                    break
                  
            
        elif 'remember that' in query or 'yad rakho' in query or 'yad rakhna' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            remsg=query.replace("remember that","")
            remsg=query.replace("yad rakho","")
            remsg=query.replace("yad rakhna","")
            remsg=remsg.replace("ruby","")
            Speak("sir, you told me to remember this:"+remsg)
            Speak("i am storing that in my data")
            remember=open('C:\\Users\\HP\\My AI assistant\\Database\\remem.txt', 'w')
            remember.write(remsg)
            remember.close()
            
        elif 'what did i told you to remember' in query or 'kya yad rakhne ko bola tha' in query or 'tumhe kya yad hai' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            remember=open('C:\\Users\\HP\\My AI assistant\\Database\\remem.txt','r' )
            remsg=remember.read()
            Speak("Accoding to saved data")
            Speak(f"you tell me that:- {remsg} ")
           
        elif 'jokes' in query or 'tell me some jokes' in query or 'joke sunao' in query or 'koi joke sunao' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            get=pyjokes.get_joke()
            Speak(get)
            
        elif 'repeat my words' in query or 'mere words dohrao' in query or  'mere sabd dohrao' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            jj=TakeCommand('audio')  
            Speak(f" sir , you said:{jj}") 
            
        elif "will you be my gf" in query or "will you be my bf" in query:   
            Speak("I'm not sure about, may be you should give me some time")     
             
        elif 'you need a break' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("ok sir, you can call me anytime ")
            break  
        
        
        
        elif 'today news' in query or "what is today's news" in query or 'aaj ki news kya hai' in query or "today's news" in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            from features import TodayNews  
            TodayNews()  
  
            
        elif 'song please' in query or 'play some songs' in query or 'can you play some songs?' in query or 'play song' in query or 'koi gana chalao' in query or 'koi gana play karo' in query or 'koi song play karo' in query or 'bajao' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("okay sir,what song should i play...")
            song =TakeCommand('audio')
            webbrowser.open(f'https://open.spotify.com/search/{song}')  
            sleep(20) 
            pyautogui.click(x=1214, y=386)
            sleep(7)
            pyautogui.click(x=533, y=712)
            Speak("Playing:-"+song) 
        
        elif 'stop song' in query or 'stop music' in query or 'gana band karo' in query or 'song band karo' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            song =TakeCommand('audio')
            pyautogui.click(x=533, y=712)
            Speak("stopped:") 
            
        elif 'add item' in query or 'add items' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak("give me the items name to add in youur shopping list")
            for i in range(1,10):
               items=TakeCommand('audio')
               if 'stop' in items or 'no items' in items or 'bas' in items:
                   items.replace('stop','')
                   Speak('ok')
                   break
               
               filelog=open('C:\\Users\\HP\\My AI assistant\\ExtraPro\\shop.txt','a')
               filelog.write(items+' , ')
               filelog.close()
               Speak('done')
               Speak('next')      
           
           
        elif 'open shopping list' in query or 'open my shopping list' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak('you can see your shopping list hare and can add items manually')
            from ExtraPro import shop 
            
        elif 'items in my shopping list' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            with open('C:\\Users\\HP\\My AI assistant\\ExtraPro\\shop.txt') as f:
                content=f.readlines()
                
            Speak(content)   
            
        elif 'write task' in query or 'create my to do' in query or 'write tasks' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak('tell me the task sir.')
            for i in range(1,15):
               items=TakeCommand('audio')
               if 'stop' in items or 'no task' in items or 'bas' in items:
                   items.replace('stop','')
                   Speak('ok')
                   break
               
               filelog=open('C:\\Users\\HP\\My AI assistant\\ExtraPro\\todo.txt','a')
               filelog.write(items+' , ')
               filelog.close()
               Speak('done')
               Speak('next')
               
        elif 'task in my to do list' in query or 'tasks in my to do list' in query or 'my to do list' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            with open('C:\\Users\\HP\\My AI assistant\\ExtraPro\\todo.txt') as f:
                content=f.readlines()
            Speak(content) 
         
        elif 'game' in query or "let's play" in query: 
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            Speak('initialy i have four games,sir 1-number guessing game ,2-stone,paper,scissor ,3-flames','4-jumbeld word guessing game')
            Speak('which one would you like to play')
            response=TakeCommand('audio')
            if 'number guessing' in response or 'number' in response or 'guess' in response:
                from ExtraPro import game2    
            elif 'stone,paper,scissor' in response or 'stone' in response or 'paper' in response:
                from ExtraPro import game
            elif 'flames' in response: 
                from ExtraPro import game3 
                
            elif 'jumbeld word guessing game' in response or 'jumbeld word game' in response:
                from ExtraPro import game4  
                
                
        elif 'play' in query:
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            song =TakeCommand('audio')
            song=song.replace('play','')
            pyautogui.click(x=97, y=253)
            keyboard.write(song)
            sleep(5)
            pyautogui.click(x=1214, y=385)
            sleep(5)
            pyautogui.click(x=533, y=712)
            Speak("Playing:-"+song) 
                 
            
        elif 'generate qr' in query or 'qr generate karo' in query or 'create qr' in query or 'qr' in query:
            query=query.replace("for",'')
            query=query.replace("for this",'')
            query=query.replace("generate qr",'')   
            query=query.replace("qr generate karo",'') 
            Speak("okay sir")
            Speak("Enter anything for which you want to create qr code, sir")
            s=input("Enter the text::") 
            from ExtraPro.qr import qr
            qr(s) 
            Speak('qr generated sir')
            Speak("you can check this")
            img=Image.open("C:\\Users\\HP\\My AI assistant\\Database\\qr_images\\qr.png")
            img.show()
                                
       
        elif 'aaj kitni tarikh hai' in query or 'aaj tarikh kitni hai' in query or 'what date is today' in query or 'what date ise today' in query or 'tell the date' in query or "today's date" in query: 
            filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
            filelog.write(query+"\n")
            filelog.close()
            strDate=datetime.datetime.now().strftime("%d/ %m /%y")
            print(f"\n\tToday is:- {strDate}") 
            Speak(f"Today is:-{strDate}")
            
        elif 'can you download images for me' in query or 'download images' in query:
            import G_Imagescrap
            
        elif "change name" in query or 'channge your name' in query:
            Speak("What would you like to call me, Sir.")
            assname = TakeCommand('audio')
            Speak("Thanks for naming me")
            
        elif 'show note' in query: 
            from automations import showNote
            showNote()                       
        else:
            
            from chatbot.chatbot import Chatterbot
            if query=='none':
                continue
            reply=Chatterbot(query)
            Speak(reply)
                
            if 'bye' in query:
                break
            
            elif 'exit' in query: 
                Speak("okay sir, it was nice to meet you")
                break
            elif 'stop' in query:
                Speak("okay sir")
                break
                
TaskExe()    
     
            
         