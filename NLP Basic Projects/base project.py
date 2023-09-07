import urllib.request
from bs4 import BeautifulSoup
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

# Get the info from the website
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/tesla')
html = response.read()

soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip=True)

tokens = [t for t in text.split() if t.lower() not in stopwords.words('english')]

freq = nltk.FreqDist(tokens)

for key, val in freq.items():
    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)
