import  pymysql
def iud(q,val):
    con=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="road damage")
    cmd=con.cursor()
    cmd.execute(q,val)
    id = con.insert_id()
    con.commit()
    return id
def select(q):
    con = pymysql.connect(host="localhost", user="root", password="root", port=3306, db="road damage")
    cmd = con.cursor()
    cmd.execute(q)
    s =cmd.fetchall()
    con.commit()
    return s
def selectcond(q,val):
    con = pymysql.connect(host="localhost", user="root", password="root", port=3306, db="road damage")
    cmd = con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    return s
def selectone(q):
    con = pymysql.connect(host="localhost", user="root", password="root", port=3306, db="road damage")
    cmd = con.cursor()
    cmd.execute(q)
    s=cmd.fetchone()
    return s
def selectonecond(q,val):
    con = pymysql.connect(host="localhost", user="root", password="root", port=3306, db="road damage")
    cmd = con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchone()
    return s
def androidselectall(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='road damage')
    cmd=con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
def androidselectone(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='road damage')
    cmd=con.cursor()
    cmd.execute(q,val)
    s = cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
def androidselectallnew(q):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='road damage')
    cmd=con.cursor()
    cmd.execute(q)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data