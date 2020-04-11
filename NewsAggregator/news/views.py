from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import itertools
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

coverlst=['Headlines','Breaking News','Stories','Politics','Entertainment','Sports','World','Health','Video','Audio','tag','online','http','popularity','content','info','people','group','company','communication','ads','business','information']
coverlist=""
for i in coverlst:
	coverlist= coverlist+i+' '

word = WordCloud(max_font_size = 40).generate(coverlist)
plt.figure()
plt.imshow(word, interpolation ="bilinear")
plt.axis("off")
fig1=plt.gcf()
plt.tight_layout(pad = 0)
plt.show()
fig1.savefig('cover.png',dpi=100) # save in static/images/slider/cover.png---------------------------------------------------------------------TODO


# times of india
url="https://timesofindia.indiatimes.com/briefs"
r_toi = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_news=r_toi.content
soup_toi = BeautifulSoup(toi_news,"html5lib")

data = soup_toi.find_all('h2')                                                      # for title,link
image = soup_toi.find_all('div',class_='posrel')                                    # for image
details = soup_toi.find_all('div',class_='brief_box')                               # for detailed content

toi_title = []
toi_link = []
toi_image = []
toi_content = []

for news in data:
    toi_title.append(news.text.strip())
    for textlink in news.find_all('a', href=True):
        toi_link.append("https://www.timesofindia.indiatimes.com"+textlink['href'])

for texts in details:
   for content in texts.find_all('p'):
        toi_content.append(content.text.strip())

for img in image:
    for imglink in img.find_all('img'):
        toi_image.append(imglink['data-src'])

toi_title=toi_title[0:-12]

#_________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________

#ndtv
url1="https://www.ndtv.com/india?pfrom=home-mainnavgation"
r_ndtv = requests.get(url1)
ndtv_news = r_ndtv.content
soup_ndtv = BeautifulSoup(ndtv_news,'html5lib')

data = soup_ndtv.find_all('div',class_="new_storylising_img")               # for title,link,image
details = soup_ndtv.find_all('div',class_="nstory_intro")                   # for detailed content

ndtv_title = []
ndtv_link = []
ndtv_image = []
ndtv_content = []

for news in data:
    for textlink in news.find_all('a',href=True):
        ndtv_title.append(textlink['title'])
        ndtv_link.append(textlink['href'])
        for img in textlink.find_all('img'):
            ndtv_image.append(img['src'])

for texts in details:
    ndtv_content.append(texts.text.strip())

#_________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________

#hindustan times

url2="https://www.hindustantimes.com/it-s-viral/"
r_ht = requests.get(url2)
ht_news = r_ht.content
soup_ht = BeautifulSoup(ht_news,'html5lib')

data = soup_ht.find_all('div',class_="media-img")                              # for title, link, image
details = soup_ht.find_all('div',class_="para-txt")                            # for detailed content

ht_title = []
ht_link = []
ht_image = []
ht_content = []

for news in data:
    for textlink in news.find_all('a',href=True):
        ht_title.append(textlink['title'])
        ht_link.append(textlink['href'])
    for image in news.find_all('img'):
        ht_image.append(image['src'])

for texts in details:
    ht_content.append(texts.text.strip()[:-9])

ht_content = ht_content[0:-2]
ht_title = ht_title[0:-16]
ht_image = ht_image[0:-16]
ht_link = ht_link[0:-16]

#_________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________

title_list = ndtv_title + ht_title
link_list = ndtv_link + ht_link
image_list = ndtv_image + ht_image
content_list = ndtv_content + ht_content

newslist=zip(toi_title, toi_link, toi_image, toi_content, title_list, link_list, image_list, content_list )

def index(req):
    return render(req,'fiction-free/index.html', {'newslist' :newslist})
