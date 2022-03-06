import os
from flask import *
from werkzeug.utils import secure_filename

from src.dbconnect import *
from src.roadcrack.fcm import test_input

app=Flask(__name__)


@app.route("/login",methods=['post'])
def login():
    print(request.form)
    username=request.form['uname']
    password=request.form['pass']
    q="SELECT * FROM `login`WHERE `username`=%s AND`password`=%s AND`usertype`='user'"
    val=username,password
    res=selectonecond(q,val)
    print(res)
    if res is None:
        return jsonify({'task': 'unsuccessfull'})
    else:
        return jsonify({'task': 'valid','lid':res[0]})

@app.route("/profile",methods=['post'])
def profile():
    id=request.form['uid']
    qry="SELECT * from `user`  where user_lid=%s"
    val=id
    res = androidselectall(qry,val)
    print(res)
    return jsonify(res)


@app.route("/userreg",methods=['post'])
def userreg():
    print(request.form)
    fname = request.form['fname']
    lname = request.form['lname']
    place = request.form['place']
    phone = request.form['phone']
    email = request.form['email']
    uname=request.form['uname']
    passd=request.form['password']
    qry="insert into login values(null,%s,%s,'user')"
    val=(uname,passd)
    id=iud(qry,val)
    qry="INSERT INTO `user` VALUE(null,%s,%s,%s,%s,%s,%s)"
    val=(id,fname,lname,place,phone,email)
    id=iud(qry,val)
    return jsonify({'task': 'success'})

@app.route("/editprofile",methods=['post'])
def editprofile():
    print(request.form)
    fname = request.form['fname']
    lname = request.form['lname']
    place = request.form['place']
    phone = request.form['phone']
    email = request.form['email']
    lid=request.form['uid']
    qry="update `user` set fname=%s,lname=%s,place=%s,phone=%s,email=%s where user_lid=%s"
    val=(fname,lname,place,phone,email,lid)
    id=iud(qry,val)
    return jsonify({'task': 'success','id':id})

@app.route("/viewroute",methods=['post'])
def viewroute():

    qry="SELECT * from route"

    res = androidselectallnew(qry)
    print(res)
    return jsonify(res)

@app.route("/feedback",methods=['post'])
def feedback():
    uid = request.form['lid']
    fd = request.form['feedback']
    qry="INSERT INTO `feedback` VALUE(null,%s,curdate(),%s)"
    val=(uid,fd)
    iud(qry,val)
    return jsonify({'task': 'success'})


@app.route("/capture",methods=['POST','GET'])
def capture():
    print(request.files)
    print(request.form)
    imei = request.form['imei']
    print(imei)
    lattitude = request.form['lattitude']
    longitude = request.form['longitude']
    print(lattitude,longitude)
    if longitude=='':
        longitude='10.8299'
        lattitude='76.0228'
    print(lattitude)
    path = 'static/photo'

    files = request.files['files']
    fname = secure_filename(files.filename)

    files.save(os.path.join(path, fname))

    try:
        res=test_input(path+"/"+fname)
        print("result",res)
        res="cracks"



        if res=="cracks":



            qry1=("insert into alert values(null,%s,%s,%s,%s,%s,now())")
            val=(imei,lattitude,longitude,fname,res,)
            iud(qry1,val)
            return jsonify({'result': res})
        else:
            return jsonify({'result':res})
    except Exception as e:
        print(e)
        return jsonify({'result': "error"})


@app.route('/loc',methods=['get','post'])
def loc():
    print(request.form)

    latitude = request.form['lati']
    longitude = request.form['longi']


    qry="SELECT `alert`.* ,(3959 * ACOS ( COS ( RADIANS(%s) * COS( RADIANS( lattitude) ) * COS( RADIANS( longitude ) - RADIANS(%s) + SIN ( RADIANS(%s) * SIN( RADIANS( lattitude ) )))))) AS user_distance FROM `alert` WHERE `alert`.`result`='cracks' HAVING user_distance  > 3.1068"

    val=(latitude,longitude,latitude)
    print(val)

    s = selectonecond(qry,val)
    print(s)
    if len(s)==0:
        print("rrrr")
        return jsonify({'task': 'error'})

    else:
        print("ok")
        return jsonify({'task': 'some distrution are there please go slowly'})
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
    # test_input(r'C:\Users\HP\PycharmProjects\road damage prediction\src\static\photo\abc.jpg')