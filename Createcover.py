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
fig1.savefig('cover.png',dpi=100)




