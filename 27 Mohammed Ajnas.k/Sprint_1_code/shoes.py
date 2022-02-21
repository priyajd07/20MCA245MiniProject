import requests
from bs4 import BeautifulSoup
import random
import sqlite3
import time
import urllib




def a_shoe(pro,cho,head,p):
    pro=pro
    cho=cho
    headers=head
    proxy=p
    print(head)
    print(p)

    print(headers)
    con = sqlite3.connect('db.db')
    cursor = con.cursor()
    cursor.execute("drop table if exists phone")
    url1 = 'https://www.amazon.in/s?k=shoes+shoes&crid=3T6HKL14VRUJ7&sprefix=shoes+shoe%2Caps%2C320&ref=nb_sb_noss_1'
    # url1='https://www.amazon.in/s?k='+pro+'+'+cho+'&page='+i+'&crid=20WZGJYAWDQ5N&qid=1643893122&sprefix='+pro+'+'+cho+'%2Caps%2C2071&ref=sr_pg_'+i
    # for i in range(1,4):
    # Pick a random user agent
    user_agent = random.choice(user_agent_list)
    # Set the headers
    headers = {'User-Agent': user_agent}
    # Make the request
    res = requests.get(url1, headers=headers, proxies=proxy, timeout=3)
    code = res.status_code
    name = []
    price = []
    a_link = []
    print(code)
    if code == 200:
        content = BeautifulSoup(res.content, "html.parser")
        div1 = content.find_all('div', {"class": "a-section a-spacing-base a-text-center"})
        for l in div1:
            for p in l.find_all('h2', {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"}):
                a = p.text
                name.append(a)
            for p in l.find_all('span', {"class": "a-offscreen"}):
                m = p.text
                price.append(m)
            for link in l.find_all('a', {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
                a = link['href']
                lin = 'https://www.amazon.in' + a
                a_link.append(lin)
        print(name)
        print(price)
        print(a_link)


def f_shoe(pro,cho):
    print("hi")