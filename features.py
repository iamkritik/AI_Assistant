import pywhatkit
import os
import wolframalpha
import pyttsx3
from googletrans import Translator
import speech_recognition as sr
# from googletrans import Translator
from dotenv import load_dotenv
import webbrowser as web
import requests
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

load_dotenv()
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
        
        query=r.recognize_google(audio,language='en')
        
        print(f": Your Query :{query}\n")
    except:   
        return ""
    
    return query.lower()

            

def YouTubeSearch(term):
    term=term.replace("open youtube and",'')
    term=term.replace("play",'')
    term=term.replace("search",'')
    term=term.replace("and",'')
    term=term.replace("one of them",'')
    term=term.replace("that",'')
    result="https://www.youtube.com/results?search_query="+term   
     
    web.open(result)   
    
    Speak("this is what i found for your search")   
    
    pywhatkit.playonyt(term)
    
    Speak("Playing Sir.")   
    
    
  
def SpeedTest():
    os.startfile("C:\\Users\\HP\\My AI assistant\\SpeedTestGui.py")

def Wolfram(query):
    api_key=os.getenv("WOLFRAM")
    
    requester=wolframalpha.Client(api_key)
    
    requested=requester.query(query)
    
    try:
        
        Answer=next(requested.results).text
        
        return Answer
    except:
        
        Speak("AN String Value Is not Answerable.")
                         
        
def temp(query):
    term=str(query)           
    term=term.replace("ruby","")
    term=term.replace("in","")
    term=term.replace("what is the","")
    term=term.replace("what is","")
    term=term.replace("temperature","")
    term=term.replace("temperature kya hai","")
    term=term.replace("me","")
    term=term.replace("tapman kaisa hai","")                   
    
    
    temp_query=str(term)
    
    if 'outside' in temp_query:
        var1="Temperature in Bareilly"
        answer=Wolfram(var1)
        
        Speak(f"{var1} is {answer}.")
        
    else:
        var2="Temperature in"+ temp_query
        
        answ=Wolfram(var2)
        Speak(f"{var2} is {answ}.")
              
        
def Tran():
    Speak("What is the sentance to translate sir?")
    line =TakeCommand('audio')
    translator=Translator()
    result=translator.translate(line)
    text=result.text
    Speak(f"The traslated line is: {text}") 
    

def DateConverter(query):
    
    Date=query.replace("and","-")
    Date=Date.replace(" and","-")   
    Date=Date.replace(" and","-")  
    Date=Date.replace(" and","-")  
    Date=Date.replace(" ","")  
    
    return str(Date)


def my_location():
    
    Speak("checking.....")
    ip_add=requests.get('https://api.ipify.org').text
    
    url='https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
    
    geo_q=requests.get(url)
    
    geo_d=geo_q.json()
    
    city=geo_d['city']
    
    country=geo_d['country']
    
    Speak(f"sir, you are now in {city , country}.")
    

def TodayNews():
     

    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": os.getenv("NEWS")
    }
    main_url = " https://newsapi.org/v1/articles"
 

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    article = open_bbc_page["articles"]
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        print(i + 1, results[i])
 
    
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)                 
 

if __name__ == '__main__':
    
    TodayNews()    
    
 
    
        
        

