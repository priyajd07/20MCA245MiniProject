import pymysql
def iud(querry,value):
    con=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="cyberbullying")
    cmd=con.cursor()
    cmd.execute(querry,value)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id
def selectall(querry,value):
    con = pymysql.connect(host="localhost", user="root", password="root", port=3306,db="cyberbullying")
    cmd = con.cursor()
    cmd.execute(querry, value)
    res=cmd.fetchall()
    return res


def selectalla(querry):
    con = pymysql.connect(host="localhost", user="root", password="root", port=3306,db="cyberbullying")
    cmd = con.cursor()
    cmd.execute(querry)
    res=cmd.fetchall()
    return res


def select1(querry,value):
    con = pymysql.connect(host="localhost", user="root", password="root", port=3306,db="cyberbullying")
    cmd = con.cursor()
    cmd.execute(querry, value)
    res=cmd.fetchone()
    return res
def select1a(querry):
    con = pymysql.connect(host="localhost", user="root", password="root", port=3306,db="cyberbullying")
    cmd = con.cursor()
    cmd.execute(querry)
    res=cmd.fetchone()
    return res

def androidselectall(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='cyberbullying')
    cmd=con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data

def androidselectallnew(q):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='cyberbullying')
    cmd=con.cursor()
    cmd.execute(q)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data

