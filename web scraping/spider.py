import requests
import time
import random
from bs4 import BeautifulSoup as bs
import json
f=open('links.json',encoding="utf8")

d={}
d=json.load(f)
f.close() 


urls=["https://steamunlocked.net/category/sports/"]
for url in urls:
    for pages in range(1,11):
        pg=f'{url}page/{pages}/'
        r=random.randint(1,5)
        time.sleep(r)
        req = requests.get(pg)
        soup = bs(req.text, 'html.parser')
        print(f"Crawling... at page: {pages}, at link: {pg}")

        for link in soup.findAll('div',{'class':'cover-item category'}):
            a=link.find('a')
            title=a.find('h1')
            pgurl=a.get('href')
            d[title.text]=a.get('href')
            #print(d)
            #f.write(f"Title: {title.text} \n Link: {a.get('href')} \n\n")

with open("links.json",'w') as f:
    json.dump(d,f,sort_keys=True)

