import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/-/en/Digital-Megapixel-Display-Viewfinder-SEL-2870/dp/B00FWUDEEC/ref=sr_1_4?dchild=1&keywords=sony+a7&qid=1620664062&s=ce-de&sr=1-4'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price= soup.find(id="priceblock_ourprice").get_text()
   
    p_price = price.replace(',',"")
    converted_price = float(p_price[1:7])
    
    if(converted_price < 1.000):
        send_mail()
        
    print(converted_price)
    print(title.strip())
    
    if(converted_price > 900):
       send_mail()
        

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('abida.taposhi@gmail.com' , 'mawurwbdsuwpgzam')
    
    subject= 'Price fell down!!'
    body = 'check this amazon link https://www.amazon.de/-/en/Digital-Megapixel-Display-Viewfinder-SEL-2870/dp/B00FWUDEEC/ref=sr_1_4?dchild=1&keywords=sony+a7&qid=1620664062&s=ce-de&sr=1-4'
 
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'abida.taposhi@gmail.com',
        'fowzia.abida21@gmail.com',
         msg
    )
    
    print("email has been sent")
    
    server.quit()


check_price()
  
    