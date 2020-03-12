from bs4 import BeautifulSoup
import urllib.request as req
import json
import requests

import mysql.connector


url = 'https://www.clickthecity.com/movies/now-showing.php'



def get_urls(url):

    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser")
    urls = soup.find_all('h3', itemprop="name")

    return urls


def is_nulldata(data):
    if not data:
        return ""
    else:
        return data.string


def get_data(url):
    # get the link for each page
    url = url.find('a')['href']
    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser")


    # get the data
    title = is_nulldata(soup.find('div', id='subcontent').find('span', itemprop="name"))
    print(title)
    date = is_nulldata(soup.find('div', id='subcontent').find('span', class_="year"))
    description = is_nulldata(soup.find('div', id='details').find('div', itemprop='description'))
    poster = soup.find('div', id="poster").find('meta', itemprop="url")["content"]

    return title, date, description, poster


def save_data(title, date, description, poster):
    # save on db
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password="",
        database='movie_serach')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies(title, date, description, poster) values(%s,%s,%s,%s)" , (title, date, description, poster))
    conn.commit()
    cursor.close()
    conn.close()



if __name__ == '__main__':
    # get the html

    urls = get_urls(url)

    for url in urls:
        title, date, description, poster = get_data(url)
        save_data(title, date, description, poster)
