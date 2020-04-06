from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

r_toi = requests.get("https://timesofindia.indiatimes.com/briefs")
soup_toi = BeautifulSoup(r_toi.content,"html5lib")

headings_toi = soup_toi.find_all('h2')

headings_toi = headings_toi[0:-13]

news_toi=[]

for head in headings_toi:
    news_toi.append(head.text)


# Create your views here.

def index(req):
    return render(req,'index.html', {'news_toi':news_toi})
