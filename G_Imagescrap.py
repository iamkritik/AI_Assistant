import requests 
from bs4 import BeautifulSoup 
import pyttsx3
import speech_recognition as sr
from PIL import Image 
from time import sleep

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
  

Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

# The User-Agent request header contains a characteristic string 
# that allows the network protocol peers to identify the application type, 
# operating system, and software version of the requesting software user agent.
# needed for google search
u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} 

Image_Folder = 'C:\\Users\\HP\\My AI assistant\\GooglePhotos'

def main():
    download_images()

def download_images():
    Speak('whose image you want to get')
    # data = input('enter name here:-')
    data=TakeCommand('audio')
    Speak('Enter the number of images you want: ')
    num_images = int(input('enter here:-'))
    
    Speak(f'Searching Images of {data}....')
    
    search_url = Google_Image + 'q=' + data #'q=' because its a query
    
    # request url, without u_agnt the permission gets denied
    response = requests.get(search_url, headers=u_agnt)
    html = response.text #To get actual result i.e. to read the html data in text mode
    
    
    b_soup = BeautifulSoup(html, 'html.parser') #html.parser is used to parse/extract features from HTML files
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
    

    count = 0
    imagelinks= []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if (count >= num_images):
                break
            
        except KeyError:
            continue
    
    Speak(f'Found {len(imagelinks)} images')
    Speak('please wait')
    Speak(f'downloading images of {data}...')

    for i, imagelink in enumerate(imagelinks):
        response = requests.get(imagelink)
        
        imagename = Image_Folder + '\\' + data + str(i+1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)

    Speak('Download Completed!')
    Speak('Downloaded file iamges are in GoooglePhotos folder you can see there')
  

    

if __name__ == '__main__':
    main()