import requests
import urllib
from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3
from bs4 import BeautifulSoup
import phone ,shoes,lap,watch,tab
import os
import sys
import random


import csv
app = Flask(__name__)
app.secret_key="123"

def get_proxies():
    proxy_url="https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt"
    r = requests.get(proxy_url)
    soup = BeautifulSoup(r.content, "html.parser").find_all("td",{"class":"blob-code blob-code-inner js-file-line"})
    proies = [proxy.text for proxy in soup]
    return proies
def get_random_proxy(proxies):
    return {"https//":random.choice((proxies))}

proxies=get_proxies()
working = []
def get_working_proxies():

    for i in range(30):
        proxy = get_random_proxy(proxies)
        print(f"using {proxy}...")
        try:
            r= requests.get("https://www.google.com/",proxies=proxy, timeout=3)
            if r.status_code == 200:
                print('200')
                working.append(proxy)
                break
        except:
            pass
    return working

proxy=get_working_proxies()
print(proxy[0])
proxy =proxy[0]
print(proxy)
print(working)

user_agent_list = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',


    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/44.1.54 like Chrome/44.0.2403.63 Safari/537.36'
]

#for i in range(1,4):
#Pick a random user agent
user_agent = random.choice(user_agent_list)
#Set the headers
headers = {'User-Agent': user_agent}
print("hi")
s=['home1.html']
def amazon(pro,cho):
    if cho == 'phone':
        print("amazon")
        print(pro)
        print(cho)
        st =300
        if st == 200:
            return st
        else:

            return st

    else:
        print("amazon")

def flip(pro,cho):
    if cho == 'phone':
        print("flip")
        print(pro)
        print(cho)
        sc=200
        return sc


    else:
        print("flip")
@app.route("/")
def index():

    if 'name' in session:
        return render_template("userpage.html")
    else:
        return render_template("home1.html")
@app.route("/loginpage")
def loginpage():
    return render_template("home.html")


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        con=sqlite3.connect("db.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from user where email=? and password=?",(email,password))
        data=cur.fetchone()



        if data:
            session.clear()
            session["email"]=data["email"]
            session["password"]=data["password"]
            s1='userpage.html'
            s.clear()
            s.append(s1)
            return render_template("userpage.html")
        else:
            flash("Username and Password Mismatch","danger")
    return redirect(url_for("home"))

