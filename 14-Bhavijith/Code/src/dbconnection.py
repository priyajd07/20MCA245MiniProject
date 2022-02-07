import pymysql


def iud(qry,val):

    con=pymysql.connect(host="localhost",user="root",password="Root@123456",port=3306,db="crimescene_recomendation")
    cmd=con.cursor()
    cmd.execute(qry,val)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id


def selectone(qry,val):


    con = pymysql.connect(host="localhost", user="root", password="Root@123456", port=3306, db="crimescene_recomendation")
    cmd = con.cursor()
    cmd.execute(qry, val)
    res=cmd.fetchone()
    return res

def selectonnew(qry):
    con = pymysql.connect(host="localhost", user="root", password="Root@123456", port=3306, db="crimescene_recomendation")
    cmd = con.cursor()
    cmd.execute(qry)
    res = cmd.fetchone()
    return res

def selectall(qry,val):
    con = pymysql.connect(host="localhost", user="root", password="Root@123456", port=3306, db="crimescene_recomendation")
    cmd = con.cursor()
    cmd.execute(qry,val)
    res = cmd.fetchall()
    return res


def selectallnew(qry):
    con = pymysql.connect(host="localhost", user="root", password="Root@123456", port=3306, db="crimescene_recomendation")
    cmd = con.cursor()
    cmd.execute(qry)
    res = cmd.fetchall()
    return res
