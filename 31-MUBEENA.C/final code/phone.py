import requests
from bs4 import BeautifulSoup
import random
import sqlite3
import time
import urllib

def a_phone(pro,cho,head,p):
    pro=pro
    cho=cho
    headers=head
    proxy=p
    print(head)
    print(p)
    name1=[]
    price1=[]
    a_link1=[]
    name2 = []
    price2 = []
    a_link2 = []

    print(headers)
    con = sqlite3.connect('db.db')
    cursor = con.cursor()
    cursor.execute("drop table if exists phone")



    url1='https://www.amazon.in/s?k='+pro+'+'+cho+'&crid=79FMJ3TM43GT&sprefix='+pro+'+'+cho+'%2Caps%2C690&ref=nb_sb_noss'
    res = requests.get(url1,headers=headers,proxies=proxy,timeout=3)
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
                n2=name1[o]
                p2=price1[o]
                a2=a_link1[o]
                cursor.execute(
                    "create table if not exists a_phone(pid integer primary key,name text,price text,link text)")
                cursor.execute("insert into a_phone(name,price,link)values(?,?,?)",
                               (n2, p2, a2))
                con.commit()
        u='http://flipkart.com/search?q='+pro+'%20'+cho+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        res = requests.get(u, headers=headers, proxies=proxy, timeout=3)
        code = res.status_code
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
            for o in range(len(name1)):
                n3 = name2[o]
                p3 = price2[o]
                a3 = a_link2[o]
                cursor.execute(
                    "create table if not exists f_phone(pid integer primary key,name text,price text,link text)")
                cursor.execute("insert into f_phone(name,price,link)values(?,?,?)",
                               (n3, p3, a3))
                con.commit()


        lists=[]
        rating=[]
        pr=[]
        a_link=[]
        div=[]
        n=[]
        for l in div1:
            for p in l.find_all('span', {"class": "a-price-whole"}):
                if len(p) == 1:
                    for p in l.find_all('span', {"class": "a-size-medium a-color-base a-text-normal"}):
                        wor = 'iPhone'
                        a = p.text
                        a1 = a.split(',')
                        s_len = len(a1)

                        q = a.split('-')
                        q_len = len(q)

                        if wor in a:
                            if q_len == 2:
                                for pric in l.find_all('span', {"class": "a-price-whole"}):
                                    div.append(l)

                if s_len == 3:
                    for pric in l.find_all('span', {"class": "a-price-whole"}):
                        div.append(l)

        for i in div:

            for p in i.find_all('span', {"class": "a-size-medium a-color-base a-text-normal"}):
                a = p.text
                lists.append(a)
            for rate in i.find_all('span', {"class": "a-icon-alt"}):
                a =rate.text
                print(rate)
                rating.append(a)
            for prices in i.find_all('span',{"class":"a-price-whole"}):
                a=prices.text
                pr.append(a)
            for link in i.find_all('a', {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
                a = link['href']
                lin = 'https://www.amazon.in' + a
                a_link.append(lin)
        name4 = content.find_all('span', {"class": "a-size-medium a-color-base a-text-normal"})
        list=[]
        print(res.status_code)
        print(res)
        le = len(name4)
        for i in range(le):
            name = name4[i].text
            list.append(name)
        word ='iPhone'
        ram2 ='RAM'
        phonename=[]
        ram=[]
        rom=[]
        colour=[]
        print(lists)
        m=0
        rates=[]
        price=[]

        a_links=[]
        for i in lists:
            print(i)
            if word in i:
                print("yes")
                split = i.split('-')
                colour1 = split[1]
                colour1 = colour1.replace(' ', '')
                colour1 = colour1.lower()
                s = split.pop(0)
                split = s.split('(')
                name = split[0]

                name = name.lower()
                s = split.pop(1)
                s= s.replace(')','')
                phonename.append(name)
                colour.append(colour1)
                rom.append(s)
                r =''
                ram.append(r)
                r1=rating[m]
                a_l=a_link[m]
                pri=pr[m]
                print(r1)
                m = m + 1
                print(m)
                rates.append(r1)
                price.append(pri)
                a_links.append(a_l)
            else:
                tab ='Tab'
                if ram2 in i:
                    if tab not in i:
                        print("no")
                        split =i.split('(')
                        name=split[0]
                        name = name.lower()
                        name = name.replace('5g', '')
                        name = name.replace('2021 edition', '')
                        s=split.pop(1)
                        split = s.split(')')
                        name1 = split[0]
                        co=','
                        if co in i:
                            split = name1.split(',')
                            s_len=len(split)
                            if s_len==3:

                                colour1 = split[0]
                                colour1 = colour1.replace(' ', '')
                                colour1 = colour1.lower()
                                ram1 = split[1]
                                ram1 = ram1.replace(' ', '')
                                print("#############################")

                                rom1= split[2]
                                rom1 = rom1.replace(' ', '')
                                rom1 = rom1.replace('Storage', '')
                                r1 = rating[m]
                                pri=pr[m]
                                a_l=a_link[m]
                                m = m + 1
                                print(r1)
                                print(m)
                                rates.append(r1)
                                price.append(pri)
                                a_links.append(a_l)
                                phonename.append(name)
                                colour.append(colour1)
                                rom.append(rom1)
                                ram.append(ram1)
                            else:
                                m= m+1
                        else:
                            m=m+1
                    else:
                        m=m+1
                else:
                    m=m+1


        print(phonename)
        print(colour)
        print(rom)
        print(ram)
        length = len(phonename)




        for i in range(length):
            ram5=ram[i]
            rom5=rom[i]
            name5 = phonename[i]
            colour5= colour[i]
            rating5=rating[i]
            price5=price[i]
            links5=a_links[i]

            con = sqlite3.connect('db.db')
            cursor = con.cursor()
            cursor.execute(
                "create table if not exists phone(pid integer primary key,name text,colour text,rom text,ram text,rating text,price text,link text)")
            cursor.execute("insert into phone(name,colour,rom,ram,rating,price,link)values(?,?,?,?,?,?,?)", (name5, colour5, rom5,ram5,rating5,price5,links5))
            con.commit()

        print(a_links)



        print("name")
        return code
    else:

        return code

def f_phone(head,p):
    headers=head
    proxy=p
    con = sqlite3.connect('db.db')
    cursor = con.cursor()
    cursor.execute("drop table if exists pro_de")
    print("@@@@@@@@@@@@#############$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%^^^^^^^^^^^^&&&&&&&&**********(((((((((()))))))))")
    con = sqlite3.connect('db.db')
    cursor = con.cursor()
    cursor.execute("select count(*) from phone")
    row_length=cursor.fetchone()
    cursor.execute("select * from phone")
    row_length=row_length[0]
    ans = cursor.fetchall()
    for i in range(row_length):
        detail=ans[i]
        print(i)

        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        #url ='https://www.flipkart.com/search?q='+detail[1]+'+'+detail[2]+'+'+detail[3]+'+'+detail[4]+'&crid=1A8XN6LRXH56O&sprefix=samsunggalaxym21+charcoalblack+64gb+4gbram%2Caps%2C1011&ref=nb_sb_noss'
        url='https://www.flipkart.com/search?q='+detail[1]+'%20'+detail[2]+'%20'+detail[3]+'%20'+detail[4]+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        res = requests.get(url,headers=headers,proxies=proxy,timeout=3)
        code=res.status_code

        if code == 200:
            content = BeautifulSoup(res.content, "html.parser")
            product = content.find_all('div', {"class": "_2kHMtA"})
            mm=detail[1]+detail[2]+detail[3]+detail[4]
            print(mm)
            product_lists=[]

            print("*****************************************")
            if len(product)>1:
                product_lists.append(product[0])
                product_lists.append(product[1])
                product =product[0:2]
                print("pro")

                print(res)
                product_list = []
                word ='iPhone'
                ram2 ='RAM'
                phonename=[]
                ram=[]
                rom=[]
                colour=[]
                lists=[]
                price=[]
                images=[]
                flip_rating=[]
                flip_ratings=[]
                flip_prices=[]
                flip_image=[]
                flip_links=[]
                flip_link=[]
                n=0
                for pro in product_lists:
                    print("12")
                    for i in pro.find_all('div', {"class": "_30jeq3 _1_WHN1"}):
                        a = i.text
                        price.append(a)
                    for i in pro.find_all('img', {"class": "_396cs4 _3exPp9"}):
                        a = i

                        images.append(a)
                    for i in pro.find_all('div', {"class": "_3LWZlK"}):
                        a = i.text
                        flip_rating.append(a)
                    for link in pro.select("a._1fQZEK"):
                        a = link['href']
                        lin = 'https://www.flipkart.com' + a
                        flip_links.append(lin)


                    for prod in pro.find_all('div', {"class":"_4rR01T"}):
                        i = prod.text
                        if word in i:
                            f_r=flip_rating[n]
                            f_l=flip_links[n]
                            f_i=images[n]
                            f_p=price[n]
                            n=n+1
                            flip_ratings.append(f_r)
                            flip_link.append(f_l)
                            flip_image.append(f_i)
                            flip_prices.append(f_p)

                            s = i.split('(')
                            name = s[0]

                            name = name.lower()
                            s = s.pop(1)
                            s1 = s.replace(')', '')
                            split = s1.split(',')
                            colour1 = split[0]
                            colour1 = colour1.replace(' ', '')
                            colour1 = colour1.lower()
                            rom1 = split[1]
                            rom1 = rom1.replace(' ', '')
                            phonename.append(name)
                            colour.append(colour1)
                            rom.append(rom1)
                            r = ''
                            ram.append(r)
                        else:
                            co='('
                            if co in i:
                                f_r = flip_rating[n]
                                f_l = flip_links[n]
                                f_i = images[n]
                                f_p = price[n]
                                n = n + 1
                                flip_ratings.append(f_r)
                                flip_link.append(f_l)
                                flip_image.append(f_i)
                                flip_prices.append(f_p)
                                print("yes")
                                s = i.split('(')
                                name = s[0]

                                name = name.lower()
                                print(name)
                                s = s.pop(1)
                                s1 = s.replace(')', '')
                                split = s1.split(',')
                                colour1 = split[0]
                                colour1 = colour1.replace(' ', '')
                                colour1 = colour1.lower()
                                rom1 = split[1]
                                rom1 = rom1.replace(' ', '')

                                phonename.append(name)
                                colour.append(colour1)
                                rom.append(rom1)
                                for pro1 in pro.find_all('li', {"class": "rgWa7D"}):
                                    a = pro1.text
                                    a= a.split('|')
                                    a=a[0]
                                    a=a.replace(' ','')
                                    ram.append(a)
                                    break
                            else:
                                n=n+1
                num=0
                for image in flip_image:
                    image_src = image["src"]
                    urllib.request.urlretrieve(image_src, str(num) + ".jpg")
                    num += 1
                for i in range(2):
                    name5=phonename[i]
                    print(detail[1])
                    colour5=colour[i]
                    print(detail[2])
                    rom5=rom[i]
                    print(detail[3])
                    ram5=ram[i]
                    print(detail[4])
                    na =name5 +' '+ colour5 + ' '+ rom5 + ' '+ram5
                    print(na)
                    f_ra=flip_ratings[i]
                    f_li=flip_link[i]
                    f_pr=flip_prices[i]
                    filename=str(i)+'.jpg'
                    f_p=[]
                    with open(filename,'rb') as file:
                        photo=file.read()
                        f_p.append(photo)
                    a_li=detail[7]
                    a_pr=detail[6]
                    a_ra=detail[5]
                    f_im=f_p[0]
                    if detail[1]==phonename[i]:
                        print("hello")
                    if 'iphone' in na:
                        print("have")
                        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                        print(detail[1])
                        print(phonename[i])
                        print(detail[2])
                        print(colour[i])
                        print(detail[3])
                        print(rom[i])
                        l=rom[i]+' '
                        print(l)
                        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

                        if detail[1] == phonename[i] and detail[2] == colour[i] and detail[3]== l :

                            con = sqlite3.connect('db.db')
                            cursor = con.cursor()

                            cursor.execute(
                                "create table if not exists pro_de(pid integer primary key,name text,a_price text,a_rating text,a_link text,f_price text,f_rating text,f_link text,photo text)")
                            cursor.execute(
                                "insert into pro_de(name,a_price,a_rating,a_link,f_price,f_rating,f_link,photo)values(?,?,?,?,?,?,?,?)",
                                (na, a_pr, a_ra, a_li, f_pr, f_ra, f_li, f_im))
                            con.commit()
                            con.close()
                            print("working")
                        else:
                            print("not")

                    elif detail[1]==phonename[i] and detail[2]==colour[i] and detail[3]==rom[i] and detail[4]==ram[i]:

                        con = sqlite3.connect('db.db')
                        cursor = con.cursor()

                        cursor.execute(
                            "create table if not exists pro_de(pid integer primary key,name text,a_price text,a_rating text,a_link text,f_price text,f_rating text,f_link text,photo text)")
                        cursor.execute("insert into pro_de(name,a_price,a_rating,a_link,f_price,f_rating,f_link,photo)values(?,?,?,?,?,?,?,?)", (na, a_pr, a_ra, a_li, f_pr, f_ra, f_li, f_im))
                        con.commit()
                        con.close()
                        print("working")
                    else:
                        print("not")

                print(colour)
                print(rom)

                print(ram)
                time.sleep(1)

        else:

            return code
    return code

