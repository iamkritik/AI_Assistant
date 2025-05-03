import cv2
from PIL import Image
from color import limits
import pyttsx3

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

yellow=[0,255,255]  #yellow in BGR colorspace
cap=cv2.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret,frame=cap.read()
    
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit=limits(color=yellow)
  
    
    
    mask=cv2.inRange(hsvImage,lowerLimit,upperLimit)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    
    if bbox is not None:
        x1,y1,x2,y2=bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,255),5)
    print(f"{bbox},'yellow")
    
    
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()

    