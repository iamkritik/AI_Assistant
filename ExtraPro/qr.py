import pyqrcode

def qr(text):
   s = text
   url = pyqrcode.create(s) 
   url.png("C:\\Users\\HP\\My AI assistant\\Database\\qr_images\\qr.png", scale = 8) 

    
   