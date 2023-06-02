#!/usr/bin/env python
# coding: utf-8

# In[39]:


import requests
from bs4 import BeautifulSoup as Bs #helps in parsing
from smtplib import SMTP #helps in sending mail


# In[40]:


url="https://www.amazon.in/Apple-iPhone-14-128GB-Midnight/dp/B0BDHX8Z63/ref=sr_1_3?crid=1BJSWZM3VSB96&keywords=iphone+14&qid=1685182989&sprefix=iphone+1%2Caps%2C336&sr=8-3"

#amzon needs a header to see from which web the req is coming


# In[41]:


def extract_price():
    page=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})
    soup=Bs(page.content,"html.parser")
    price_in_string=soup.find(class_ ="a-price-whole").text.replace(",","").replace(".","") #finding the class named from inspect element and extarcting the price 
    price=float(price_in_string)  #string to number
    return price


# In[42]:


SMTP_SERVER="smtp.gmail.com"
PORT=587
EMAIL_ID="samarthpaliwal3@gmail.com"
PASSWORD="vyimejpzsnozfvvg"


# In[43]:


def sendmail():

    server=SMTP(SMTP_SERVER,PORT)
    server.starttls() #makes a secure channel (transport layer security)
    server.login(EMAIL_ID,PASSWORD)
    subject="BUY NOW"
    body="Time to buy your fav item  "+ url
    msg=f"Subject:{subject}\n\n{body}" #f for formatting
    server.sendmail(EMAIL_ID,EMAIL_ID,msg) #from ur mail to ur mail id only
    server.quit


# In[45]:


affordable_price=70000


# In[46]:


if extract_price()<=affordable_price:
    sendmail()


# In[48]:


import schedule
import time
import subprocess

def run_script():
    subprocess.run(["python", "script.ipynb"])  # Replace with the path to your script if necessary

schedule.every(10).second.do(run_script)  # Set the desired time to run the script

while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:




