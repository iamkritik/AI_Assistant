import requests
import os
from datetime import datetime
from PIL import Image
import pyttsx3
from dotenv import load_dotenv
import os

load_dotenv()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(audio):   
    print("    ")   
    print(f":{audio}")    
    engine.say(audio)
    engine.runAndWait()
    print(" ")

api_key = os.getenv("NASA_API_KEY")

def NasaNews(Date):
    Speak("Extracting Data From Nasa .")
    
    Url="https://api.nasa.gov/planetary/apod?api_key="+str(api_key)
    
    Parameter={'date':str( Date)}
    r=requests.get(Url , params=Parameter)
    
    Data=r.json()
    
    Info=Data['explanation']
    
    Title=Data['title']
    Image_Url=Data['url']
    Image_r=requests.get(Image_Url)
    
    filename=str(Date) +'.jpg'
    
    with open(filename,'wb') as f:
        f.write(Image_r.content)
        
    path_1="C:\\Users\\HP\\My AI assistant\\" +str(filename)
    path_2="C:\\Users\\HP\\My AI assistant\\Nasa Database\\Images\\" +str(filename)
    
    os.rename(path_1, path_2)
    
    img=Image.open(path_2)
    
    img.show()
    
    
    Speak(f"Title :{Title}")
    
    Speak(f"According TO Nasa :{Info}") 
    

     
    
def MarsImage():
    name='curiosity'
    date='2023-12-3'
    
    Api_=str(api_key)
    
    url=f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"
    
    r=requests.get(url)
    
    Data=r.json()
    #here we set 5 images to be extract an can set to any rage
    Photos=Data['photos'][:5]
    
    try:
        for index , photo in enumerate(Photos):
            camera=photo['camera']
            
            rover=photo['rover']
            
            rover_name=rover['name']
            camera_name=camera['name']
            
            full_camera_name=camera['full_name']
            
            date_of_photo=photo['earth_date']
            
            img_url=photo['img_src']
            
            p=requests.get(img_url)
            img=f'{index}.jpg'
            with open(img,'wb') as file:
                file.write(p.content)
            
            path_1="C:\\Users\\HP\\My AI assistant\\" +str(img)
            path_2="C:\\Users\\HP\\My AI assistant\\Nasa Database\\mars_images\\" +str(img)
            
            os.rename(path_1,path_2)
            
            os.startfile(path_2)
            
            Speak(f"This Image Was Captured With :{full_camera_name}")
            
            Speak(f"This Image Was Captured on:{date_of_photo}")           
    except:
        Speak("there is an error")                    
               
def Astro(start_date, end_date):
    
    url=f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"

    r=requests.get(url)
    Data=r.json()
    
    Total_Astro=Data['element_count']
  
    neo=Data['near_earth_objects']
    
    Speak(f"total astroid between {start_date} and {end_date} is: {Total_Astro}")
     
    Speak("Extracted Data for those Astroids Are Listed Below.") 
    
    for body in neo[start_date]:
        
        id=body['id']
        
        name=body['name']
        
        absolute=body['absolute_magnitude_h']
        
        print(id,name,absolute)
        
def SolarBodies(body):
    
    url="https://api.le-systeme-solaire.net/rest/bodies/"
    
    r=requests.get(url)
    
    Data=r.json()
    
    bodies=Data['bodies']
    
    Number=len(bodies)
    
    for bodyy in bodies:
        print(bodyy['id'],end=',')
    
    url=f"https://api.le-systeme-solaire.net/rest/bodies/{body}"
    
    rr=requests.get(url)
    
    data_2=rr.json()
    
    mass=data_2['mass']['massValue']
    
    volume=data_2['vol']['volValue']
    
    density=data_2['density']
    
    gravity=data_2['gravity']
    
    escape=data_2['escape']
    

    Speak(f"mass of {body} is {mass}")
    Speak(f"gravity of {body } is {gravity}")
    Speak(f"volume of {body} is {volume}")
    Speak(f"escape velocity of {body }is {escape}")
    Speak(f"density of {body} is {density}")
    
   
  
          
  
    

  
 
        

   
     
    
  


    