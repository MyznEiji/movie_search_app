from bs4 import BeautifulSoup
import urllib.request as req
import json
import requests

url = 'https://www.clickthecity.com/movies/now-showing.php'
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")

urls = soup.find_all('h3', itemprop="name")
for url in urls:
    url = url.find('a')['href']

    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser")



    title = soup.find('div', id='subcontent').find('span', itemprop="name").string

    date = soup.find('div', id='subcontent').find('span', class_="year").string

    description = soup.find('div', itemprop='description').string

    poster = soup.find('div', id="poster").find('meta', itemprop="url")["content"]



