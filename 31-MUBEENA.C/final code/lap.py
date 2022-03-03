import requests
from bs4 import BeautifulSoup
import random
import sqlite3
import time
import urllib




def f_lap(pro,cho,head,p):
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    pro = pro
    cho = cho
    headers = head
    proxy = p
    name1 = []
    price1 = []
    a_link1 = []
    name2 = []
    price2 = []
    a_link2 = []
    con = sqlite3.connect('db.db')
    cursor = con.cursor()
    cursor.execute("drop table if exists f_lap")
    url1 = 'https://www.amazon.in/s?k=' + pro + '+' + cho + '&crid=79FMJ3TM43GT&sprefix=' + pro + '+' + cho + '%2Caps%2C690&ref=nb_sb_noss'
    res = requests.get(url1, headers=headers, proxies=proxy, timeout=3)
    code = res.status_code
    if code == 200:
        content = BeautifulSoup(res.content, "html.parser")
        div1 = content.find_all('div', {"class": "a-section a-spacing-small a-spacing-top-small"})
        for l in div1:
            for p in l.find_all('span', {"class": "a-price-whole"}):
                if len(p) == 1:
                    for p in l.find_all('h2', {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"}):
                        a = p.text
                        name1.append(a)
                    for p in l.find_all('span', {"class": "a-price-whole"}):
                        m = p.text
                        price1.append(m)
                    for link in l.find_all('a', {
                        "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
                        a = link['href']
                        lin = 'https://www.amazon.in' + a
                        a_link1.append(lin)
            con = sqlite3.connect('db.db')
            cursor = con.cursor()
            cursor.execute("drop table if exists a_phone")
            for o in range(len(name1)):
                n2 = name1[o]
                p2 = price1[o]
                a2 = a_link1[o]
                cursor.execute(
                    "create table if not exists a_phone(pid integer primary key,name text,price text,link text)")
                cursor.execute("insert into a_phone(name,price,link)values(?,?,?)",
                               (n2, p2, a2))
                con.commit()
        u = 'http://flipkart.com/search?q=' + pro + '%20' + cho + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        res = requests.get(u, headers=headers, proxies=proxy, timeout=3)
        code = res.status_code
        print(code)
        if code == 200:
            content = BeautifulSoup(res.content, "html.parser")
            product = content.find_all('div', {"class": "_2kHMtA"})
            for pr in product:
                for prod in pr.find_all('div', {"class": "_4rR01T"}):
                    i = prod.text
                    name2.append(i)
                for i in pr.find_all('div', {"class": "_30jeq3 _1_WHN1"}):
                    a = i.text
                    price2.append(a)
                for link in pr.select("a._1fQZEK"):
                    a = link['href']
                    lin = 'https://www.flipkart.com' + a
                    a_link2.append(lin)
            con = sqlite3.connect('db.db')
            cursor = con.cursor()
            cursor.execute("drop table if exists f_phone")
            print("mmm")
            for o in range(len(name1)):
                n3 = name2[o]
                p3 = price2[o]
                a3 = a_link2[o]
                print(a3)
                cursor.execute(
                    "create table if not exists f_phone(pid integer primary key,name text,price text,link text)")
                cursor.execute("insert into f_phone(name,price,link)values(?,?,?)",
                               (n3, p3, a3))
                con.commit()
    name=[]
    price=[]
    a_link=[]
    u='http://flipkart.com/search?q='+pro+'%20'+cho+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    res = requests.get(u, headers=headers, proxies=proxy, timeout=3)
    code = res.status_code
    print(code)

    p1=[]
    p2=[]
    p3=[]
    if code == 200:
        content = BeautifulSoup(res.content, "html.parser")
        product = content.find_all('div', {"class": "_2kHMtA"})
        for pr in product:
            for prod in pr.find_all('div', {"class": "_4rR01T"}):
                i = prod.text
                name.append(i)
            for i in pr.find_all('div', {"class": "_30jeq3 _1_WHN1"}):
                a = i.text
                price.append(a)
            for link in pr.select("a._1fQZEK"):
                a = link['href']
                lin = 'https://www.flipkart.com' + a
                a_link.append(lin)


        for n in range(len(a_link)):
            li=a_link[n]


            res1 = requests.get(li, headers=headers, proxies=proxy, timeout=3)
            code = res1.status_code

            if code == 200:
                content = BeautifulSoup(res1.content, "html.parser")
                product1 = content.find_all('div', {"class": "_1UhVsV _3AsE0T"})
                for pro in product1:
                    for p in pro.find_all('li',{"class":"_21lJbe"}):
                        p=p.text

                        p1.append(p)

                    p2.append(p1[1])
                    p3.append(p1[3])
                    p1.clear()
                print("########")
            time.sleep(1)
    else:

        return code
    for i in range(len(price)):
        n1=name[i]
        p1=price[i]
        l1=a_link[i]
        pr1=p2[i]
        pr2=p3[i]
        con = sqlite3.connect('db.db')
        cursor = con.cursor()

        cursor.execute(
            "create table if not exists f_lap(pid integer primary key,name text,price text,link text,key text,ke text)")
        cursor.execute("insert into f_lap(name,price,link,key,ke)values(?,?,?,?,?)",
                       (n1,p1,l1,pr1,pr2))
        con.commit()
    return code


def a_lap(head,p):
    headers = head
    proxy = p
    name3=[]
    con = sqlite3.connect('db.db')
    cursor = con.cursor()
    cursor.execute("select count(*) from f_lap")
    row_length = cursor.fetchone()
    cursor.execute("select * from f_lap")

    row_length = row_length[0]
    ans = cursor.fetchall()
    for i in range(row_length):
        detail = ans[i]
        print(ans[5])
        l = 'https://www.amazon.in/s?k=' + detail[4] + '&crid=23TL6H6BV6IAW&sprefix=la%2Caps%2C3972&ref=nb_sb_noss_2'
        res = requests.get(l, headers=headers, proxies=proxy, timeout=3)
        code = res.status_code
        print(code)

        if code == 200:
            cont = BeautifulSoup(res.content, "html.parser")
            div1 = cont.find_all('div', {"class": "a-section a-spacing-small a-spacing-top-small"})
            product_lists = []
            product_lists.append(div1[0])
            product_lists.append(div1[1])

            for l in product_lists:
                for p in l.find_all('span', {"class": "a-price-whole"}):
                    if len(p) == 1:
                        for p in l.find_all('h2', {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-2"}):
                            a = p.text
                            name3.append(a)
            for f1 in range(len(name3)):
                nk = name3[f1]
                d1 = detail[4]
                if '- ' in d1:
                    d1 = d1.replace(' ', '')
                if d1 in nk:
                    d3 = detail[1]
                    d2 = detail[3]
                    con = sqlite3.connect('dbs.db')
                    cursor = con.cursor()

                    cursor.execute(
                        "create table if not exists phone(pid integer primary key,name text,link text,name1 text,price1 text)")
                    cursor.execute("insert into phone(name,link,name1,price1)values(?,?,?,?)",
                                   (d3, d2, d1, d3))
                    con.commit()

            time.sleep(1)
            return code
        else:
            return code