@app.route('/register',methods=['GET','POST'])
def register():
    print(request.method)
    if request.method=='POST':
        print("hi")

        try:
            name=request.form.get('name')
            email=request.form.get('email1')
            password=request.form.get('password1')
            print(name)
            con=sqlite3.connect("db.db")
            cur=con.cursor()
            cur.execute("insert into user(name,email,password)values(?,?,?)",(name,email,password))
            con.commit()
            flash("Record Added  Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return render_template("home.html")
            con.close()

    return render_template('register.html')
@app.route('/logout')
def logout():
    session.clear()
    s1='home1.html'
    s.clear()
    s.append(s1)
    return render_template("home.html")
@app.route('/pro_detail')
def pro_detail():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("select * from pro_de")
    s = cur.fetchall()
    path = 'C:/Users/DELL/PycharmProjects/mini_project/static/images'
    os.chdir(path)
    print("lkjjlnbk")
    count = 1
    for img in s:
        with open("{}.jpg".format(count), "wb") as f:
            f.write(img[8])
            count = count + 1
    path = 'C:/Users/DELL/PycharmProjects/mini_project'
    os.chdir(path)
    return render_template('pro_detail.html', val=s)

@app.route('/view')
def view():

    id = request.args.get('id')
    cwd = os.getcwd()
    print(cwd)
    s=id
    print(s)

    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("select * from pro_de where pid=?",(s,))
    s = cur.fetchall()
    return render_template('view.html',val=s)
view_v=[]
@app.route('/a_price')
def a_price():
    print("hi")
    print(view_v)
    id = request.args.get('id1')
    view_v.append(id)
    print(id)
    s=id
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("select * from a_phone where pid=?", (s,))
    print("ooooo")
    s = cur.fetchall()
    return render_template('price1.html',val=s)
@app.route('/f_price')
def f_price():
    print("hi")
    print(view_v)
    id = request.args.get('id1')
    view_v.append(id)
    print(id)
    s=id
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("select * from f_phone where pid=?", (s,))
    print("ooooo")
    s = cur.fetchall()
    return render_template('price2.html',val=s)
@app.route('/price1',methods=['POST','GET'])
def price1():
    id = request.args.get('id')
    print(id)
    epr=request.form['mail1']
    if 'name'in session:
        print(session['name'])
        amazon='amazon'
        con = sqlite3.connect('db.db')
        cursor = con.cursor()
        cursor.execute(
            "create table if not exists price(pid integer primary key,email text,price text,link text,site text)")
        cursor.execute("insert into price(email,price,link,site)values(?,?,?,?)", (session['name'], epr,id,amazon))
        con.commit()
        con.close()
        return redirect(url_for('a_price',id=id))
    else:
        print("no")
        return redirect(url_for('loginpage'))
@app.route('/price2',methods=['POST','GET'])
def price2():
    id = request.args.get('id')
    print(id)
    epr=request.form['mail2']
    if 'name'in session:
        print(session['name'])
        flip1='flipkart'
        con = sqlite3.connect('db.db')
        cursor = con.cursor()
        cursor.execute(
            "create table if not exists price(pid integer primary key,email text,price text,link text,site text)")
        cursor.execute("insert into price(email,price,link,site)values(?,?,?,?)", (session['name'], epr,id,flip1))
        con.commit()
        con.close()
        return redirect(url_for('f_price',id=id))
    else:
        print("no")
        return redirect(url_for('loginpage'))

@app.route('/aphone')
def aphone():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("select * from a_phone")
    s = cur.fetchall()
    cur.execute("select * from f_phone")
    m = cur.fetchall()
    return s,m

@app.route('/', methods=['POST'])
def getvalue():
    print(s[0])
    product = request.form['name_in']
    choice = request.form['choice']
    if choice == 'phone':
        n='1'
        st =phone.a_phone(product,choice,headers,proxy)
        if st==200:
            sc=phone.f_phone(headers,proxy)
            if sc==200:
                print("popup")
                flash("Server ok", "danger")
                sm,sk=aphone()
                return render_template('aphone.html',val1=sm,val2=sk)
            else:
                flash("Server busy", "danger")
                return render_template(s[0])
        else:
            flash("Server busy", "danger")
            return render_template(s[0])
    elif choice=='laptop':
        st = lap.a_phone(product, choice)
        if st == 200:
            sc = lap.f_phone(product, choice)
            if sc == 200:
                print("popup")
                flash("Server ok", "danger")
                sm = pro_detail()
                return render_template('pro_detail.html', val=sm)
            else:
                flash("Server busy", "danger")
                return render_template(s[0])
        else:
            flash("Server busy", "danger")
            return render_template(s[0])
    elif choice=='watches':
        st = watch.a_phone(product, choice)
        if st == 200:
            sc = watch.f_phone(product, choice)
            if sc == 200:
                print("popup")
                flash("Server ok", "danger")
                sm = pro_detail()
                return render_template('pro_detail.html', val=sm)
            else:
                flash("Server busy", "danger")
                return render_template(s[0])
        else:
            flash("Server busy", "danger")
            return render_template(s[0])

    elif choice=='shoes':
        n=1
        st = shoes.a_phone(product, choice)
        if st == 200:
            sc = shoes.f_phone(product, choice)
            if sc == 200:
                print("popup")
                flash("Server ok", "danger")
                sm,sk = pro_detail()
                return render_template('pro_detail.html', val1=sm,val2=sk)
            else:
                flash("Server busy", "danger")
                return render_template(s[0])
        else:
            flash("Server busy", "danger")
            return render_template(s[0])
    else:
        st = tab.a_phone(product, choice)
        if st == 200:
            sc = tab.f_phone(product, choice)
            if sc == 200:
                print("popup")
                flash("Server ok", "danger")
                sm = pro_detail()
                return render_template('pro_detail.html', val=sm)
            else:
                flash("Server busy", "danger")
                return render_template(s[0])
        else:
            flash("Server busy", "danger")
            return render_template(s[0])
    #flip(product,choice)



app.run()