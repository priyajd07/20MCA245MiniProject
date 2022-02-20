import  pymysql
def iud(q,val):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="intelligent chatbot")
    cmd=con.cursor()
    cmd.execute(q,val)
    id = con.insert_id()
    con.commit()
    return id

def select(q):
    con = pymysql.connect(host="localhost", user="root", password="", port=3306, db="intelligent chatbot")
    cmd = con.cursor()
    cmd.execute(q)
    s =cmd.fetchall()
    con.commit()
    return s
def selectcond(q,val):
    con = pymysql.connect(host="localhost", user="root", password="", port=3306, db="intelligent chatbot")
    cmd = con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    return s
def selectone(q):
    con = pymysql.connect(host="localhost", user="root", password="", port=3306, db="intelligent chatbot")
    cmd = con.cursor()
    cmd.execute(q)
    s=cmd.fetchone()
    return s
def selectonecond(q,val):
    con = pymysql.connect(host="localhost", user="root", password="", port=3306, db="intelligent chatbot")
    cmd = con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchone()
    return s
