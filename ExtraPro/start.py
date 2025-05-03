import os
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
def GoogleImage():
    o=open('C:\\Users\\HP\\My AI assistant\\Data.txt','rt')
    query=str(o.read())
    o.close()
    p=open('C:\\Users\\HP\\My AI assistant\\Data.txt','r+')
    p.truncate(0)
    
    webdriver="C:\\Users\\HP\\My AI assistant\\Database\\Webdriver\\chromedriver.exe"
    photos="C:\\Users\\HP\\My AI assistant\\Database\\GooglePhotos"
    
    search_keys= [f"{query}"]
    number=10
    head=False
    max=(1000,1000)
    min=(0,0)
    
    for search_keys in search_keys:
        image_search=GoogleImageScraper(webdriver,photos,search_keys,number,head,min,max)
        image_url=image_search.find_image_urls()
        image_search.save_images(image_url)
        
    os.startfile(photos)    
        
GoogleImage()        