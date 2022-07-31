import requests 
from bs4 import BeautifulSoup
import lxml

Pagecounter = 0


for Pagecounter in range(0,13):
    urlrequest = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=php&start={Pagecounter}")

markup = urlrequest.content
print(markup)

bs = BeautifulSoup(markup , "lxml")

h = bs.find_all('h2',{'class':'css-m604qf'})
pages = bs.find_all('li',{'class':'css-1q4vxyr'})

jobs = []
pagess = []

for i in range(len(pages)):
    pages.append(pagess[i].text)

for i in range(len(h)):
    jobs.append(h[i].text)

## To get the spans 
print(bs.find_all("span"))
