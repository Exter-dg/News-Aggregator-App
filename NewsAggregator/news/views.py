from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import itertools
#from wordcloud import Wordcloud
import matplotlib.pyplot as plt
#cover 

#coverlist=['Headlines','Breaking News','Stories','Politics','Entertainment','Sports','World','Health']
#word = WordCloud(max_font_size = 40).generate(coverlist) 
#plt.figure() 
#plt.imshow(word, interpolation ="bilinear") 
#plt.axis("off") 
#fig1=plt.gcf()
#plt.show()
#fig1.savefig('cover.png',dpi=100)

# times of india
url="https://timesofindia.indiatimes.com/briefs"
r_toi = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_news=r_toi.content
soup_toi = BeautifulSoup(toi_news,"html5lib")

data = soup_toi.find_all('h2')
image = soup_toi.find_all('div',class_='posrel')

toi_title = []
toi_link = []
toi_image = []

for news in data:
    toi_title.append(news.text.strip())
    for textlink in news.find_all('a', href=True):
        toi_link.append("https://www.timesofindia.indiatimes.com"+textlink['href'])

for img in image:
    for imglink in img.find_all('img'):
        toi_image.append(imglink['data-src'])

toi_title=toi_title[0:-13]
toi=zip(toi_title,toi_link,toi_image)



# news 18
url="https://www.news18.com/politics/"
r_n18 = requests.get(url)
n18_news = r_n18.content
soup_n18 = BeautifulSoup(n18_news,'html5lib')

data = soup_n18.find_all('div',class_="blog-list-blog")

n18_title = [] 
n18_link = []
n18_image = []

for news in data:
    n18_title.append(news.text.strip())
    for p in news.find_all('figure'):
        for textlink in p.find_all('a', href=True):
            n18_link.append(textlink['href'])
        for imglink in p.find_all('img'):
            n18_image.append(imglink['data-src'])

n18=zip(n18_title,n18_link, n18_image)
        

def index(req):
    return render(req,'index.html', {'toi':toi,'n18':n18})