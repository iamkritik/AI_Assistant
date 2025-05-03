import cv2
import matplotlib.pyplot as plt
import easyocr
import pyttsx3
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
    
Speak('sir can you provide the path of the iamge')
path=input('enter the path:')
updatePath=path.replace('/','\\')
  

img=cv2.imread(f"{updatePath}")



    
reader=easyocr.Reader(['en'],gpu=False)

text_=reader.readtext(img)
threshold=0.25
for t in text_:
    print(t)
    bbox,text,score=t
    Speak(f"i found the written text in image:{text}, with cofidence of {round(score,2)}")
            
    if score>threshold:
            
        cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),5)
        cv2.putText(img,text,bbox[0],cv2.FONT_HERSHEY_SIMPLEX,0.65,(255,0,0),2)
        cv2.imshow("faces",img)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
cv2.destroyAllWindows()

    


