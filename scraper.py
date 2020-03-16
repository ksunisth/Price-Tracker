import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='' # 'amazon link for a product'

headers = {"User-Agent": ''} #'user agent' search my user agent on google

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:4]+price[5:8]) #to get price in float without currency symbol

    if(converted_price< ): #compares price. enter upper-limit amount for the product
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

     server.login('', '') #'from email-id', 'app-password for mail'

     subject = "Price fell down!"
     body = "Check the amazon link '' "# 'amazon link for the product'

     msg = f"Subject: {subject}\n\n{body}"

     server.sendmail('','',msg) #'from email-id', 'to email-id'

     print("E-mail has benn sent!")
     server.quit()

while(True):
    check_price()
    time.sleep(86400) # checks price once a day
