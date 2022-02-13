import pymysql
def iud(query,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='real_estate')
    cmd=con.cursor()
    cmd.execute(query,val)
    con.commit()
    id=cmd.lastrowid
    return id
def selectall(query):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='real_estate')
    cmd=con.cursor()
    cmd.execute(query)
    s=cmd.fetchall()
    return s
def selectsome(query,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='real_estate')
    cmd=con.cursor()
    cmd.execute(query,val)
    s=cmd.fetchall()
    return s
def selectone(query,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='real_estate')
    cmd=con.cursor()
    cmd.execute(query,val)
    s=cmd.fetchone()
    return s