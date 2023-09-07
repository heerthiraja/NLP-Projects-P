import urllib.request #Handling URL


from bs4 import BeautifulSoup #Handling or parsing html files

#import nltk #toolkit
#nltk.download('stopwords') #or is was extracted

import nltk #toolkit
nltk.download('stopwords')

from nltk.corpus import stopwords

#get the info from website
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/Tesla,_Inc.')
html = response.read()
#print(html)
'''
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
#print(text)

tokens = [t for t in text.split()]
#print(tokens)

#removing stop works
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

#
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)

'''
